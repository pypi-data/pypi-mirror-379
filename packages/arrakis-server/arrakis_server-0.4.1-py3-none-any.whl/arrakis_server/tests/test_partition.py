from collections import Counter

import numpy

from arrakis_server.channel import Channel
from arrakis_server.partition import generate_partition_id, partition_channels


def create_channel(
    name: str,
    data_type: str = "float64",
    sample_rate: int =16384,
    publisher: str | None = None,
    partition_id: str | None = None,
) -> Channel:
    return Channel(
        name=name,
        data_type=data_type,
        sample_rate=sample_rate,
        publisher=publisher,
        partition_id=partition_id,
    )


def test_generate_partition_id_without_channel():
    publisher_id = "test_publisher"
    partition_id = generate_partition_id(publisher_id)

    assert publisher_id in partition_id


def test_generate_partition_id_with_channel():
    publisher_id = "test_publisher"
    channel = Channel(
        name="H1:TEST-CHANNEL_1", data_type="float64", sample_rate=16384
    )
    partition_id = generate_partition_id(publisher_id, channel)

    assert publisher_id in partition_id
    assert "TEST" in partition_id


def test_generate_partition_id_uniqueness():
    publisher_id = "test_publisher"
    ids = {generate_partition_id(publisher_id) for _ in range(100)}
    assert len(ids) == 100


def test_channels_with_existing_partition_ids():
    channels = [
        create_channel(
            "H1:TEST-CHANNEL_A",
            publisher="test_publisher",
            partition_id="existing_partition",
        )
    ]
    result = partition_channels(channels, "test_publisher")

    assert len(result) == 1
    assert result[0].publisher == "test_publisher"
    assert result[0].partition_id == "existing_partition"


def test_single_new_channel():
    channels = [create_channel("H1:TEST-CHANNEL_A")]
    result = partition_channels(channels, "test_publisher")

    assert len(result) == 1
    assert result[0].publisher == "test_publisher"
    assert result[0].partition_id is not None
    assert "test_publisher" in result[0].partition_id


def test_multiple_channels_same_data_type():
    channels = [
        create_channel("H1:TEST-CHANNEL_A"),
        create_channel("H1:TEST-CHANNEL_B"),
        create_channel("H1:TEST-CHANNEL_C"),
    ]
    result = partition_channels(channels, "test_publisher", max_channels=100)

    assert len(result) == 3
    partition_ids = {ch.partition_id for ch in result}
    assert len(partition_ids) == 1  # All in same partition

    for channel in result:
        assert channel.publisher == "test_publisher"
        assert channel.partition_id is not None


def test_channels_different_data_types():
    channels = [
        create_channel("H1:TEST-CHANNEL_A", data_type="float64"),
        create_channel("H1:TEST-CHANNEL_B", data_type="int32"),
        create_channel("H1:TEST-CHANNEL_C", data_type="float64"),
    ]
    result = partition_channels(channels, "test_publisher")

    assert len(result) == 3
    float64_channels = [ch for ch in result if ch.data_type == numpy.float64]
    int32_channels = [ch for ch in result if ch.data_type == numpy.int32]

    # Channels with same dtype should share partition, different dtypes separate
    float64_partition_ids = {ch.partition_id for ch in float64_channels}
    int32_partition_ids = {ch.partition_id for ch in int32_channels}

    assert len(float64_partition_ids) == 1
    assert len(int32_partition_ids) == 1
    assert float64_partition_ids != int32_partition_ids


def test_multiple_partitions():
    # Create enough channels to exceed max_channels and trigger
    # partition_fraction logic
    channels = [create_channel(f"H1:TEST-CHANNEL_{i:03d}") for i in range(120)]

    # With max_channels=100 and partition_fraction=0.8, new partitions
    # should have max 80 channels
    result = partition_channels(
        channels, "test_publisher", max_channels=100, partition_fraction=0.8
    )

    assert len(result) == 120
    partition_ids = {ch.partition_id for ch in result}
    assert len(partition_ids) >= 2

    partition_counts = Counter(ch.partition_id for ch in result)
    partition_sizes = list(partition_counts.values())
    for size in partition_sizes:
        assert size <= 80


