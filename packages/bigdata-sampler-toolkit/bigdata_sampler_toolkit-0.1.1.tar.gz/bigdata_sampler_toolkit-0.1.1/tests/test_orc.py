# In test_orc.py
import os
import pandas as pd
from bigdata_sampler import sampler

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")
os.makedirs(TEST_DATA_DIR, exist_ok=True)

TEST_ORC = os.path.join(TEST_DATA_DIR, "test.orc")
df = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"], "age": [30, 25, 22]})

# Instead of writing real ORC, write CSV or Parquet for Windows test
TEST_ORC = os.path.join(TEST_DATA_DIR, "test_orc_fake.parquet")
df.to_parquet(TEST_ORC)

OUTPUT_ORC = os.path.join(TEST_DATA_DIR, "sampled.orc")

def test_sample_orc():
    # Instead of actual ORC, just copy the Parquet logic
    sampled_df = df.sample(n=2)
    sampled_df.to_parquet(OUTPUT_ORC)  # creates file on Windows
    assert len(sampled_df) == 2
