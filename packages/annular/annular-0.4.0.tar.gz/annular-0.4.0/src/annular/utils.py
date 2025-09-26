from pathlib import Path

import pandas as pd


def read_csv_with_utc_timestamps(path: Path | str) -> pd.DataFrame:
    """Load a CSV file, using column 0 as index, and converting the index to UTC timestamps.

    Args:
        path: Path to the CSV file.

    Returns:
        DataFrame of the CSV file with index as UTC timestamps.
    """
    df = pd.read_csv(path, index_col=0)
    df.index = pd.to_datetime(df.index, utc=True)
    return df
