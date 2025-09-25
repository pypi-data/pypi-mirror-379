import math

import polars as pl
import pyarrow as pa
import pytest

from planar.data.dataset import PlanarDataset
from planar.testing.planar_test_client import PlanarTestClient


@pytest.fixture(name="app")
def app_fixture(app_with_data):
    """Use the shared app_with_data fixture as 'app' for this test module."""
    return app_with_data


async def test_stream_arrow_chunks(
    client: PlanarTestClient,
):
    dataset_name = "test_streaming"
    dataset_size = 10_000
    batch_size = 1000

    dataset = await PlanarDataset.create(dataset_name)

    df = pl.DataFrame({"id": range(dataset_size)}).with_columns(
        pl.format("value_{}", pl.col("id")).alias("value")
    )

    await dataset.write(df)

    response = await client.get(
        f"/planar/v1/datasets/content/{dataset_name}/arrow-stream",
        params={"batch_size": batch_size, "limit": dataset_size},
    )

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/vnd.apache.arrow.stream"
    assert "test_streaming.arrow" in response.headers.get("content-disposition", "")
    assert response.headers.get("x-batch-size") == str(batch_size)

    content = await response.aread()
    buffer = pa.py_buffer(content)
    reader = pa.ipc.open_stream(buffer)

    batch_info = []
    total_rows_received = 0
    all_ids = []

    try:
        while True:
            arrow_batch = reader.read_next_batch()
            batch_info.append(
                {
                    "rows": arrow_batch.num_rows,
                    "columns": arrow_batch.num_columns,
                }
            )
            total_rows_received += arrow_batch.num_rows

            id_column = arrow_batch.column("id")
            batch_ids = id_column.to_pylist()
            all_ids.extend(batch_ids)
    except StopIteration:
        pass

    expected_batches = math.ceil(dataset_size / batch_size)

    assert len(batch_info) == expected_batches
    assert total_rows_received == dataset_size

    # Verify data integrity - check that we received all expected IDs
    assert len(all_ids) == dataset_size
    assert set(all_ids) == set(range(dataset_size))
    assert sum(all_ids) == sum(range(dataset_size))


async def test_stream_arrow_with_limit(
    client: PlanarTestClient,
):
    """Test that the limit parameter properly restricts the number of rows streamed."""
    dataset_name = "test_streaming_limit"
    dataset_size = 1000
    batch_size = 100
    row_limit = 250  # Should get 3 batches (100 + 100 + 50)

    dataset = await PlanarDataset.create(dataset_name)

    # Create test data
    df = pl.DataFrame({"id": range(dataset_size)}).with_columns(
        pl.format("value_{}", pl.col("id")).alias("value")
    )

    await dataset.write(df)

    response = await client.get(
        f"/planar/v1/datasets/content/{dataset_name}/arrow-stream",
        params={"batch_size": batch_size, "limit": row_limit},
    )

    assert response.status_code == 200
    assert response.headers["x-row-limit"] == str(row_limit)

    content = await response.aread()
    buffer = pa.py_buffer(content)
    reader = pa.ipc.open_stream(buffer)

    total_rows_received = 0
    batch_count = 0

    try:
        while True:
            arrow_batch = reader.read_next_batch()
            total_rows_received += arrow_batch.num_rows
            batch_count += 1
    except StopIteration:
        pass

    # Should receive exactly the limited number of rows
    assert total_rows_received == row_limit
    # Should receive expected number of batches (3: 100, 100, 50)
    expected_batches = math.ceil(row_limit / batch_size)
    assert batch_count == expected_batches


async def test_stream_arrow_empty_dataset(
    client: PlanarTestClient,
):
    """Test streaming behavior with an empty dataset."""
    dataset_name = "test_empty_stream"
    batch_size = 100

    dataset = await PlanarDataset.create(dataset_name)

    # Create empty dataset
    df = pl.DataFrame(
        {"id": [], "value": []}, schema={"id": pl.Int64, "value": pl.Utf8}
    )
    await dataset.write(df)

    response = await client.get(
        f"/planar/v1/datasets/content/{dataset_name}/arrow-stream",
        params={"batch_size": batch_size},
    )

    assert response.status_code == 200

    content = await response.aread()
    buffer = pa.py_buffer(content)
    reader = pa.ipc.open_stream(buffer)

    # Should be able to read the schema and get one empty batch
    total_rows = 0
    batch_count = 0

    try:
        while True:
            arrow_batch = reader.read_next_batch()
            total_rows += arrow_batch.num_rows
            batch_count += 1
    except StopIteration:
        pass

    # Should have exactly 1 empty batch (our fallback for empty datasets)
    assert batch_count == 1
    assert total_rows == 0


