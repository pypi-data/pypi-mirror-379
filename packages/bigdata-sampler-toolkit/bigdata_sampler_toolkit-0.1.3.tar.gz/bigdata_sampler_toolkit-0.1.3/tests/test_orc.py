# tests/test_orc_sampler.py
import os
os.environ["TZ"] = "UTC"
import pandas as pd
from bigdata_sampler import Sampler

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")
os.makedirs(TEST_DATA_DIR, exist_ok=True)

TEST_ORC = os.path.join(TEST_DATA_DIR, "test.orc")
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [30, 25, 22]
})
df.to_orc(TEST_ORC)

OUTPUT_ORC = os.path.join(TEST_DATA_DIR, "sampled.orc")

def test_sample_orc(monkeypatch):
    monkeypatch.setattr(Sampler, "sample_orc", lambda input_file, output_file, sample_size=2: None)
    Sampler.sample_orc(TEST_ORC, OUTPUT_ORC, 2)

