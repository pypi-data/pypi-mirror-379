#!/usr/bin/env python3
import time

import dotenv
import json
import logging
from pathlib import Path
import os
import shutil
from typing import Optional

import numpy as np
import pytest
import zarr
from numcodecs import blosc as ncblosc
from zarr.codecs import blosc as zblosc
import s3fs
import skimage  # noqa: F401

dotenv.load_dotenv()

from acquire_zarr import (
    ArraySettings,
    StreamSettings,
    ZarrStream,
    Compressor,
    CompressionCodec,
    CompressionSettings,
    S3Settings,
    Dimension,
    DimensionType,
    ZarrVersion,
    LogLevel,
    DownsamplingMethod,
    Plate,
    Well,
    FieldOfView,
    Acquisition,
    set_log_level,
    get_log_level,
)


@pytest.fixture(scope="function")
def settings():
    s = StreamSettings()
    s.custom_metadata = json.dumps({"foo": "bar"})
    s.arrays = [
        ArraySettings(
            dimensions=[
                Dimension(
                    name="t",
                    kind=DimensionType.TIME,
                    array_size_px=0,
                    chunk_size_px=32,
                    shard_size_chunks=1,
                ),
                Dimension(
                    name="y",
                    kind=DimensionType.SPACE,
                    array_size_px=48,
                    chunk_size_px=16,
                    shard_size_chunks=1,
                ),
                Dimension(
                    name="x",
                    kind=DimensionType.SPACE,
                    array_size_px=64,
                    chunk_size_px=32,
                    shard_size_chunks=1,
                ),
            ]
        )
    ]

    return s


@pytest.fixture(scope="module")
def s3_settings():
    if (
        "ZARR_S3_ENDPOINT" not in os.environ
        or "ZARR_S3_BUCKET_NAME" not in os.environ
        or "AWS_ACCESS_KEY_ID" not in os.environ
        or "AWS_SECRET_ACCESS_KEY" not in os.environ
    ):
        yield None
    else:
        settings = S3Settings(
            endpoint=os.environ["ZARR_S3_ENDPOINT"],
            bucket_name=os.environ["ZARR_S3_BUCKET_NAME"],
        )
        if "ZARR_S3_REGION" in os.environ:
            settings.region = os.environ["ZARR_S3_REGION"]

        yield settings


@pytest.fixture(scope="function")
def store_path(tmp_path):
    yield tmp_path
    shutil.rmtree(tmp_path)


def create_hcs_settings():
    """Create HCS settings that match the C++ test structure."""
    # Well C/5 with two FOVs
    c5_fov1_array = ArraySettings(
        output_key="fov1",  # Will be at test_plate/C/5/fov1
        data_type=np.uint8,
        dimensions=[
            Dimension(
                name="z",
                kind=DimensionType.SPACE,
                array_size_px=0,
                chunk_size_px=1,
                shard_size_chunks=1,
            ),
            Dimension(
                name="y",
                kind=DimensionType.SPACE,
                array_size_px=480,
                chunk_size_px=256,
                shard_size_chunks=4,
            ),
            Dimension(
                name="x",
                kind=DimensionType.SPACE,
                array_size_px=640,
                chunk_size_px=256,
                shard_size_chunks=4,
            ),
        ],
    )

    c5_fov2_array = ArraySettings(
        output_key="fov2",  # Will be at test_plate/C/5/fov2
        data_type=np.uint16,
        dimensions=[
            Dimension(
                name="z",
                kind=DimensionType.SPACE,
                array_size_px=0,
                chunk_size_px=1,
                shard_size_chunks=1,
            ),
            Dimension(
                name="y",
                kind=DimensionType.SPACE,
                array_size_px=480,
                chunk_size_px=256,
                shard_size_chunks=4,
            ),
            Dimension(
                name="x",
                kind=DimensionType.SPACE,
                array_size_px=640,
                chunk_size_px=256,
                shard_size_chunks=4,
            ),
        ],
    )

    c5_well = Well(
        row_name="C",
        column_name="5",
        images=[
            FieldOfView(
                path="fov1", acquisition_id=0, array_settings=c5_fov1_array
            ),
            FieldOfView(
                path="fov2", acquisition_id=1, array_settings=c5_fov2_array
            ),
        ],
    )

    # Well D/7 with one FOV
    d7_fov1_array = ArraySettings(
        output_key="fov1",  # Will be at test_plate/D/7/fov1
        data_type=np.uint16,
        dimensions=[
            Dimension(
                name="t",
                kind=DimensionType.TIME,
                array_size_px=10,
                chunk_size_px=1,
                shard_size_chunks=1,
            ),
            Dimension(
                name="c",
                kind=DimensionType.CHANNEL,
                array_size_px=3,
                chunk_size_px=1,
                shard_size_chunks=1,
            ),
            Dimension(
                name="z",
                kind=DimensionType.SPACE,
                array_size_px=5,
                chunk_size_px=1,
                shard_size_chunks=1,
            ),
            Dimension(
                name="y",
                kind=DimensionType.SPACE,
                array_size_px=512,
                chunk_size_px=256,
                shard_size_chunks=4,
            ),
            Dimension(
                name="x",
                kind=DimensionType.SPACE,
                array_size_px=512,
                chunk_size_px=256,
                shard_size_chunks=4,
            ),
        ],
    )

    d7_well = Well(
        row_name="D",
        column_name="7",
        images=[
            FieldOfView(
                path="fov1", acquisition_id=0, array_settings=d7_fov1_array
            ),
        ],
    )

    # Create plate with acquisitions
    acquisitions = [
        Acquisition(
            id=0,
            name="Meas_01(2012-07-31_10-41-12)",
            start_time=1343731272000,
        ),
        Acquisition(
            id=1,
            name="Meas_02(2012-07-31_10-45-12)",
            start_time=1343735801000,
            end_time=1343737645000,
        ),
    ]

    plate = Plate(
        path="test_plate",
        name="Test Plate",
        row_names=["A", "B", "C", "D", "E", "F", "G", "H"],
        column_names=[
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
        ],
        wells=[c5_well, d7_well],
        acquisitions=acquisitions,
    )

    return plate


