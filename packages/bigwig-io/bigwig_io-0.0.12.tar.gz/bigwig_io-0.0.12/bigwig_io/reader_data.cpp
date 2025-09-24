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

#include "structs.hpp"
#include "byte_util.cpp"
#include "file_util.cpp"
#include "util.cpp"
#include "reader_header.cpp"


WigDataHeader read_wig_data_header(const ByteArray& buffer) {
    WigDataHeader header;
    header.chr_index = buffer.read_uint32(0);
    header.chr_start = buffer.read_uint32(4);
    header.chr_end = buffer.read_uint32(8);
    header.item_step = buffer.read_uint32(12);
    header.item_span = buffer.read_uint32(16);
    header.type = buffer.read_uint8(20);
    header.reserved = buffer.read_uint8(21);
    header.item_count = buffer.read_uint16(22);
    return header;
}


ZoomDataRecord read_zoom_data_record(const ByteArray& buffer, uint64_t index) {
    uint64_t offset = index * 32;
    ZoomDataRecord record;
    record.chr_index = buffer.read_uint32(offset);
    record.chr_start = buffer.read_uint32(offset + 4);
    record.chr_end = buffer.read_uint32(offset + 8);
    record.valid_count = buffer.read_uint32(offset + 12);
    record.min_value = buffer.read_float(offset + 16);
    record.max_value = buffer.read_float(offset + 20);
    record.sum_data = buffer.read_float(offset + 24);
    record.sum_squared = buffer.read_float(offset + 28);
    return record;
}


struct DataIntervalGeneratorNext {
    DataInterval data;
    bool done;
};

class DataIntervalGenerator {
    const DataTreeLeaf& node;
    const ByteArray& buffer;
    bool is_zoom;
    WigDataHeader header;
    uint64_t count;
    uint16_t index = 0;

public:
    DataIntervalGenerator(const DataTreeLeaf& node, const ByteArray& buffer, bool is_zoom = false) : node(node), buffer(buffer), is_zoom(is_zoom) {
        if (is_zoom) {
            count = node.data_size / 32;
        } else {
            header = read_wig_data_header(buffer);
            count = header.item_count;
        }
    }
    
    DataIntervalGeneratorNext next() {
        while (index < count) {
            DataInterval data;
            if (is_zoom) { // zoom record
                ZoomDataRecord record = read_zoom_data_record(buffer, index);
                if (record.valid_count == 0) {
                    index += 1;
                    continue;
                }
                data.chr_index = record.chr_index;
                data.start = record.chr_start;
                data.end = record.chr_end;
                data.value = record.sum_data / record.valid_count;
            } else if (header.type == 1) { // bedgraph
                data.chr_index = header.chr_index;
                data.start = buffer.read_uint32(24 + index * 12);
                data.end = buffer.read_uint32(24 + index * 12 + 4);
                data.value = buffer.read_float(24 + index * 12 + 8);
            } else if (header.type == 2) { // variable step wig
                data.chr_index = header.chr_index;
                data.start = buffer.read_uint32(24 + index * 8);
                data.end = data.start + header.item_span;
                data.value = buffer.read_float(24 + index * 8 + 4);
            } else if (header.type == 3) { // fixed step wig
                data.chr_index = header.chr_index;
                data.start = header.chr_start + index * header.item_step;
                data.end = data.start + header.item_span;
                data.value = buffer.read_float(24 + index * 4);
            } else {
                throw std::runtime_error(fstring("wig data type {} invalid", header.type));
            }
            index += 1;
            return {data, false};
        }
        return {DataInterval{}, true};
    }
};



class LocsLockManager {
private:
    std::vector<std::unique_ptr<std::mutex>> mutexes;

public:
    explicit LocsLockManager(size_t locs_count) {
        mutexes.reserve(locs_count);
        for (size_t i = 0; i < locs_count; ++i) {
            mutexes.push_back(std::make_unique<std::mutex>());
        }
    }

