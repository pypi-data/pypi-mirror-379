#include "macros.hh"
#include "zarr.common.hh"

#include <blosc.h>

#include <regex>
#include <stdexcept>

namespace fs = std::filesystem;

std::string
zarr::trim(std::string_view s)
{
    if (s.empty()) {
        return {};
    }

    // trim left
    std::string trimmed(s);
    trimmed.erase(trimmed.begin(),
                  std::find_if(trimmed.begin(), trimmed.end(), [](char c) {
                      return !std::isspace(c);
                  }));

    // trim right
    trimmed.erase(std::find_if(trimmed.rbegin(),
                               trimmed.rend(),
                               [](char c) { return !std::isspace(c); })
                    .base(),
                  trimmed.end());

    return trimmed;
}

bool
zarr::is_empty_string(std::string_view s, std::string_view err_on_empty)
{
    auto trimmed = trim(s);
    if (trimmed.empty()) {
        LOG_ERROR(err_on_empty);
        return true;
    }
    return false;
}

size_t
zarr::bytes_of_type(ZarrDataType data_type)
{
    switch (data_type) {
        case ZarrDataType_int8:
        case ZarrDataType_uint8:
            return 1;
        case ZarrDataType_int16:
        case ZarrDataType_uint16:
            return 2;
        case ZarrDataType_int32:
        case ZarrDataType_uint32:
        case ZarrDataType_float32:
            return 4;
        case ZarrDataType_int64:
        case ZarrDataType_uint64:
        case ZarrDataType_float64:
            return 8;
        default:
            throw std::invalid_argument("Invalid data type: " +
                                        std::to_string(data_type));
    }
}

size_t
zarr::bytes_of_frame(const ArrayDimensions& dims, ZarrDataType type)
{
    const auto height = dims.height_dim().array_size_px;
    const auto width = dims.width_dim().array_size_px;
    return bytes_of_type(type) * height * width;
}

uint32_t
zarr::parts_along_dimension(uint32_t array_size, uint32_t part_size)
{
    EXPECT(part_size > 0, "Invalid part size.");

    return (array_size + part_size - 1) / part_size;
}

uint32_t
zarr::chunks_along_dimension(const ZarrDimension& dimension)
{
    return parts_along_dimension(dimension.array_size_px,
                                 dimension.chunk_size_px);
}

uint32_t
zarr::shards_along_dimension(const ZarrDimension& dimension)
{
    if (dimension.shard_size_chunks == 0) {
        return 0;
    }

    const auto shard_size = dimension.shard_size_chunks;
    const auto n_chunks = chunks_along_dimension(dimension);
    return (n_chunks + shard_size - 1) / shard_size;
}

bool
zarr::compress_in_place(ByteVector& data,
                        const zarr::BloscCompressionParams& params,
                        size_t type_size)
{
    if (data.empty()) {
        LOG_WARNING("Buffer is empty, not compressing.");
        return false;
    }

    std::vector<uint8_t> compressed_data(data.size() + BLOSC_MAX_OVERHEAD);
    const auto n_bytes_compressed = blosc_compress_ctx(params.clevel,
                                                       params.shuffle,
                                                       type_size,
                                                       data.size(),
                                                       data.data(),
                                                       compressed_data.data(),
                                                       compressed_data.size(),
                                                       params.codec_id.c_str(),
                                                       0,
                                                       1);

    if (n_bytes_compressed <= 0) {
        LOG_ERROR("blosc_compress_ctx failed with code ", n_bytes_compressed);
        return false;
    }

    compressed_data.resize(n_bytes_compressed);
    data.swap(compressed_data);

    return true;
}

std::string
zarr::regularize_key(const char* key)
{
    if (key == nullptr) {
        return "";
    }

    return regularize_key(std::string_view{ key });
}

std::string
zarr::regularize_key(const std::string_view key)
{
    std::string regularized_key{ key };

    // replace leading and trailing whitespace and/or slashes
    regularized_key = std::regex_replace(
      regularized_key, std::regex(R"(^(\s|\/)+|(\s|\/)+$)"), "");

    // replace multiple consecutive slashes with single slashes
    regularized_key =
      std::regex_replace(regularized_key, std::regex(R"(\/+)"), "/");

    return regularized_key;
}