async def test_stream_arrow_single_batch(
    client: PlanarTestClient,
):
    """Test streaming when dataset size is smaller than batch size."""
    dataset_name = "test_single_batch"
    dataset_size = 50
    batch_size = 100

    dataset = await PlanarDataset.create(dataset_name)

    df = pl.DataFrame({"id": range(dataset_size)}).with_columns(
        pl.format("value_{}", pl.col("id")).alias("value")
    )

    await dataset.write(df)

    response = await client.get(
        f"/planar/v1/datasets/content/{dataset_name}/arrow-stream",
        params={"batch_size": batch_size},
    )

    assert response.status_code == 200

    content = await response.aread()
    buffer = pa.py_buffer(content)
    reader = pa.ipc.open_stream(buffer)

    total_rows = 0
    batch_count = 0

    try:
        while True:
            arrow_batch = reader.read_next_batch()
            total_rows += arrow_batch.num_rows
            batch_count += 1
    except StopIteration:
        pass

    assert batch_count == 1
    assert total_rows == dataset_size


async def test_get_schemas_endpoint(
    client: PlanarTestClient,
):
    """Test the GET /schemas endpoint."""
    response = await client.get("/planar/v1/datasets/schemas")

    assert response.status_code == 200
    schemas = response.json()
    assert isinstance(schemas, list)
    assert "main" in schemas  # Default schema should exist


async def test_list_datasets_metadata_endpoint(
    client: PlanarTestClient,
):
    """Test the GET /metadata endpoint (list all datasets)."""
    # Create a test dataset first
    dataset_name = "test_list_datasets"
    dataset = await PlanarDataset.create(dataset_name)

    df = pl.DataFrame({"id": [1, 2, 3], "name": ["a", "b", "c"]})
    await dataset.write(df)

    response = await client.get("/planar/v1/datasets/metadata")

    assert response.status_code == 200
    datasets = response.json()
    assert isinstance(datasets, list)

    # Find our test dataset
    test_dataset = next((d for d in datasets if d["name"] == dataset_name), None)
    assert test_dataset is not None
    assert test_dataset["row_count"] == 3
    assert "id" in test_dataset["table_schema"]
    assert "name" in test_dataset["table_schema"]


async def test_list_datasets_metadata_with_pagination(
    client: PlanarTestClient,
):
    """Test the GET /metadata endpoint with pagination parameters."""
    response = await client.get(
        "/planar/v1/datasets/metadata",
        params={"limit": 5, "offset": 0, "schema_name": "main"},
    )

    assert response.status_code == 200
    datasets = response.json()
    assert isinstance(datasets, list)
    assert len(datasets) <= 5  # Should respect limit


async def test_get_dataset_metadata_endpoint(
    client: PlanarTestClient,
):
    """Test the GET /metadata/{dataset_name} endpoint."""
    dataset_name = "test_single_metadata"
    dataset = await PlanarDataset.create(dataset_name)

    df = pl.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "value": ["apple", "banana", "cherry", "date", "elderberry"],
        }
    )
    await dataset.write(df)

    response = await client.get(f"/planar/v1/datasets/metadata/{dataset_name}")

    assert response.status_code == 200
    metadata = response.json()
    assert metadata["name"] == dataset_name
    assert metadata["row_count"] == 5
    assert "id" in metadata["table_schema"]
    assert "value" in metadata["table_schema"]


async def test_get_dataset_metadata_not_found(
    client: PlanarTestClient,
):
    """Test the GET /metadata/{dataset_name} endpoint with non-existent dataset."""
    response = await client.get("/planar/v1/datasets/metadata/nonexistent_dataset")

    assert response.status_code == 404
    error = response.json()
    assert "not found" in error["detail"].lower()


