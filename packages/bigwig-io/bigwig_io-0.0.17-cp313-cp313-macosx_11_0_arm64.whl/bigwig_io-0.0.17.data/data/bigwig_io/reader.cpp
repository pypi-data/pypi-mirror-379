#pragma once

#include <algorithm>
#include <chrono>
#include <cstdint>
#include <deque>
#include <fstream>
#include <functional>
#include <future>
#include <map>
#include <mutex>
#include <string>
#include <tuple>
#include <vector>
#include <cmath>
#include <limits>

#include "structs.hpp"
#include "byte_util.cpp"
#include "file_util.cpp"
#include "util.cpp"
#include "reader_header.cpp"
#include "reader_data.cpp"






class BigwigReader {
    std::string path;
    uint64_t parallel;
    float zoom_correction = 0.33;
    std::shared_ptr<BufferedFilePool> file;

public:
    MainHeader main_header;
    std::vector<ZoomHeader> zoom_headers;
    TotalSummary total_summary;
    ChrTreeHeader chr_tree_header;
    std::vector<ChrTreeLeaf> chr_tree;
    std::map<std::string, ChrTreeLeaf> chr_map;

    BigwigReader(
        const std::string& path_,
        uint64_t parallel_ = 24,
        float zoom_correction_ = 0.33
    ) : path(path_), parallel(parallel_), zoom_correction(zoom_correction_) {
        file = std::make_shared<BufferedFilePool>(path, "r", parallel);
    }

    std::future<void> read_headers() {
        return std::async(std::launch::async, [this]() {
            main_header = read_main_header(*file);
            zoom_headers = read_zoom_headers(*file, main_header.zoom_levels);
            total_summary = read_total_summary(*file, main_header.total_summary_offset);
            chr_tree_header = read_chr_tree_header(*file, main_header.chr_tree_offset);
            chr_tree = read_chr_tree(*file, main_header.chr_tree_offset + 32, chr_tree_header.key_size);
            chr_map = convert_chr_tree_to_map(chr_tree);
        });
    }

    int32_t select_zoom(uint32_t bin_size) {
        int32_t best_level = -1;
        uint32_t best_reduction = 0;
        bin_size = static_cast<uint32_t>(std::round(bin_size * zoom_correction));
        for (uint16_t i = 0; i < zoom_headers.size(); ++i) {
            uint32_t reduction = zoom_headers[i].reduction_level;
            if (reduction <= bin_size && reduction > best_reduction) {
                best_reduction = reduction;
                best_level = i;
            }
        }
        return best_level;
    }

    ChrTreeLeaf get_chr_entry(const std::string& chr_id) {
        std::string chr_key = chr_id.substr(0, chr_tree_header.key_size);
        auto it = chr_map.find(chr_key);
        if (it != chr_map.end()) return it->second;
        it = chr_map.find(lowercase(chr_key));
        if (it != chr_map.end()) return it->second;
        it = chr_map.find(uppercase(chr_key));
        if (it != chr_map.end()) return it->second;
        if (chr_id.length() >= 3 && chr_id.substr(0, 3) == "chr") {
            chr_key = chr_id.substr(3).substr(0, chr_tree_header.key_size);
        } else {
            chr_key = ("chr" + chr_id).substr(0, chr_tree_header.key_size);
        }
        it = chr_map.find(chr_key);
        if (it != chr_map.end()) return it->second;
        it = chr_map.find(lowercase(chr_key));
        if (it != chr_map.end()) return it->second;
        it = chr_map.find(uppercase(chr_key));
        if (it != chr_map.end()) return it->second;
        std::string available;
        for (const auto& entry : chr_map) {
            if (!available.empty()) available += ", ";
            available += entry.first;
        }
        throw std::runtime_error(fstring("chr {} not in bigwig ({})", chr_id, available));
    }

    std::vector<Loc> parse_locs(
        const std::vector<std::string>& chr_ids,
        const std::vector<int64_t>& starts,
        const std::vector<int64_t>& ends,
        uint32_t span = 1,
        uint32_t bin_size = 1) {

        if (chr_ids.size() != starts.size() || (!ends.empty() && chr_ids.size() != ends.size())) {
            throw std::runtime_error("length mismatch between chr_ids, starts or ends");
        }
        std::vector<Loc> locs(chr_ids.size());
        uint64_t values_offset = 0;
        for (uint64_t i = 0; i < chr_ids.size(); ++i) {
            auto chr_entry = get_chr_entry(chr_ids[i]);
            int64_t start = starts[i];
            int64_t end = ends.empty() ? starts[i] + span : ends[i];
            if (start > end) {
                throw std::runtime_error(fstring("loc {}:{}-{} at index {} invalid", chr_ids[i], start, end, i));
            }
            Loc loc;
            loc.chr_index = chr_entry.chr_index;
            loc.start = start < 0 ? 0 : start;
            loc.end = end < 0 ? 0 : end;
            loc.input_index = i;
            loc.values_index = values_offset + (loc.start - start) / bin_size;
            locs[i] = loc;
            values_offset += (end - start) / bin_size;
        }
        std::sort(locs.begin(), locs.end(), [](const Loc& a, const Loc& b) {
            return std::tie(a.chr_index, a.start) < std::tie(b.chr_index, b.start);
        });
        return locs;
    }