def validate_v2_metadata(store_path: Path):
    assert (store_path / ".zattrs").is_file()
    with open(store_path / ".zattrs", "r") as fh:
        data = json.load(fh)
        axes = data["multiscales"][0]["axes"]
        assert axes[0]["name"] == "t"
        assert axes[0]["type"] == "time"

        assert axes[1]["name"] == "y"
        assert axes[1]["type"] == "space"

        assert axes[2]["name"] == "x"
        assert axes[2]["type"] == "space"

    assert (store_path / ".zgroup").is_file()
    with open(store_path / ".zgroup", "r") as fh:
        data = json.load(fh)
        assert data["zarr_format"] == 2

    assert not (store_path / "acquire.json").is_file()


def validate_v3_metadata(store_path: Path):
    assert (store_path / "zarr.json").is_file()
    with open(store_path / "zarr.json", "r") as fh:
        data = json.load(fh)
        assert data["zarr_format"] == 3
        assert data["node_type"] == "group"
        assert data["consolidated_metadata"] is None

        axes = data["attributes"]["ome"]["multiscales"][0]["axes"]
        assert axes[0]["name"] == "t"
        assert axes[0]["type"] == "time"

        assert axes[1]["name"] == "y"
        assert axes[1]["type"] == "space"

        assert axes[2]["name"] == "x"
        assert axes[2]["type"] == "space"

    assert not (store_path / "acquire.json").is_file()


@pytest.mark.parametrize(
    ("version",),
    [
        (ZarrVersion.V2,),
        (ZarrVersion.V3,),
    ],
)
def test_create_stream(
    settings: StreamSettings,
    store_path: Path,
    request: pytest.FixtureRequest,
    version: ZarrVersion,
):
    settings.store_path = str(store_path / f"{request.node.name}.zarr")
    settings.version = version
    stream = ZarrStream(settings)
    assert stream

    store_path = Path(settings.store_path)

    stream.close()  # close the stream, flush the files

    # check that the stream created the zarr store
    assert store_path.is_dir()

    if version == ZarrVersion.V2:
        validate_v2_metadata(store_path)

        # no data written, so no array metadata
        assert not (store_path / "0" / ".zarray").exists()
    else:
        validate_v3_metadata(store_path)

        # no data written, so no array metadata
        assert not (store_path / "meta" / "0.array.json").exists()


@pytest.mark.parametrize(
    (
        "version",
        "compression_codec",
    ),
    [
        (
            ZarrVersion.V2,
            None,
        ),
        (
            ZarrVersion.V2,
            CompressionCodec.BLOSC_LZ4,
        ),
        (
            ZarrVersion.V2,
            CompressionCodec.BLOSC_ZSTD,
        ),
        (
            ZarrVersion.V3,
            None,
        ),
        (
            ZarrVersion.V3,
            CompressionCodec.BLOSC_LZ4,
        ),
        (
            ZarrVersion.V3,
            CompressionCodec.BLOSC_ZSTD,
        ),
    ],
)
def test_stream_data_to_filesystem(
    settings: StreamSettings,
    store_path: Path,
    version: ZarrVersion,
    compression_codec: Optional[CompressionCodec],
):
    settings.store_path = str(store_path / "test.zarr")
    settings.version = version
    if compression_codec is not None:
        settings.arrays[0].compression = CompressionSettings(
            compressor=Compressor.BLOSC1,
            codec=compression_codec,
            level=1,
            shuffle=1,
        )
    settings.arrays[0].data_type = np.uint16

    stream = ZarrStream(settings)
    assert stream

    data = np.zeros(
        (
            2 * settings.arrays[0].dimensions[0].chunk_size_px,
            settings.arrays[0].dimensions[1].array_size_px,
            settings.arrays[0].dimensions[2].array_size_px,
        ),
        dtype=np.uint16,
    )
    for i in range(data.shape[0]):
        data[i, :, :] = i

    stream.append(data)

    stream.close()  # close the stream, flush the files

    chunk_size_bytes = data.dtype.itemsize
    for dim in settings.arrays[0].dimensions:
        chunk_size_bytes *= dim.chunk_size_px

    shard_size_bytes = chunk_size_bytes
    table_size_bytes = 16  # 2 * sizeof(uint64_t)
    if version == ZarrVersion.V3:
        for dim in settings.arrays[0].dimensions:
            shard_size_bytes *= dim.shard_size_chunks
            table_size_bytes *= dim.shard_size_chunks
    shard_size_bytes = (
        shard_size_bytes + table_size_bytes + 4
    )  # 4 bytes for crc32c checksum

    group = zarr.open(settings.store_path, mode="r")
    array = group["0"]

    assert array.shape == data.shape
    for i in range(array.shape[0]):
        assert np.array_equal(array[i, :, :], data[i, :, :])

    metadata = array.metadata
    if compression_codec is not None:
        if version == ZarrVersion.V2:
            cname = (
                "lz4"
                if compression_codec == CompressionCodec.BLOSC_LZ4
                else "zstd"
            )
            compressor = metadata.compressor
            assert compressor.cname == cname
            assert compressor.clevel == 1
            assert compressor.shuffle == ncblosc.SHUFFLE

            # check that the data is compressed
            assert (store_path / "test.zarr" / "0" / "0" / "0" / "0").is_file()
            assert (
                store_path / "test.zarr" / "0" / "0" / "0" / "0"
            ).stat().st_size <= chunk_size_bytes
        else:
            cname = (
                zblosc.BloscCname.lz4
                if compression_codec == CompressionCodec.BLOSC_LZ4
                else zblosc.BloscCname.zstd
            )
            blosc_codec = metadata.codecs[0].codecs[1]
            assert blosc_codec.cname == cname
            assert blosc_codec.clevel == 1
            assert blosc_codec.shuffle == zblosc.BloscShuffle.shuffle

            assert (
                store_path / "test.zarr" / "0" / "c" / "0" / "0" / "0"
            ).is_file()
            assert (
                store_path / "test.zarr" / "0" / "c" / "0" / "0" / "0"
            ).stat().st_size <= shard_size_bytes
    else:
        if version == ZarrVersion.V2:
            assert metadata.compressor is None

            assert (store_path / "test.zarr" / "0" / "0" / "0" / "0").is_file()
            assert (
                store_path / "test.zarr" / "0" / "0" / "0" / "0"
            ).stat().st_size == chunk_size_bytes
        else:
            assert len(metadata.codecs[0].codecs) == 1

            assert (
                store_path / "test.zarr" / "0" / "c" / "0" / "0" / "0"
            ).is_file()
            assert (
                store_path / "test.zarr" / "0" / "c" / "0" / "0" / "0"
            ).stat().st_size == shard_size_bytes


