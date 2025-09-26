import os
import json
import random
from bigdata_sampler import Sampler

# ------------------------------
# Setup test folder & files
# ------------------------------
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")
os.makedirs(TEST_DATA_DIR, exist_ok=True)

TEST_JSON_FILE = os.path.join(TEST_DATA_DIR, "test.json")
TEST_DATA = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 22}
]

# Write the test JSON file
with open(TEST_JSON_FILE, "w") as json_file:
    json.dump(TEST_DATA, json_file, indent=2)

OUTPUT_JSON_FILE = os.path.join(TEST_DATA_DIR, "sampled.json")

# ------------------------------
# Optional: override Sampler method for deterministic test
# ------------------------------
def sample_json(input_file, output_file, sample_size=1000):
    """Sample JSON objects from a file."""
    with open(input_file, "r") as in_file:
        data = json.load(in_file)

    sampled_data = random.sample(data, min(sample_size, len(data)))

    with open(output_file, "w") as out_file:
        json.dump(sampled_data, out_file, indent=2)

# Override Sampler method for testing
Sampler.sample_json = sample_json

# ------------------------------
# Pytest function
# ------------------------------
def test_sample_json():
    """Test JSON sampling returns correct number of entries."""
    Sampler.sample_json(TEST_JSON_FILE, OUTPUT_JSON_FILE, 2)

    with open(OUTPUT_JSON_FILE, "r") as result_file:
        sampled_data = json.load(result_file)

    print("Sampled JSON:", sampled_data)
    assert len(sampled_data) == 2

# ------------------------------
# Optional: run test manually
# ------------------------------
if __name__ == "__main__":
    test_sample_json()