    uint64_t get_coverage(const std::vector<Loc>& locs) {
        uint64_t coverage = 0;
        for (const auto& loc : locs) {
            coverage += (loc.end - loc.start);
        }
        return coverage;
    }

    std::vector<float> read_values(
        const std::vector<std::string>& chr_ids,
        const std::vector<int64_t>& starts,
        uint32_t span,
        uint32_t bin_size = 1,
        std::string bin_mode = "mean",
        float def_value = 0.0f,
        int32_t zoom = 0,
        std::function<void(uint64_t, uint64_t)> progress = nullptr) {
        
        if (bin_size == 0 || bin_size > span) bin_size = span;
        auto locs = parse_locs(chr_ids, starts, {}, span, bin_size);
        ProgressTracker tracker(get_coverage(locs), progress);

        int32_t zoom_index = zoom < 0 ? -1 : zoom > 0 ? zoom - 1 : select_zoom(bin_size);
        uint64_t tree_offset = (zoom_index < 0) ?
            main_header.full_index_offset + 48 : 
            zoom_headers[zoom_index].index_offset + 48;
        TreeNodeGenerator tree_nodes(*file, locs, tree_offset);
        
        if (bin_mode == "single") {
            return read_values_at_locs(
                *file,
                main_header.uncompress_buffer_size,
                locs,
                tree_nodes,
                span,
                bin_size,
                def_value,
                zoom_index,
                tracker
            );
        } else if (bin_mode == "mean") {
            return read_values_stats_at_locs(
                *file,
                main_header.uncompress_buffer_size,
                locs,
                tree_nodes,
                span,
                bin_size,
                def_value,
                zoom_index,
                tracker
            );
        } else {
            throw std::runtime_error("bin_mode " + bin_mode + " invalid");
        }

    }

    std::vector<float> quantify(
        const std::vector<std::string>& chr_ids,
        const std::vector<int64_t>& starts,
        const std::vector<int64_t>& ends = {},
        uint32_t span = 1,
        uint32_t bin_size = 1,
        float def_value = 0.0f,
        std::string reduce = "mean",
        int32_t zoom = 0,
        std::function<void(uint64_t, uint64_t)> progress = nullptr) {
        
        if (bin_size == 0 || bin_size > span) bin_size = span;
        auto locs = parse_locs(chr_ids, starts, ends, span, bin_size);
        ProgressTracker tracker(get_coverage(locs), progress);

        int32_t zoom_index = zoom < 0 ? -1 : zoom > 0 ? zoom - 1 : select_zoom(bin_size);
        uint64_t tree_offset = (zoom_index < 0) ?
            main_header.full_index_offset + 48 : 
            zoom_headers[zoom_index].index_offset + 48;
        TreeNodeGenerator tree_nodes(*file, locs, tree_offset);

        return read_stats_at_locs(
            *file,
            main_header.uncompress_buffer_size,
            locs,
            tree_nodes,
            def_value,
            reduce,
            zoom_index,
            tracker
        );

    }

    std::vector<float> profile(
        const std::vector<std::string>& chr_ids,
        const std::vector<int64_t>& starts,
        uint32_t span,
        uint32_t bin_size = 1,
        std::string bin_mode = "mean",
        float def_value = 0.0f,
        std::string reduce = "mean",
        int32_t zoom = 0,
        std::function<void(uint64_t, uint64_t)> progress = nullptr) {
        
        if (bin_size == 0 || bin_size > span) bin_size = span;
        auto values = read_values(chr_ids, starts, span, bin_size, bin_mode, def_value, zoom, progress);

        uint32_t bin_count = values.size() / chr_ids.size();
        std::vector<float> profile(bin_count, std::numeric_limits<float>::quiet_NaN());
        for (uint32_t col = 0; col < bin_count; ++col) {
            uint64_t count = 0;
            for (uint64_t row = 0; row < chr_ids.size(); ++row) {
                auto value = values[row * bin_count + col];
                if (std::isnan(value)) continue;
                count += 1;
                if (reduce == "mean" || reduce == "sum") {
                    profile[col] += value;
                } else if (reduce == "min") {
                    if (value < profile[col] || row == 0) {
                        profile[col] = value;
                    }
                } else if (reduce == "max") {
                    if (value > profile[col] || row == 0) {
                        profile[col] = value;
                    }
                } else {
                    throw std::runtime_error("reduce " + reduce + " invalid");
                }
            }
            if (reduce == "mean" && count > 0) {
                profile[col] /= count;
            }
        }
        return profile;

    }