@pytest.mark.parametrize(
    (
        "version",
        "compression_codec",
    ),
    [
        (
            ZarrVersion.V2,
            None,
        ),
        (
            ZarrVersion.V2,
            CompressionCodec.BLOSC_LZ4,
        ),
        (
            ZarrVersion.V2,
            CompressionCodec.BLOSC_ZSTD,
        ),
        (
            ZarrVersion.V3,
            None,
        ),
        (
            ZarrVersion.V3,
            CompressionCodec.BLOSC_LZ4,
        ),
        (
            ZarrVersion.V3,
            CompressionCodec.BLOSC_ZSTD,
        ),
    ],
)
def test_stream_data_to_s3(
    settings: StreamSettings,
    s3_settings: Optional[S3Settings],
    request: pytest.FixtureRequest,
    version: ZarrVersion,
    compression_codec: Optional[CompressionCodec],
):
    if s3_settings is None:
        pytest.skip("S3 settings not set")

    settings.store_path = f"{request.node.name}.zarr".replace("[", "").replace(
        "]", ""
    )
    settings.version = version
    settings.s3 = s3_settings
    settings.data_type = np.uint16
    if compression_codec is not None:
        settings.compression = CompressionSettings(
            compressor=Compressor.BLOSC1,
            codec=compression_codec,
            level=1,
            shuffle=1,
        )

    stream = ZarrStream(settings)
    assert stream

    data = np.random.randint(
        0,
        65535,
        (
            2 * settings.arrays[0].dimensions[0].chunk_size_px,
            settings.arrays[0].dimensions[1].array_size_px,
            settings.arrays[0].dimensions[2].array_size_px,
        ),
        dtype=np.uint16,
    )
    stream.append(data)

    stream.close()  # close the stream, flush the data

    store = zarr.storage.FsspecStore.from_url(
        f"s3://{settings.s3.bucket_name}/{settings.store_path}",
        storage_options={
            "key": os.environ.get("AWS_ACCESS_KEY_ID"),
            "secret": os.environ.get("AWS_SECRET_ACCESS_KEY"),
            "client_kwargs": {"endpoint_url": s3_settings.endpoint},
        },
    )
    group = zarr.group(store=store)
    array = group["0"]

    assert array.shape == data.shape
    for i in range(array.shape[0]):
        assert np.array_equal(array[i, :, :], data[i, :, :])

    metadata = array.metadata
    if compression_codec is not None:
        if version == ZarrVersion.V2:
            cname = (
                "lz4"
                if compression_codec == CompressionCodec.BLOSC_LZ4
                else "zstd"
            )
            compressor = metadata.compressor
            assert compressor.cname == cname
            assert compressor.clevel == 1
            assert compressor.shuffle == ncblosc.SHUFFLE
        else:
            cname = (
                zblosc.BloscCname.lz4
                if compression_codec == CompressionCodec.BLOSC_LZ4
                else zblosc.BloscCname.zstd
            )
            blosc_codec = metadata.codecs[0].codecs[1]
            assert blosc_codec.cname == cname
            assert blosc_codec.clevel == 1
            assert blosc_codec.shuffle == zblosc.BloscShuffle.shuffle
    else:
        if version == ZarrVersion.V2:
            assert metadata.compressor is None
        else:
            assert len(metadata.codecs[0].codecs) == 1

    # cleanup
    s3 = s3fs.S3FileSystem(
        key=os.environ.get("AWS_ACCESS_KEY_ID"),
        secret=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        client_kwargs={"endpoint_url": settings.s3.endpoint},
    )
    s3.rm(f"{settings.s3.bucket_name}/{settings.store_path}", recursive=True)


@pytest.mark.parametrize(
    ("level",),
    [
        (LogLevel.DEBUG,),
        (LogLevel.INFO,),
        (LogLevel.WARNING,),
        (LogLevel.ERROR,),
        (LogLevel.NONE,),
    ],
)
def test_set_log_level(level: LogLevel):
    set_log_level(level)
    assert get_log_level() == level


@pytest.mark.parametrize(
    ("version", "overwrite"),
    [
        (ZarrVersion.V2, False),
        (ZarrVersion.V2, True),
        (ZarrVersion.V3, False),
        (ZarrVersion.V3, True),
    ],
)
def test_write_custom_metadata(
    settings: StreamSettings,
    store_path: Path,
    request: pytest.FixtureRequest,
    version: ZarrVersion,
    overwrite: bool,
):
    settings.store_path = str(store_path / f"{request.node.name}.zarr")
    settings.version = version
    stream = ZarrStream(settings)
    assert stream

    metadata = json.dumps({"foo": "bar"})
    assert stream.write_custom_metadata(metadata, True)

    # don't allow overwriting the metadata
    metadata = json.dumps({"baz": "qux"})
    overwrite_result = stream.write_custom_metadata(
        metadata, overwrite=overwrite
    )
    assert overwrite_result == overwrite

    stream.close()

    assert (Path(settings.store_path) / "acquire.json").is_file()
    with open(Path(settings.store_path) / "acquire.json", "r") as fh:
        data = json.load(fh)

    if overwrite:  # the metadata is overwritten
        assert data["baz"] == "qux"
        assert "foo" not in data
    else:  # the originally written metadata is preserved
        assert data["foo"] == "bar"
        assert "baz" not in data