    std::vector<std::unique_lock<std::mutex>> lock_range(uint32_t start_loc_index, uint32_t end_loc_index) {
        std::vector<std::unique_lock<std::mutex>> locks;
        locks.reserve(end_loc_index - start_loc_index + 1);
        for (uint32_t i = start_loc_index; i <= end_loc_index; ++i) {
            if (i < mutexes.size()) {
                locks.emplace_back(*mutexes[i]);
            }
        }
        return locks;
    }
};


bool fill_values_with_value(
    const std::vector<Loc>& locs,
    std::vector<float>& values,
    uint64_t start_loc_index,
    uint64_t end_loc_index,
    uint32_t bin_size,
    uint32_t start, uint32_t end, float value) {

    bool no_more_overlap = true;
    for (uint64_t loc_index = start_loc_index; loc_index < end_loc_index; ++loc_index) {
        const Loc& loc = locs[loc_index];
        if (start >= loc.end) continue;
        no_more_overlap = false;
        if (end <= loc.start) break;
        uint32_t overlap_start = std::max(start, loc.start);
        uint32_t overlap_end = std::min(end, loc.end);
        uint32_t loc_bin_start = loc.start / bin_size;
        uint32_t bin_start = overlap_start / bin_size;
        uint32_t bin_end = (overlap_end - 1) / bin_size + 1;
        for (uint32_t b = bin_start; b < bin_end; b += 1) {
            uint64_t value_index = loc.values_index + (b - loc_bin_start);
            values[value_index] = value;
        }
    }
    return no_more_overlap;
}


bool fill_values_stats_with_value(
    const std::vector<Loc>& locs,
    std::vector<ValueStats>& values,
    uint64_t start_loc_index,
    uint64_t end_loc_index,
    uint32_t bin_size,
    uint32_t start, uint32_t end, float value) {

    bool no_more_overlap = true;
    for (uint64_t loc_index = start_loc_index; loc_index < end_loc_index; ++loc_index) {
        const Loc& loc = locs[loc_index];
        if (start >= loc.end) continue;
        no_more_overlap = false;
        if (end <= loc.start) break;
        uint32_t overlap_start = std::max(start, loc.start);
        uint32_t overlap_end = std::min(end, loc.end);
        uint32_t loc_bin_start = loc.start / bin_size;
        uint32_t bin_start = overlap_start / bin_size;
        uint32_t bin_end = (overlap_end - 1) / bin_size + 1;
        for (uint32_t b = bin_start; b < bin_end; b += 1) {
            uint64_t value_index = loc.values_index + (b - loc_bin_start);
            ValueStats& stats = values[value_index];
            stats.sum += value;
            stats.count += 1;
        }
    }
    return no_more_overlap;
}


bool fill_stats_with_value(
    const std::vector<Loc>& locs,
    std::vector<ExtendedValueStats>& values,
    uint64_t start_loc_index,
    uint64_t end_loc_index,
    uint32_t start, uint32_t end, float value) {

    bool no_more_overlap = true;
    for (uint64_t loc_index = start_loc_index; loc_index < end_loc_index; ++loc_index) {
        const Loc& loc = locs[loc_index];
        if (start >= loc.end) continue;
        no_more_overlap = false;
        if (end <= loc.start) break;
        uint32_t overlap_start = std::max(start, loc.start);
        uint32_t overlap_end = std::min(end, loc.end);
        uint32_t overlap = overlap_end - overlap_start;
        ExtendedValueStats& stats = values[loc_index];
        if (value < stats.min || std::isnan(stats.min)) stats.min = value;
        if (value > stats.max || std::isnan(stats.max)) stats.max = value;
        stats.sum += value * overlap;
        stats.sum_squared += value * value * overlap;
        stats.count += overlap;
    }
    return no_more_overlap;
}


