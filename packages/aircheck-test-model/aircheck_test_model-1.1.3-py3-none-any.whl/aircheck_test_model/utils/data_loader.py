import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq
from dataclasses import dataclass
from tqdm.auto import tqdm
from pathlib import Path

FINGERPRINT_TYPES = [
    "ATOMPAIR",
    "MACCS",
    "ECFP6",
    "ECFP4",
    "FCFP4",
    "FCFP6",
    "TOPTOR",
    "RDK",
    "AVALON",
]
INDEX_COL = "RandomID"
TARGET_COL = "LABEL"
FLOAT_COLS = ["MW", "ALOGP"]
FINGERPRINT_COLS = FINGERPRINT_TYPES


def parquet_dataloader(filename, x_col, y_col=None, batch_size=1000):
    pf = pa.parquet.ParquetFile(filename)
    columns = [x_col] + ([y_col] if y_col is not None else [])
    for batch in pf.iter_batches(columns=columns, batch_size=batch_size):
        df = pa.Table.from_batches([batch]).to_pandas()
        # Use string splitting for X, as in basic_dataloader
        X = df[x_col].str.split(",", expand=True).astype(float, copy=False).values
        if y_col is not None:
            y = df[y_col].values
        else:
            y = None
        yield X, y


@dataclass
class Dataset:
    """Basic dataset class holding a dataset."""

    x_col: str
    filename: str | Path
    y_col: str = "LABEL"
    test: bool = False
    X: np.ndarray = None
    y: np.ndarray = None

    def __post_init__(self):
        if self.x_col not in FINGERPRINT_TYPES:
            raise ValueError("Invalid fingerprint type")

        if self.test:
            df = pd.read_parquet(self.filename, columns=[self.x_col])
            self.y = None
        else:
            df = pd.read_parquet(self.filename, columns=[self.x_col, self.y_col])
            self.y = df[self.y_col].values
            df = df.drop(columns=[self.y_col])
            if not np.all(np.isin(self.y, [0, 1])):
                raise ValueError("y must contain only binary labels (0 or 1)")

        # first_row = np.fromstring(
        #     df[self.x_col].iloc[0], sep=",", dtype=np.float32)
        # self.X = np.empty((len(df), len(first_row)), dtype=np.float32)
        self.X = np.stack(df[self.x_col].apply(lambda x: np.array(x, dtype=np.float32)))
        # for i, x in enumerate(df[self.x_col].values):
        #     self.X[i, :] = np.fromstring(x, sep=",", dtype=np.float32)

        invalid_mask = np.isnan(self.X).any(axis=1)
        invalid_rows = np.where(invalid_mask)[0]
        if len(invalid_rows) > 0:
            print(f"Warning: Found {len(invalid_rows)} invalid rows in dataset")

        del df


def calculate_np_memory(shape, dtype=np.float32):
    """
    Calculates the memory in GB for the data buffer of a NumPy array
    given its shape and dtype.
    """
    num_elements = np.prod(shape)
    item_size = np.dtype(dtype).itemsize
    memory_in_bytes = num_elements * item_size
    return memory_in_bytes / (1024**3)


def calculate_feature_dims(features, dims):
    """
    Calculates the start and end indices for each feature in a stacked array.
    """
    stacked_map = {}
    offset = 0
    for c, dim in zip(features, dims):
        start_index = offset
        end_index = offset + dim
        stacked_map[c] = (start_index, end_index)
        offset += dim
    return stacked_map


def get_feature_dims(parquet_file, features: list[str]) -> list[int]:
    """Return the dimensions of the features."""
    first_row = next(parquet_file.iter_batches(batch_size=1)).to_pandas().iloc[0]
    dims = []
    for c in features:
        if c in FINGERPRINT_COLS:
            dims.append(len(np.array(first_row[c].split(","), dtype=np.float32)))
        elif c in FLOAT_COLS:
            dims.append(1)

    return dims


def parse_pyarrow_string_array(str_arr):
    """
    Parses a PyArrow StringArray into a 2D NumPy array."""
    list_str_arr = pc.split_pattern(str_arr, pattern=",")
    flat_str_values = list_str_arr.values
    flat_float_values = pc.cast(flat_str_values, pa.float32(), safe=False)
    list_float_arr = pa.ListArray.from_arrays(list_str_arr.offsets, flat_float_values)
    arr = list_float_arr.to_numpy(zero_copy_only=False)
    # n_rows = len(list_float_arr)
    # dim = len(flat_float_values) // n_rows
    return np.vstack(arr)


def load_y(filename: str, y_col: str = "DELLabel", batch_size=1000) -> np.ndarray:
    """Loads label features from a Parquet file."""
    parquet_file = pq.ParquetFile(filename)
    pq_iter = parquet_file.iter_batches(batch_size=batch_size)
    values = []
    for record_batch in pq_iter:
        values.append(record_batch.column(y_col).to_numpy(np.float32))
    return np.hstack(values).reshape(-1, 1)


def load_x(filename: str, x_cols: list[str], return_index=False, batch_size=1000) -> np.ndarray:
    """Loads input features from a Parquet file."""
    parquet_file = pq.ParquetFile(filename)
    n_rows = parquet_file.metadata.num_rows
    print(f"Total rows: {n_rows}")
    feat_dims = get_feature_dims(parquet_file, x_cols)
    n_dim = sum(feat_dims)
    n_chunks = n_rows // batch_size + 1
    print(f"Expected Memory for inputs: {calculate_np_memory((n_rows, n_dim)):.2f} GBs")
    feature_dims = calculate_feature_dims(x_cols, feat_dims)
    pq_iter = parquet_file.iter_batches(batch_size=batch_size, columns=None)
    x = np.zeros((n_rows, n_dim), dtype=np.float32)
    index = []
    for i, record_batch in tqdm(enumerate(pq_iter), total=n_chunks):
        x_start = i * batch_size
        x_end = min((i + 1) * batch_size, n_rows)
        x_slice = slice(x_start, x_end)
        if return_index:
            index.extend(record_batch.column(INDEX_COL).tolist())
        for c in x_cols:
            f_slice = slice(*feature_dims[c])
            chunked_arr = record_batch.column(c)
            if c in FINGERPRINT_COLS:
                values = parse_pyarrow_string_array(chunked_arr)
            else:
                values = chunked_arr.to_numpy(zero_copy_only=False).reshape(-1, 1)
            x[x_slice, f_slice] = values
    if return_index:
        return index, x
    else:
        return x