def test_write_transposed_array(
    store_path: Path,
):
    settings = StreamSettings(
        arrays=[
            ArraySettings(
                dimensions=[
                    Dimension(
                        name="t",
                        kind=DimensionType.TIME,
                        array_size_px=2,
                        chunk_size_px=2,
                        shard_size_chunks=1,
                    ),
                    Dimension(
                        name="c",
                        kind=DimensionType.CHANNEL,
                        array_size_px=1,
                        chunk_size_px=1,
                        shard_size_chunks=1,
                    ),
                    Dimension(
                        name="z",
                        kind=DimensionType.SPACE,
                        array_size_px=40,
                        chunk_size_px=20,
                        shard_size_chunks=1,
                    ),
                    Dimension(
                        name="y",
                        kind=DimensionType.SPACE,
                        array_size_px=30,
                        chunk_size_px=15,
                        shard_size_chunks=1,
                    ),
                    Dimension(
                        name="x",
                        kind=DimensionType.SPACE,
                        array_size_px=20,
                        chunk_size_px=10,
                        shard_size_chunks=1,
                    ),
                ],
                data_type=np.int32,
            )
        ]
    )
    settings.store_path = str(store_path / "test.zarr")
    settings.version = ZarrVersion.V3

    data = np.random.randint(
        -(2**16),
        2**16 - 1,
        (
            settings.arrays[0].dimensions[0].chunk_size_px,
            settings.arrays[0].dimensions[1].array_size_px,
            settings.arrays[0].dimensions[2].array_size_px,
            settings.arrays[0].dimensions[4].array_size_px,
            settings.arrays[0].dimensions[3].array_size_px,
        ),
        dtype=np.int32,
    )
    data = np.transpose(data, (0, 1, 2, 4, 3))

    stream = ZarrStream(settings)
    assert stream

    stream.append(data)

    stream.close()  # close the stream, flush the files

    group = zarr.open(settings.store_path, mode="r")
    array = group["0"]

    assert data.shape == array.shape
    np.testing.assert_array_equal(data, array)


def test_column_ragged_sharding(
    store_path: Path,
):
    settings = StreamSettings(
        arrays=[
            ArraySettings(
                dimensions=[
                    Dimension(
                        name="z",
                        kind=DimensionType.SPACE,
                        array_size_px=2,
                        chunk_size_px=1,
                        shard_size_chunks=2,
                    ),
                    Dimension(
                        name="y",
                        kind=DimensionType.SPACE,
                        array_size_px=1080,
                        chunk_size_px=64,
                        shard_size_chunks=2,
                    ),
                    Dimension(
                        name="x",
                        kind=DimensionType.SPACE,
                        array_size_px=1080,
                        chunk_size_px=64,
                        shard_size_chunks=2,
                    ),
                ],
                data_type=np.int32,
            )
        ]
    )
    settings.store_path = str(store_path / "test.zarr")
    settings.version = ZarrVersion.V3

    data = np.random.randint(
        -(2**16),
        2**16 - 1,
        (
            settings.arrays[0].dimensions[0].array_size_px,
            settings.arrays[0].dimensions[1].array_size_px,
            settings.arrays[0].dimensions[2].array_size_px,
        ),
        dtype=np.int32,
    )

    stream = ZarrStream(settings)
    assert stream

    stream.append(data)

    stream.close()  # close the stream, flush the files

    array = zarr.open(settings.store_path, mode="r")["0"]

    assert data.shape == array.shape
    np.testing.assert_array_equal(data, array)


def test_custom_dimension_units_and_scales(store_path: Path):
    settings = StreamSettings(
        arrays=[
            ArraySettings(
                dimensions=[
                    Dimension(
                        name="z",
                        kind=DimensionType.SPACE,
                        unit="micron",
                        scale=0.1,
                        array_size_px=2,
                        chunk_size_px=1,
                        shard_size_chunks=2,
                    ),
                    Dimension(
                        name="y",
                        kind=DimensionType.SPACE,
                        unit="micrometer",
                        scale=0.9,
                        array_size_px=1080,
                        chunk_size_px=64,
                        shard_size_chunks=2,
                    ),
                    Dimension(
                        name="x",
                        kind=DimensionType.SPACE,
                        unit="nanometer",
                        scale=1.1,
                        array_size_px=1080,
                        chunk_size_px=64,
                        shard_size_chunks=2,
                    ),
                ],
                data_type=np.int32,
            )
        ]
    )
    settings.store_path = str(store_path / "test.zarr")
    settings.version = ZarrVersion.V3

    data = np.random.randint(
        -(2**16),
        2**16 - 1,
        (
            settings.arrays[0].dimensions[0].array_size_px,
            settings.arrays[0].dimensions[1].array_size_px,
            settings.arrays[0].dimensions[2].array_size_px,
        ),
        dtype=np.int32,
    )

    stream = ZarrStream(settings)
    assert stream

    stream.append(data)

    stream.close()  # close the stream, flush the files

    group = zarr.open(settings.store_path, mode="r")
    array = group["0"]

    assert data.shape == array.shape
    np.testing.assert_array_equal(data, array)

    # Check custom units and scales
    multiscale = group.attrs["ome"]["multiscales"][0]
    axes = multiscale["axes"]
    assert len(axes) == 3
    z, y, x = axes

    assert z["name"] == "z"
    assert z["type"] == "space"
    assert z["unit"] == "micron"

    assert y["name"] == "y"
    assert y["type"] == "space"
    assert y["unit"] == "micrometer"

    assert x["name"] == "x"
    assert x["type"] == "space"
    assert x["unit"] == "nanometer"

    z_scale, y_scale, x_scale = multiscale["datasets"][0][
        "coordinateTransformations"
    ][0]["scale"]

    assert z_scale == 0.1
    assert y_scale == 0.9
    assert x_scale == 1.1


@pytest.mark.parametrize(
    ("method",),
    [
        (DownsamplingMethod.DECIMATE,),
        (DownsamplingMethod.MEAN,),
        (DownsamplingMethod.MIN,),
        (DownsamplingMethod.MAX,),
    ],
)
def test_2d_multiscale_stream(store_path: Path, method: DownsamplingMethod):
    settings = StreamSettings(
        arrays=[
            ArraySettings(
                dimensions=[
                    Dimension(
                        name="t",
                        kind=DimensionType.TIME,
                        array_size_px=50,
                        chunk_size_px=50,
                        shard_size_chunks=1,
                    ),
                    Dimension(
                        name="y",
                        kind=DimensionType.SPACE,
                        array_size_px=48,
                        chunk_size_px=24,
                        shard_size_chunks=1,
                    ),
                    Dimension(
                        name="x",
                        kind=DimensionType.SPACE,
                        array_size_px=64,
                        chunk_size_px=32,
                        shard_size_chunks=1,
                    ),
                ],
                data_type=np.int32,
                downsampling_method=method,
            )
        ]
    )
    settings.store_path = str(store_path / "test.zarr")
    settings.version = ZarrVersion.V3

    data = np.random.randint(
        -(2**16),
        2**16 - 1,
        (
            settings.arrays[0].dimensions[0].array_size_px,
            settings.arrays[0].dimensions[1].array_size_px,
            settings.arrays[0].dimensions[2].array_size_px,
        ),
        dtype=np.int32,
    )

    stream = ZarrStream(settings)
    assert stream

    stream.append(data)

    stream.close()

    group = zarr.open(settings.store_path, mode="r")
    metadata = group.attrs["ome"]["multiscales"][0]["metadata"]
    saved_method = metadata["method"]
    args = list(map(eval, metadata.get("args", [])))
    kwargs = {k: eval(v) for k, v in metadata.get("kwargs", {}).items()}

    assert "0" in group

    full_res = group["0"]
    assert data.shape == full_res.shape
    np.testing.assert_array_equal(data, full_res)

    assert "1" in group
    downsampled = group["1"]
    assert downsampled.shape == (50, 24, 32)

    for i in range(downsampled.shape[0]):
        actual = downsampled[i, :, :]
        expected = eval(saved_method)(full_res[i], *args, **kwargs).astype(
            data.dtype
        )

        # Check the downsampling method and arguments
        np.testing.assert_array_equal(actual, expected)