void fill_values_at_locs(
    const ByteArray& buffer,
    const std::vector<Loc>& locs,
    bool is_zoom,
    const DataTreeLeaf& node,
    uint64_t start_loc_index,
    uint64_t end_loc_index,
    uint32_t bin_size,
    std::vector<float>& values) {
    
    DataIntervalGenerator data_intervals(node, buffer, is_zoom);
    DataIntervalGeneratorNext data_interval;
    while (!(data_interval = data_intervals.next()).done) {
        auto no_more_overlap = fill_values_with_value(
            locs, values, start_loc_index, end_loc_index, bin_size,
            data_interval.data.start, data_interval.data.end, data_interval.data.value
        );
        if (no_more_overlap) break;
    }
}


void fill_values_stats_at_locs(
    const ByteArray& buffer,
    const std::vector<Loc>& locs,
    bool is_zoom,
    const DataTreeLeaf& node,
    uint64_t start_loc_index,
    uint64_t end_loc_index,
    uint32_t bin_size,
    std::vector<ValueStats>& values) {

    DataIntervalGenerator data_intervals(node, buffer, is_zoom);
    DataIntervalGeneratorNext data_interval;
    while (!(data_interval = data_intervals.next()).done) {
        auto no_more_overlap = fill_values_stats_with_value(
            locs, values, start_loc_index, end_loc_index, bin_size,
            data_interval.data.start, data_interval.data.end, data_interval.data.value
        );
        if (no_more_overlap) break;
    }
}


void fill_stats_at_locs(
    const ByteArray& buffer,
    const std::vector<Loc>& locs,
    bool is_zoom,
    const DataTreeLeaf& node,
    uint64_t start_loc_index,
    uint64_t end_loc_index,
    std::vector<ExtendedValueStats>& values) {

    DataIntervalGenerator data_intervals(node, buffer, is_zoom);
    DataIntervalGeneratorNext data_interval;
    while (!(data_interval = data_intervals.next()).done) {
        auto no_more_overlap = fill_stats_with_value(
            locs, values, start_loc_index, end_loc_index,
            data_interval.data.start, data_interval.data.end, data_interval.data.value
        );
        if (no_more_overlap) break;
    }
}


std::vector<float> read_values_at_locs(
    BufferedFilePool& file,
    uint32_t uncompress_buffer_size,
    const std::vector<Loc>& locs,
    TreeNodeGenerator& tree_nodes,
    uint32_t span,
    uint32_t bin_size,
    float def_value,
    int32_t zoom_index,
    ProgressTracker& tracker) {

    uint32_t bin_count = span / bin_size;
    std::vector<float> values(locs.size() * bin_count, def_value);

    std::deque<std::future<void>> futures;
    TreeNodeGeneratorNext result;
    while (!(result = tree_nodes.next()).done) {
        tracker.update(tree_nodes.coverage);
        auto future = std::async(std::launch::async, [&file, uncompress_buffer_size, &locs, result, bin_size, &values, zoom_index]() {
            auto buffer = file.read(result.node.data_size, result.node.data_offset).get();
            if (uncompress_buffer_size > 0) buffer = buffer.decompress(uncompress_buffer_size);
            fill_values_at_locs(
                buffer,
                locs,
                zoom_index >= 0,
                result.node,
                result.start_loc_index,
                result.end_loc_index,
                bin_size,
                values
            );
        });
        futures.push_back(std::move(future));
        while (!futures.empty()) {
            auto &future = futures.front();
            if (future.wait_for(std::chrono::seconds(0)) == std::future_status::ready) {
                future.get();
                futures.pop_front();
            } else {
                break;
            }
        }
    }
    for (auto& future : futures) future.get();
    tracker.done();

    return values;
}


