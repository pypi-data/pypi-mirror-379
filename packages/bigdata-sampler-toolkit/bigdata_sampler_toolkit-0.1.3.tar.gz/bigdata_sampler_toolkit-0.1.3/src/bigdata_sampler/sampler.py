import random
import pyarrow.parquet as pq
import pyarrow.orc as orc
import fastavro


class Sampler:
    @staticmethod
    def sample_csv(input_file, output_file, sample_size=1000):
        sample = []
        with open(input_file, "r") as f:
            header = f.readline()
            for i, line in enumerate(f, start=1):
                if i <= sample_size:
                    sample.append(line)
                else:
                    j = random.randint(1, i)
                    if j <= sample_size:
                        sample[j - 1] = line

        with open(output_file, "w") as f:
            f.write(header)
            f.writelines(sample)

    @staticmethod
    def sample_json(input_file, output_file, sample_size=1000):
        sample = []
        with open(input_file, "r") as f:
            for i, line in enumerate(f, start=1):
                if i <= sample_size:
                    sample.append(line)
                else:
                    j = random.randint(1, i)
                    if j <= sample_size:
                        sample[j - 1] = line

        with open(output_file, "w") as f:
            f.writelines(sample)

    @staticmethod
    def sample_parquet(input_file, output_file, sample_size=1000):
        table = pq.read_table(input_file)
        df = table.to_pandas()
        df_sampled = df.sample(n=sample_size, random_state=42)
        df_sampled.to_parquet(output_file)

    @staticmethod
    def sample_orc(input_file, output_file, sample_size=1000):
        table = orc.ORCFile(input_file).read()
        df = table.to_pandas()
        df_sampled = df.sample(n=sample_size, random_state=42)

        # NOTE: pandas does not support to_orc directly.
        # Saving to Parquet as a fallback (or you can implement ORC write via pyarrow if needed).
        df_sampled.to_parquet(output_file.replace(".orc", ".parquet"))

    @staticmethod
    def sample_avro(input_file, output_file, sample_size=1000):
        records = []
        with open(input_file, "rb") as f:
            reader = fastavro.reader(f)
            for i, record in enumerate(reader, start=1):
                if i <= sample_size:
                    records.append(record)
                else:
                    j = random.randint(1, i)
                    if j <= sample_size:
                        records[j - 1] = record

            schema = reader.writer_schema

        with open(output_file, "wb") as out:
            fastavro.writer(out, schema, records)