def test_partitions_existing_metadata():
    # Create metadata with existing partitions
    existing_channel = create_channel(
        "H1:TEST-CHANNEL_B",
        publisher="test_publisher",
        partition_id="existing_partition",
    )
    metadata = {"H1:TEST-CHANNEL_B": existing_channel}

    channels = [
        create_channel("H1:TEST-CHANNEL_A"),  # New, will be inserted before B
        create_channel("H1:TEST-CHANNEL_B"),  # Exists in metadata
        create_channel("H1:TEST-CHANNEL_C"),  # New, will be inserted after B
    ]

    result = partition_channels(
        channels, "test_publisher", metadata=metadata, max_channels=10
    )

    assert len(result) == 3

    # Channel B should use existing partition
    channel_b = next(ch for ch in result if ch.name == "H1:TEST-CHANNEL_B")
    assert channel_b.partition_id == "existing_partition"

    # Channels A and C should be assigned to existing partition
    # (alphabetical insertion)
    channel_a = next(ch for ch in result if ch.name == "H1:TEST-CHANNEL_A")
    channel_c = next(ch for ch in result if ch.name == "H1:TEST-CHANNEL_C")
    assert channel_a.partition_id == "existing_partition"
    assert channel_c.partition_id == "existing_partition"


def test_metadata_filtered_by_publisher():
    # Create metadata with different publishers
    metadata = {
        "H1:TEST-CHANNEL_A": create_channel(
            "H1:TEST-CHANNEL_A",
            publisher="other_publisher",
            partition_id="other_partition",
        ),
        "H1:TEST-CHANNEL_B": create_channel(
            "H1:TEST-CHANNEL_B",
            publisher="test_publisher",
            partition_id="correct_partition",
        ),
    }

    channels = [
        create_channel("H1:TEST-CHANNEL_A"),
        create_channel("H1:TEST-CHANNEL_B"),
    ]

    result = partition_channels(channels, "test_publisher", metadata=metadata)

    # Only metadata matching the publisher should be used
    channel_a = next(ch for ch in result if ch.name == "H1:TEST-CHANNEL_A")
    channel_b = next(ch for ch in result if ch.name == "H1:TEST-CHANNEL_B")

    assert channel_b.partition_id == "correct_partition"
    assert channel_a.partition_id != "other_partition"  # Should get new partition


def test_mixed_partitioned_and_new_channels():
    # Channel B has existing partition and must be in metadata
    existing_channel_b = create_channel(
        "H1:TEST-CHANNEL_B", publisher="test_publisher", partition_id="existing"
    )
    metadata = {"H1:TEST-CHANNEL_B": existing_channel_b}

    channels = [
        create_channel("H1:TEST-CHANNEL_A"),  # New
        create_channel(
            "H1:TEST-CHANNEL_B", publisher="test_publisher", partition_id="existing"
        ),  # Has partition
        create_channel("H1:TEST-CHANNEL_C"),  # New
    ]

    result = partition_channels(channels, "test_publisher", metadata=metadata)

    assert len(result) == 3

    # Channel B should keep its existing partition
    channel_b = next(ch for ch in result if ch.name == "H1:TEST-CHANNEL_B")
    assert channel_b.partition_id == "existing"

    # Channels A and C should get new partitions
    channel_a = next(ch for ch in result if ch.name == "H1:TEST-CHANNEL_A")
    channel_c = next(ch for ch in result if ch.name == "H1:TEST-CHANNEL_C")

    assert channel_a.partition_id is not None
    assert channel_c.partition_id is not None
    assert channel_a.partition_id != "existing"
    assert channel_c.partition_id != "existing"


def test_channel_order_preserved():
    channels = [
        create_channel("H1:TEST-CHANNEL_Z"),
        create_channel("H1:TEST-CHANNEL_A"),
        create_channel("H1:TEST-CHANNEL_M"),
    ]

    result = partition_channels(channels, "test_publisher")

    # Output order should match input order
    assert [ch.name for ch in result] == [ch.name for ch in channels]


def test_boundary_conditions():
    # Test exactly at max_channels limit
    channels = [create_channel(f"H1:TEST-CHANNEL_{i:03d}") for i in range(100)]
    result = partition_channels(channels, "test_publisher", max_channels=100)

    partition_ids = {ch.partition_id for ch in result}
    assert len(partition_ids) == 1  # Should fit in single partition

    # Test one over the limit
    channels.append(create_channel("H1:TEST-CHANNEL_100"))
    result = partition_channels(channels, "test_publisher", max_channels=100)

    partition_ids = {ch.partition_id for ch in result}
    assert len(partition_ids) >= 2  # Should create additional partition