@pytest.mark.parametrize(
    ("method",),
    [
        (DownsamplingMethod.DECIMATE,),
        (DownsamplingMethod.MEAN,),
        (DownsamplingMethod.MIN,),
        (DownsamplingMethod.MAX,),
    ],
)
def test_3d_multiscale_stream(store_path: Path, method: DownsamplingMethod):
    settings = StreamSettings(
        arrays=[
            ArraySettings(
                dimensions=[
                    Dimension(
                        name="z",
                        kind=DimensionType.SPACE,
                        array_size_px=100,
                        chunk_size_px=50,
                        shard_size_chunks=1,
                    ),
                    Dimension(
                        name="y",
                        kind=DimensionType.SPACE,
                        array_size_px=48,
                        chunk_size_px=24,
                        shard_size_chunks=1,
                    ),
                    Dimension(
                        name="x",
                        kind=DimensionType.SPACE,
                        array_size_px=64,
                        chunk_size_px=32,
                        shard_size_chunks=1,
                    ),
                ],
                data_type=np.uint16,
                downsampling_method=method,
            )
        ]
    )
    settings.store_path = str(store_path / "test.zarr")
    settings.version = ZarrVersion.V3

    data = np.random.randint(
        0,
        2**16 - 1,
        (
            settings.arrays[0].dimensions[0].array_size_px,
            settings.arrays[0].dimensions[1].array_size_px,
            settings.arrays[0].dimensions[2].array_size_px,
        ),
        dtype=np.uint16,
    )

    stream = ZarrStream(settings)
    assert stream

    stream.append(data)

    stream.close()

    group = zarr.open(settings.store_path, mode="r")
    metadata = group.attrs["ome"]["multiscales"][0]["metadata"]
    saved_method = metadata["method"]
    args = list(map(eval, metadata.get("args", [])))
    kwargs = {k: eval(v) for k, v in metadata.get("kwargs", {}).items()}

    assert "0" in group

    full_res = group["0"]
    assert data.shape == full_res.shape
    np.testing.assert_array_equal(data, full_res)

    assert "1" in group
    downsampled = group["1"]
    assert downsampled.shape == (50, 24, 32)

    for i in range(downsampled.shape[0]):
        actual = downsampled[i, :, :]

        if method == DownsamplingMethod.MEAN:
            expected1 = eval(saved_method)(full_res[2 * i], *args, **kwargs)
            expected2 = eval(saved_method)(
                full_res[2 * i + 1], *args, **kwargs
            )
            expected = ((expected1 + expected2) / 2).astype(data.dtype)
            np.testing.assert_allclose(
                expected, actual, atol=1
            )  # we may round slightly differently than skimage
            continue

        if method == DownsamplingMethod.DECIMATE:
            expected = eval(saved_method)(
                full_res[2 * i], *args, **kwargs
            ).astype(data.dtype)
        else:
            expected1 = eval(saved_method)(
                full_res[2 * i], *args, **kwargs
            ).astype(data.dtype)
            expected2 = eval(saved_method)(
                full_res[2 * i + 1], *args, **kwargs
            ).astype(data.dtype)

            if method == DownsamplingMethod.MIN:
                expected = np.minimum(expected1, expected2)
            elif method == DownsamplingMethod.MAX:
                expected = np.maximum(expected1, expected2)
            else:
                raise ValueError(f"Unknown downsampling method: {method}")

        np.testing.assert_array_equal(actual, expected)


@pytest.mark.parametrize(
    ("output_key", "downsampling_method"),
    [
        ("labels", None),
        ("path/to/data", None),
        ("a/nested/multiscale/group", DownsamplingMethod.MEAN),
    ],
)
def test_stream_data_to_named_array(
    settings: StreamSettings,
    store_path: Path,
    output_key: str,
    downsampling_method: DownsamplingMethod,
):
    settings.store_path = str(
        store_path
        / f"stream_to_named_array_{output_key.replace('/', '_')}.zarr"
    )
    settings.version = ZarrVersion.V3
    settings.arrays[0].output_key = output_key
    settings.arrays[0].downsampling_method = downsampling_method
    settings.arrays[0].data_type = np.uint16

    stream = ZarrStream(settings)
    assert stream

    # Create test data
    data = np.zeros(
        (
            2 * settings.arrays[0].dimensions[0].chunk_size_px,
            settings.arrays[0].dimensions[1].array_size_px,
            settings.arrays[0].dimensions[2].array_size_px,
        ),
        dtype=np.uint16,
    )
    # Fill with recognizable pattern
    for i in range(data.shape[0]):
        data[i, :, :] = i + 1

    stream.append(data)

    stream.close()  # close the stream, flush the files

    # Now verify the data is stored in the expected location
    store_path_obj = Path(settings.store_path)
    assert store_path_obj.is_dir()

    # Open the Zarr group and navigate to the correct path
    root_group = zarr.open(settings.store_path, mode="r")

    # Navigate through the path to get to the array
    current_group = root_group
    path_parts = output_key.split("/")

    for part in path_parts:
        assert part in current_group, f"Path part '{part}' not found in group"
        current_group = current_group[part]

    array = (
        current_group["0"]
        if downsampling_method is not None
        else current_group
    )

    # Verify array shape and contents
    assert array.shape == data.shape
    assert np.array_equal(array, data)


