import pandas as pd
from io import StringIO

def process_csv(file):
    content = StringIO(file.file.read().decode("utf-8"))
    dataset = pd.read_csv(content)
    required_columns = {"Machine_ID", "Temperature", "Run_Time", "Downtime_Flag"}
    if not required_columns.issubset(dataset.columns):
        raise ValueError(f"Dataset must contain columns: {required_columns}")
    return dataset
