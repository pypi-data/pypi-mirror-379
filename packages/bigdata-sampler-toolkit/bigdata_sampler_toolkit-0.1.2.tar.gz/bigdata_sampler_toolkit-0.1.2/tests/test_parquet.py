# tests/test_parquet_sampler.py
import os
import pandas as pd
from bigdata_sampler import sampler

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")
os.makedirs(TEST_DATA_DIR, exist_ok=True)

TEST_PARQUET = os.path.join(TEST_DATA_DIR, "test.parquet")
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [30, 25, 22]
})
df.to_parquet(TEST_PARQUET)

OUTPUT_PARQUET = os.path.join(TEST_DATA_DIR, "sampled.parquet")

def test_sample_parquet():
    sampler.sample_parquet(TEST_PARQUET, OUTPUT_PARQUET, sample_size=2)
    sampled_df = pd.read_parquet(OUTPUT_PARQUET)
    assert len(sampled_df) == 2