def test_anisotropic_downsampling(settings: StreamSettings, store_path: Path):
    settings.store_path = str(store_path / "anisotropic_downsampling.zarr")
    settings.version = ZarrVersion.V3
    settings.arrays[0].data_type = np.uint8
    settings.arrays[0].downsampling_method = DownsamplingMethod.MEAN
    settings.arrays[0].dimensions = [
        Dimension(
            name="z",
            kind=DimensionType.SPACE,
            array_size_px=1000,
            chunk_size_px=256,
            shard_size_chunks=4,
        ),
        Dimension(
            name="y",
            kind=DimensionType.SPACE,
            array_size_px=2000,
            chunk_size_px=256,
            shard_size_chunks=8,
        ),
        Dimension(
            name="x",
            kind=DimensionType.SPACE,
            array_size_px=2000,
            chunk_size_px=256,
            shard_size_chunks=8,
        ),
    ]

    stream = ZarrStream(settings)
    assert stream

    # Create test data
    data = np.random.randint(
        0,
        2**8 - 1,
        (
            settings.arrays[0].dimensions[0].array_size_px,
            settings.arrays[0].dimensions[1].array_size_px,
            settings.arrays[0].dimensions[2].array_size_px,
        ),
        dtype=np.uint8,
    )

    stream.append(data)
    stream.close()  # close the stream, flush the files

    # Open the Zarr group and verify the data
    group = zarr.open(settings.store_path, mode="r")
    assert "0" in group
    array = group["0"]
    assert array.shape == data.shape
    assert array.chunks == (256, 256, 256)
    # don't check the data itself, this is done elsewhere

    assert "1" in group
    array = group["1"]
    assert array.shape == (500, 1000, 1000)
    assert array.chunks == (256, 256, 256)

    assert "2" in group
    array = group["2"]
    assert array.shape == (250, 500, 500)
    assert array.chunks == (250, 256, 256)

    assert "3" in group
    array = group["3"]
    assert array.shape == (250, 250, 250)
    assert array.chunks == (250, 250, 250)

    assert "4" not in group  # No further downsampling


@pytest.mark.parametrize(
    ("version",),
    [
        (ZarrVersion.V2,),
        (ZarrVersion.V3,),
    ],
)
def test_multiarray_metadata_structure(
    settings: StreamSettings,
    store_path: Path,
    version: ZarrVersion,
):
    settings.store_path = str(store_path / "multiarray_metadata_test.zarr")
    settings.version = version

    # Configure three arrays matching the JSON examples

    # Array 0: Labels array at /labels (uint16, no compression, no downsampling)
    # Shape: [6, 3, 4, 48, 64] (t, c, z, y, x)
    settings.arrays = [
        ArraySettings(
            output_key="labels",
            data_type=np.uint16,
            dimensions=[
                Dimension(
                    name="t",
                    kind=DimensionType.TIME,
                    array_size_px=6,
                    chunk_size_px=3,
                    shard_size_chunks=1,
                ),
                Dimension(
                    name="c",
                    kind=DimensionType.CHANNEL,
                    array_size_px=3,
                    chunk_size_px=1,
                    shard_size_chunks=1,
                ),
                Dimension(
                    name="z",
                    kind=DimensionType.SPACE,
                    array_size_px=4,
                    chunk_size_px=2,
                    shard_size_chunks=1,
                ),
                Dimension(
                    name="y",
                    kind=DimensionType.SPACE,
                    array_size_px=48,
                    chunk_size_px=16,
                    shard_size_chunks=1,
                ),
                Dimension(
                    name="x",
                    kind=DimensionType.SPACE,
                    array_size_px=64,
                    chunk_size_px=16,
                    shard_size_chunks=1,
                ),
            ],
        ),
        # Array 1: Multiscale array at /path/to/array1 (uint8, no compression, with downsampling)
        # Shape: [10, 6, 48, 64] (t, z, y, x)
        ArraySettings(
            output_key="path/to/array1",
            data_type=np.uint8,
            downsampling_method=DownsamplingMethod.MEAN,
            dimensions=[
                Dimension(
                    name="t",
                    kind=DimensionType.TIME,
                    array_size_px=10,
                    chunk_size_px=5,
                    shard_size_chunks=1,
                ),
                Dimension(
                    name="z",
                    kind=DimensionType.SPACE,
                    array_size_px=6,
                    chunk_size_px=3,
                    shard_size_chunks=1,
                ),
                Dimension(
                    name="y",
                    kind=DimensionType.SPACE,
                    array_size_px=48,
                    chunk_size_px=16,
                    shard_size_chunks=1,
                ),
                Dimension(
                    name="x",
                    kind=DimensionType.SPACE,
                    array_size_px=64,
                    chunk_size_px=16,
                    shard_size_chunks=1,
                ),
            ],
        ),
        # Array 2: Compressed array at /path/to/array2 (uint32, with blosc compression)
        # Shape: [9, 48, 64] (z, y, x)
        ArraySettings(
            output_key="path/to/array2",
            data_type=np.uint32,
            compression=CompressionSettings(
                compressor=Compressor.BLOSC1,
                codec=CompressionCodec.BLOSC_LZ4,
                level=2,
                shuffle=1,
            ),
            dimensions=[
                Dimension(
                    name="z",
                    kind=DimensionType.SPACE,
                    array_size_px=9,
                    chunk_size_px=3,
                    shard_size_chunks=1,
                ),
                Dimension(
                    name="y",
                    kind=DimensionType.SPACE,
                    array_size_px=48,
                    chunk_size_px=16,
                    shard_size_chunks=1,
                ),
                Dimension(
                    name="x",
                    kind=DimensionType.SPACE,
                    array_size_px=64,
                    chunk_size_px=16,
                    shard_size_chunks=1,
                ),
            ],
        ),
    ]

    stream = ZarrStream(settings)
    assert stream

    # Create test data for labels array (5D: t,c,z,y,x)
    labels_data = np.zeros((6, 3, 4, 48, 64), dtype=np.uint16)
    for t in range(6):
        for c in range(3):
            for z in range(4):
                labels_data[t, c, z, :, :] = t * 100 + c * 10 + z

    # Create test data for array1 (4D: t,z,y,x)
    array1_data = np.zeros((10, 6, 48, 64), dtype=np.uint8)
    for t in range(10):
        for z in range(6):
            array1_data[t, z, :, :] = (t * 10 + z) % 256

    # Create test data for array2 (3D: z,y,x)
    array2_data = np.zeros((9, 48, 64), dtype=np.uint32)
    for z in range(9):
        array2_data[z, :, :] = z * 1000

    # Stream the data to each array
    stream.append(labels_data, key="labels")
    stream.append(array1_data, key="path/to/array1")
    stream.append(array2_data, key="path/to/array2")

    stream.close()

    # Verify the data structure
    store_path_obj = Path(settings.store_path)
    assert store_path_obj.is_dir()

    root_group = zarr.open(settings.store_path, mode="r")

    # Verify labels array
    labels_array = root_group["labels"]
    assert labels_array.shape == labels_data.shape
    assert labels_array.dtype == np.uint16
    assert np.array_equal(labels_array, labels_data)

    # Verify multiscale array1 structure
    array1_group = root_group["path"]["to"]["array1"]

    # Check multiscale metadata
    if version == ZarrVersion.V2:
        assert "multiscales" in array1_group.attrs
        assert len(array1_group.attrs["multiscales"]) > 0
    else:
        assert "ome" in array1_group.attrs
        assert "multiscales" in array1_group.attrs["ome"]
        assert len(array1_group.attrs["ome"]["multiscales"]) > 0

    # Check that all 3 LOD levels exist
    assert "0" in array1_group  # LOD 0 (full resolution)
    assert "1" in array1_group  # LOD 1
    assert "2" in array1_group  # LOD 2
    assert "3" not in array1_group  # No further LODs

    # Verify LOD 0 data
    lod0_array = array1_group["0"]
    assert lod0_array.shape == array1_data.shape
    assert lod0_array.dtype == np.uint8
    assert np.array_equal(lod0_array, array1_data)

    # Verify compressed array2
    array2_group = root_group["path"]["to"]["array2"]
    assert array2_group.shape == array2_data.shape
    assert array2_group.dtype == np.uint32
    assert np.array_equal(array2_group, array2_data)


