import os
from bigdata_sampler import Sampler

# Test data folder (relative path)
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")
os.makedirs(TEST_DATA_DIR, exist_ok=True)

# Create a small sample CSV for testing
TEST_CSV = os.path.join(TEST_DATA_DIR, "test.csv")
with open(TEST_CSV, "w") as fw:
    fw.write("name,age,city\nAlice,30,NY\nBob,25,LA\nCharlie,22,SF\n")

# Output file for testing
OUTPUT_CSV = os.path.join(TEST_DATA_DIR, "sampled.csv")


def test_sample_csv():
    # Sample 2 rows
    Sampler.sample_csv(TEST_CSV, OUTPUT_CSV, 2)

    # Read output and check if it has 2 rows + header
    with open(OUTPUT_CSV, "r") as fr:
        lines = fr.readlines()

    assert len(lines) == 3  # 2 data rows + header
    assert lines[0].strip() == "name,age,city"
