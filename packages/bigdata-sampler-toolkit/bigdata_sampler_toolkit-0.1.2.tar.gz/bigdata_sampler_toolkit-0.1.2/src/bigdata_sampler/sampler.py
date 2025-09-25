import random
import pyarrow.parquet as pq
import pyarrow.orc as orc
import fastavro
import pandas as pd


class Sampler:
    def __init__(self, sample_size=1000, random_state=42):
        self.sample_size = sample_size
        self.random_state = random_state

    def sample_csv(self, input_file, output_file):
        sample = []
        with open(input_file, "r") as f:
            header = f.readline()
            for i, line in enumerate(f, start=1):
                if i <= self.sample_size:
                    sample.append(line)
                else:
                    j = random.randint(1, i)
                    if j <= self.sample_size:
                        sample[j - 1] = line

        with open(output_file, "w") as f:
            f.write(header)
            f.writelines(sample)

    def sample_json(self, input_file, output_file):
        sample = []
        with open(input_file, "r") as f:
            for i, line in enumerate(f, start=1):
                if i <= self.sample_size:
                    sample.append(line)
                else:
                    j = random.randint(1, i)
                    if j <= self.sample_size:
                        sample[j - 1] = line

        with open(output_file, "w") as f:
            f.writelines(sample)

    def sample_parquet(self, input_file, output_file):
        table = pq.read_table(input_file)
        df = table.to_pandas()
        df_sampled = df.sample(n=self.sample_size, random_state=self.random_state)
        df_sampled.to_parquet(output_file)

    def sample_orc(self, input_file, output_file):
        table = orc.ORCFile(input_file).read()
        df = table.to_pandas()
        df_sampled = df.sample(n=self.sample_size, random_state=self.random_state)
        df_sampled.to_orc(output_file)

    def sample_avro(self, input_file, output_file):
        records = []
        with open(input_file, "rb") as f:
            reader = fastavro.reader(f)
            for i, record in enumerate(reader, start=1):
                if i <= self.sample_size:
                    records.append(record)
                else:
                    j = random.randint(1, i)
                    if j <= self.sample_size:
                        records[j - 1] = record

        schema = reader.writer_schema
        with open(output_file, "wb") as out:
            fastavro.writer(out, schema, records)