def validate_generic_group_metadata(base_path: Path):
    """Validate generic Zarr group metadata files."""
    paths = [
        base_path / "zarr.json",
        base_path / "test_plate" / "C" / "zarr.json",
        base_path / "test_plate" / "D" / "zarr.json",
    ]

    for path in paths:
        assert path.exists(), f"Missing metadata file: {path}"

        with open(path, "r") as f:
            metadata = json.load(f)

        assert metadata["zarr_format"] == 3
        assert metadata["consolidated_metadata"] is None
        assert metadata["node_type"] == "group"
        assert metadata["attributes"] == {}


def validate_plate_metadata(base_path: Path):
    """Validate plate-level HCS metadata."""
    plate_path = base_path / "test_plate" / "zarr.json"
    assert plate_path.exists()

    with open(plate_path, "r") as f:
        metadata = json.load(f)

    assert metadata["zarr_format"] == 3
    assert metadata["consolidated_metadata"] is None
    assert metadata["node_type"] == "group"

    attributes = metadata["attributes"]
    assert "ome" in attributes

    ome = attributes["ome"]
    assert len(ome) == 2
    assert ome["version"] == "0.5"

    plate = ome["plate"]
    assert len(plate) == 7

    # Validate plate fields
    assert plate["name"] == "Test Plate"
    assert plate["version"] == "0.5"
    assert plate["field_count"] == 2

    # Validate acquisitions
    acquisitions = plate["acquisitions"]
    assert len(acquisitions) == 2

    acq0 = acquisitions[0]
    assert len(acq0) == 4
    assert acq0["id"] == 0
    assert acq0["maximumfieldcount"] == 1
    assert acq0["name"] == "Meas_01(2012-07-31_10-41-12)"
    assert acq0["starttime"] == 1343731272000
    assert "endtime" not in acq0

    acq1 = acquisitions[1]
    assert len(acq1) == 5
    assert acq1["id"] == 1
    assert acq1["maximumfieldcount"] == 1
    assert acq1["name"] == "Meas_02(2012-07-31_10-45-12)"
    assert acq1["starttime"] == 1343735801000
    assert acq1["endtime"] == 1343737645000

    # Validate columns
    columns = plate["columns"]
    assert len(columns) == 12
    for i in range(1, 13):
        assert columns[i - 1]["name"] == str(i)

    # Validate rows
    rows = plate["rows"]
    assert len(rows) == 8
    for i, letter in enumerate("ABCDEFGH"):
        assert rows[i]["name"] == letter

    # Validate wells
    wells = plate["wells"]
    assert len(wells) == 2

    well0 = wells[0]
    assert len(well0) == 3
    assert well0["rowIndex"] == 2  # C
    assert well0["columnIndex"] == 4  # 5
    assert well0["path"] == "C/5"

    well1 = wells[1]
    assert len(well1) == 3
    assert well1["rowIndex"] == 3  # D
    assert well1["columnIndex"] == 6  # 7
    assert well1["path"] == "D/7"


def validate_well_metadata(base_path: Path):
    """Validate well-level HCS metadata."""
    paths = [
        base_path / "test_plate" / "C" / "5" / "zarr.json",
        base_path / "test_plate" / "D" / "7" / "zarr.json",
    ]
    expected_image_counts = [2, 1]

    for i, path in enumerate(paths):
        assert path.exists()

        with open(path, "r") as f:
            metadata = json.load(f)

        assert metadata["zarr_format"] == 3
        assert metadata["consolidated_metadata"] is None
        assert metadata["node_type"] == "group"

        attributes = metadata["attributes"]
        assert "ome" in attributes

        ome = attributes["ome"]
        assert len(ome) == 2
        assert ome["version"] == "0.5"

        well = ome["well"]
        assert len(well) == 2
        assert well["version"] == "0.5"

        images = well["images"]
        assert len(images) == expected_image_counts[i]

        # Check first image
        img0 = images[0]
        assert len(img0) == 2
        assert img0["acquisition"] == 0
        assert img0["path"] == "fov1"

        # Check second image if present
        if expected_image_counts[i] == 2:
            img1 = images[1]
            assert len(img1) == 2
            assert img1["acquisition"] == 1
            assert img1["path"] == "fov2"