    void to_bedgraph(
        const std::string& output_path,
        std::vector<std::string> chr_ids = {},
        int32_t zoom = -1
    ) {
        std::vector<Loc> locs;
        if (chr_ids.empty()) chr_ids = get_map_keys(chr_map);
        for (std::string chr_id : chr_ids) {
            auto chr_entry = get_chr_entry(chr_id);
            Loc loc;
            loc.chr_index = chr_entry.chr_index;
            loc.start = 0;
            loc.end = chr_entry.chr_size;
            locs.push_back(loc);
        }

        int32_t zoom_index = zoom <= 0 ? -1 : zoom - 1;
        uint64_t tree_offset = (zoom_index < 0) ?
            main_header.full_index_offset + 48 : 
            zoom_headers[zoom_index].index_offset + 48;
        TreeNodeGenerator generator(*file, locs, tree_offset);

        auto output_file = open_file(output_path, "w");
        auto write_line = [&](std::string chr_id, uint32_t start, uint32_t end, float value) {
            std::string line =
                chr_id + "\t" +
                std::to_string(start) + "\t" +
                std::to_string(end) + "\t" +
                std::to_string(value) + "\n";
            output_file->write_string(line);
        };

        TreeNodeGeneratorNext result;
        while (!(result = generator.next()).done) {
            DataTreeLeaf node = result.node;
            ByteArray buffer = file->read(node.data_size, node.data_offset).get();
            if (main_header.uncompress_buffer_size > 0) buffer = buffer.decompress(main_header.uncompress_buffer_size);
            
            DataIntervalGenerator data_intervals(node, buffer, zoom_index >= 0);
            DataIntervalGeneratorNext data_interval;
            while (!(data_interval = data_intervals.next()).done) {
                DataInterval interval = data_interval.data;
                std::string chr_id = chr_tree[interval.chr_index].key;
                write_line(chr_id, interval.start, interval.end, interval.value);
            }
        }
    }

    void to_wig(
        const std::string& output_path,
        std::vector<std::string> chr_ids = {},
        int32_t zoom = -1
    ) {
        std::vector<Loc> locs;
        if (chr_ids.empty()) chr_ids = get_map_keys(chr_map);
        for (std::string chr_id : chr_ids) {
            auto chr_entry = get_chr_entry(chr_id);
            Loc loc;
            loc.chr_index = chr_entry.chr_index;
            loc.start = 0;
            loc.end = chr_entry.chr_size;
            locs.push_back(loc);
        }

        int32_t zoom_index = zoom <= 0 ? -1 : zoom - 1;
        uint64_t tree_offset = (zoom_index < 0) ?
            main_header.full_index_offset + 48 : 
            zoom_headers[zoom_index].index_offset + 48;
        TreeNodeGenerator generator(*file, locs, tree_offset);

        auto output_file = open_file(output_path, "w");
        auto write_header_line = [&](std::string chr_id, uint32_t start, int64_t span) {
            std::string line =
                "fixedStep chrom=" + chr_id +
                " start=" + std::to_string(start + 1) +
                " step=" + std::to_string(span) +
                " span=" + std::to_string(span) + "\n";
            output_file->write_string(line);
        };
        
        TreeNodeGeneratorNext result;
        while (!(result = generator.next()).done) {
            DataTreeLeaf node = result.node;
            ByteArray buffer = file->read(node.data_size, node.data_offset).get();
            if (main_header.uncompress_buffer_size > 0) buffer = buffer.decompress(main_header.uncompress_buffer_size);
            int64_t span = -1;

            DataIntervalGenerator data_intervals(node, buffer, zoom_index >= 0);
            DataIntervalGeneratorNext data_interval;
            while (!(data_interval = data_intervals.next()).done) {
                DataInterval interval = data_interval.data;
                std::string chr_id = chr_tree[interval.chr_index].key;
                if (interval.end - interval.start != span) {
                    span = interval.end - interval.start;
                    write_header_line(chr_id, interval.start, span);
                }
                output_file->write_string(std::to_string(interval.value) + "\n");
            }
        }
    }


};
