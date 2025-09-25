# tests/test_avro_sampler.py
import os
import fastavro
from bigdata_sampler import sampler

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")
os.makedirs(TEST_DATA_DIR, exist_ok=True)

TEST_AVRO = os.path.join(TEST_DATA_DIR, "test.avro")
OUTPUT_AVRO = os.path.join(TEST_DATA_DIR, "sampled.avro")

records = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 22}
]

schema = {
    "type": "record",
    "name": "Person",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "age", "type": "int"}
    ]
}

# Write test Avro file
with open(TEST_AVRO, "wb") as out:
    fastavro.writer(out, schema, records)

def test_sample_avro():
    sampler.sample_avro(TEST_AVRO, OUTPUT_AVRO, sample_size=2)
    # Read sampled output
    with open(OUTPUT_AVRO, "rb") as fo:
        sampled = list(fastavro.reader(fo))
    assert len(sampled) == 2
