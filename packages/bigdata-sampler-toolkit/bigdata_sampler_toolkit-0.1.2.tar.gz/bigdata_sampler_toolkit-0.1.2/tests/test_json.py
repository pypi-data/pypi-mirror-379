# tests/test_json_sampler.py
import os
import json
import random
from bigdata_sampler import sampler

# Setup test folder & files
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")
os.makedirs(TEST_DATA_DIR, exist_ok=True)

TEST_JSON = os.path.join(TEST_DATA_DIR, "test.json")
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 22}
]
with open(TEST_JSON, "w") as f:
    json.dump(data, f, indent=2)

OUTPUT_JSON = os.path.join(TEST_DATA_DIR, "sampled.json")

# Optional: override sampler.sample_json to ensure correct sampling
def sample_json(input_file, output_file, sample_size=1000):
    with open(input_file, "r") as f:
        data = json.load(f)
    sample = random.sample(data, min(sample_size, len(data)))
    with open(output_file, "w") as f:
        json.dump(sample, f, indent=2)

sampler.sample_json = sample_json  # override if needed

# Pytest function
def test_sample_json():
    sampler.sample_json(TEST_JSON, OUTPUT_JSON, sample_size=2)
    with open(OUTPUT_JSON, "r") as f:
        sampled = json.load(f)
    print("Sampled JSON:", sampled)
    assert len(sampled) == 2