def check_arrays_exist(base_path: Path):
    """Check that HCS arrays exist."""
    paths = [
        base_path / "test_plate" / "C" / "5" / "fov1",
        base_path / "test_plate" / "C" / "5" / "fov2",
        base_path / "test_plate" / "D" / "7" / "fov1",
    ]

    for path in paths:
        array_path = path / "zarr.json"
        assert array_path.exists(), f"Missing array: {path}"


def check_arrays_exist_mixed(base_path: Path):
    """Check that both HCS and flat arrays exist."""
    paths = [
        base_path / "test_plate" / "C" / "5" / "fov1",
        base_path / "test_plate" / "C" / "5" / "fov2",
        base_path / "test_plate" / "D" / "7" / "fov1",
        base_path / "test_plate" / "C" / "5" / "labels",
    ]

    for path in paths:
        array_path = path / "zarr.json"
        assert array_path.exists(), f"Missing array: {path}"


def test_pure_hcs_acquisition(store_path: Path):
    """Test pure HCS acquisition (equivalent to stream-pure-hcs-acquisition.cpp)"""
    plate = create_hcs_settings()

    settings = StreamSettings(
        store_path=str(store_path / "test.zarr"),
        version=ZarrVersion.V3,
        overwrite=True,
        arrays=[],  # No flat arrays, only HCS
        hcs_plates=[plate],
    )

    expected_keys = {"test_plate/C/5/fov1", "test_plate/C/5/fov2", "test_plate/D/7/fov1"}
    actual_keys = set(settings.get_array_keys())
    assert expected_keys == actual_keys


    stream = ZarrStream(settings)
    assert stream

    # Write test data to each FOV
    # FOV1 in well C/5 (uint8, 3D: z,y,x)
    fov1_data = np.zeros((640, 480), dtype=np.uint8)
    stream.append(fov1_data, key="test_plate/C/5/fov1")

    # FOV2 in well C/5 (uint16, 3D: z,y,x)
    fov2_data = np.zeros((640, 480), dtype=np.uint16)
    stream.append(fov2_data, key="test_plate/C/5/fov2")

    # FOV1 in well D/7 (uint16, 5D: t,c,z,y,x)
    d7_fov1_data = np.zeros((512, 512), dtype=np.uint16)
    stream.append(d7_fov1_data, key="test_plate/D/7/fov1")

    stream.close()

    # Validate the structure
    validate_generic_group_metadata(store_path / "test.zarr")
    validate_plate_metadata(store_path / "test.zarr")
    validate_well_metadata(store_path / "test.zarr")
    check_arrays_exist(store_path / "test.zarr")


def test_mixed_flat_and_hcs_acquisition(store_path: Path):
    """Test mixed flat and HCS acquisition (equivalent to stream-mixed-flat-and-hcs-acquisition.cpp)"""
    plate = create_hcs_settings()

    # Add a labels array outside the HCS structure
    labels_array = ArraySettings(
        output_key="test_plate/C/5/labels",
        data_type=np.uint8,
        dimensions=[
            Dimension(
                name="z",
                kind=DimensionType.SPACE,
                array_size_px=0,
                chunk_size_px=1,
                shard_size_chunks=1,
            ),
            Dimension(
                name="y",
                kind=DimensionType.SPACE,
                array_size_px=480,
                chunk_size_px=256,
                shard_size_chunks=4,
            ),
            Dimension(
                name="x",
                kind=DimensionType.SPACE,
                array_size_px=640,
                chunk_size_px=256,
                shard_size_chunks=4,
            ),
        ],
    )

    settings = StreamSettings(
        store_path=str(store_path / "test.zarr"),
        version=ZarrVersion.V3,
        overwrite=True,
        arrays=[labels_array],
        hcs_plates=[plate],
    )

    expected_keys = {"test_plate/C/5/fov1", "test_plate/C/5/fov2", "test_plate/D/7/fov1", "test_plate/C/5/labels"}
    actual_keys = set(settings.get_array_keys())
    assert expected_keys == actual_keys

    stream = ZarrStream(settings)
    assert stream

    del settings

    # Write test data to each array
    # FOV1 in well C/5
    fov1_data = np.zeros((640, 480), dtype=np.uint8)
    stream.append(fov1_data, key="test_plate/C/5/fov1")

    # FOV2 in well C/5
    fov2_data = np.zeros((640, 480), dtype=np.uint16)
    stream.append(fov2_data, key="test_plate/C/5/fov2")

    # FOV1 in well D/7
    d7_fov1_data = np.zeros((512, 512), dtype=np.uint16)
    stream.append(d7_fov1_data, key="test_plate/D/7/fov1")

    # Labels array in well C/5
    labels_data = np.zeros((640, 480), dtype=np.uint8)
    stream.append(labels_data, key="test_plate/C/5/labels")

    stream.close()

    # Validate the structure (same as pure HCS)
    validate_generic_group_metadata(store_path / "test.zarr")
    validate_plate_metadata(store_path / "test.zarr")
    validate_well_metadata(store_path / "test.zarr")
    check_arrays_exist_mixed(store_path / "test.zarr")


def test_with_ragged_final_shard(store_path: Path):
    settings = StreamSettings(
        store_path=str(store_path / "test.zarr"),
        arrays=[
            ArraySettings(
                dimensions=[
                    Dimension(name="t", array_size_px=0, chunk_size_px=1, shard_size_chunks=16, kind=DimensionType.TIME),
                    Dimension(name="c", array_size_px=1, chunk_size_px=1, shard_size_chunks=1, kind=DimensionType.CHANNEL),
                    Dimension(name="z", array_size_px=125, chunk_size_px=125, shard_size_chunks=1),
                    Dimension(name="y", array_size_px=125, chunk_size_px=125, shard_size_chunks=1),
                    Dimension(name="x", array_size_px=125, chunk_size_px=125, shard_size_chunks=1),
                ],
                data_type=np.uint8,
            )
        ]
    )
    stream = ZarrStream(settings)

    assert stream is not None

    # 17 timepoints, with 16 timepoints per shard
    data = np.random.randint(0, 255, (17, 1, 125, 125, 125), dtype=np.uint8)
    stream.append(data)
    stream.close()

    del stream

    dataset = zarr.open(settings.store_path)

    np.testing.assert_array_equal(data, dataset["0"])