std::vector<float> read_values_stats_at_locs(
    BufferedFilePool& file,
    uint32_t uncompress_buffer_size,
    const std::vector<Loc>& locs,
    TreeNodeGenerator& tree_nodes,
    uint32_t span,
    uint32_t bin_size,
    float def_value,
    int32_t zoom_index,
    ProgressTracker& tracker) {

    LocsLockManager lock_manager(locs.size());
    uint32_t bin_count = span / bin_size;
    std::vector<ValueStats> values_stats(locs.size() * bin_count);

    std::deque<std::future<void>> futures;
    TreeNodeGeneratorNext result;
    while (!(result = tree_nodes.next()).done) {
        tracker.update(tree_nodes.coverage);
        auto future = std::async(std::launch::async, [&file, uncompress_buffer_size, &locs, result, bin_size, &values_stats, zoom_index, &lock_manager]() {
            auto buffer = file.read(result.node.data_size, result.node.data_offset).get();
            if (uncompress_buffer_size > 0) buffer = buffer.decompress(uncompress_buffer_size);
            auto locks = lock_manager.lock_range(result.start_loc_index, result.end_loc_index);
            fill_values_stats_at_locs(
                buffer,
                locs,
                zoom_index >= 0,
                result.node,
                result.start_loc_index,
                result.end_loc_index,
                bin_size,
                values_stats
            );
        });
        futures.push_back(std::move(future));
        while (!futures.empty()) {
            auto &future = futures.front();
            if (future.wait_for(std::chrono::seconds(0)) == std::future_status::ready) {
                future.get();
                futures.pop_front();
            } else {
                break;
            }
        }
    }
    for (auto& future : futures) future.get();
    tracker.done();

    std::vector<float> values(locs.size() * bin_count, def_value);
    for (uint64_t i = 0; i < values_stats.size(); ++i) {
        if (values_stats[i].count > 0) {
            values[i] = values_stats[i].sum / values_stats[i].count;
        }
    }

    return values;
}


std::vector<float> read_stats_at_locs(
    BufferedFilePool& file,
    uint32_t uncompress_buffer_size,
    const std::vector<Loc>& locs,
    TreeNodeGenerator& tree_nodes,
    float def_value,
    std::string reduce,
    int32_t zoom_index,
    ProgressTracker& tracker) {

    LocsLockManager lock_manager(locs.size());
    std::vector<ExtendedValueStats> values_stats(locs.size());

    std::deque<std::future<void>> futures;
    TreeNodeGeneratorNext result;
    while (!(result = tree_nodes.next()).done) {
        tracker.update(tree_nodes.coverage);
        auto future = std::async(std::launch::async, [&file, uncompress_buffer_size, &locs, result, &values_stats, zoom_index, &lock_manager]() {
            auto buffer = file.read(result.node.data_size, result.node.data_offset).get();
            if (uncompress_buffer_size > 0) buffer = buffer.decompress(uncompress_buffer_size);
            auto locks = lock_manager.lock_range(result.start_loc_index, result.end_loc_index);
            fill_stats_at_locs(
                buffer,
                locs,
                zoom_index >= 0,
                result.node,
                result.start_loc_index,
                result.end_loc_index,
                values_stats
            );
        });
        futures.push_back(std::move(future));
        while (!futures.empty()) {
            auto &future = futures.front();
            if (future.wait_for(std::chrono::seconds(0)) == std::future_status::ready) {
                future.get();
                futures.pop_front();
            } else {
                break;
            }
        }
    }
    for (auto& future : futures) future.get();
    tracker.done();

    std::vector<float> values(locs.size(), def_value);
    for (uint64_t i = 0; i < values_stats.size(); ++i) {
        if (values_stats[i].count > 0) {
            if (reduce == "mean") {
                values[i] = values_stats[i].sum / values_stats[i].count;
            } else if (reduce == "std") {
                float mean = values_stats[i].sum / values_stats[i].count;
                float variance = (values_stats[i].sum_squared / values_stats[i].count) - (mean * mean);
                values[i] = std::sqrt(variance);
            } else if (reduce == "min") {
                values[i] = values_stats[i].min;
            } else if (reduce == "max") {
                values[i] = values_stats[i].max;
            } else {
                throw std::runtime_error("reduce " + reduce + " invalid");
            }
        }
    }

    return values;
}