async def test_download_dataset_endpoint(
    client: PlanarTestClient,
):
    """Test the GET /content/{dataset_name}/download endpoint."""
    dataset_name = "test_download"
    dataset = await PlanarDataset.create(dataset_name)

    df = pl.DataFrame({"id": [1, 2, 3], "value": ["x", "y", "z"]})
    await dataset.write(df)

    response = await client.get(f"/planar/v1/datasets/content/{dataset_name}/download")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/x-parquet"
    assert f"{dataset_name}.parquet" in response.headers.get("content-disposition", "")

    # Verify we get valid parquet content
    content = await response.aread()
    assert len(content) > 0

    # Verify it's valid parquet by reading it back
    import pyarrow.parquet as pq

    parquet_buffer = pa.py_buffer(content)
    table = pq.read_table(parquet_buffer)
    assert table.num_rows == 3
    assert table.num_columns == 2


async def test_download_dataset_not_found(
    client: PlanarTestClient,
):
    """Test the GET /content/{dataset_name}/download endpoint with non-existent dataset."""
    response = await client.get(
        "/planar/v1/datasets/content/nonexistent_dataset/download"
    )

    assert response.status_code == 404
    error = response.json()
    assert "not found" in error["detail"].lower()


async def test_stream_arrow_dataset_not_found(
    client: PlanarTestClient,
):
    """Test the GET /content/{dataset_name}/arrow-stream endpoint with non-existent dataset."""
    response = await client.get(
        "/planar/v1/datasets/content/nonexistent_dataset/arrow-stream"
    )

    assert response.status_code == 404
    error = response.json()
    assert "not found" in error["detail"].lower()


async def test_get_dataset_metadata_empty_dataset(
    client: PlanarTestClient,
):
    """Test GET /metadata/{dataset_name} with empty dataset."""
    dataset_name = "test_empty_metadata"
    dataset = await PlanarDataset.create(dataset_name)

    # Create empty dataset
    df = pl.DataFrame(
        {"id": [], "value": []}, schema={"id": pl.Int64, "value": pl.Utf8}
    )
    await dataset.write(df)

    response = await client.get(f"/planar/v1/datasets/metadata/{dataset_name}")
    assert response.status_code == 200

    metadata = response.json()
    assert metadata["name"] == dataset_name
    assert metadata["row_count"] == 0
    assert "id" in metadata["table_schema"]
    assert "value" in metadata["table_schema"]


async def test_list_datasets_metadata_empty_dataset(
    client: PlanarTestClient,
):
    """Test GET /metadata with empty dataset in the list."""
    dataset_name = "test_empty_in_list"
    dataset = await PlanarDataset.create(dataset_name)

    # Create empty dataset
    df = pl.DataFrame(
        {"id": [], "value": []}, schema={"id": pl.Int64, "value": pl.Utf8}
    )
    await dataset.write(df)

    response = await client.get("/planar/v1/datasets/metadata")
    assert response.status_code == 200

    datasets = response.json()
    empty_dataset = next((d for d in datasets if d["name"] == dataset_name), None)
    assert empty_dataset is not None
    assert empty_dataset["row_count"] == 0


async def test_download_empty_dataset(
    client: PlanarTestClient,
):
    """Test GET /content/{dataset_name}/download with empty dataset."""
    dataset_name = "test_empty_download"
    dataset = await PlanarDataset.create(dataset_name)

    # Create empty dataset
    df = pl.DataFrame(
        {"id": [], "value": []}, schema={"id": pl.Int64, "value": pl.Utf8}
    )
    await dataset.write(df)

    response = await client.get(f"/planar/v1/datasets/content/{dataset_name}/download")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/x-parquet"
    assert f"{dataset_name}.parquet" in response.headers.get("content-disposition", "")

    # Verify we get valid parquet content (even if empty)
    content = await response.aread()
    assert len(content) > 0  # Should have parquet metadata even for empty data

    # Verify it's valid parquet by reading it back
    import pyarrow.parquet as pq

    parquet_buffer = pa.py_buffer(content)
    table = pq.read_table(parquet_buffer)
    assert table.num_rows == 0
    assert table.num_columns == 2  # id and value columns
    assert table.schema.field("id").type == pa.int64()
    assert table.schema.field("value").type == pa.string()
