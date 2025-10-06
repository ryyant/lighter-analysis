import pandas as pd
from datetime import timezone, timedelta


def convert_timestamp_column(
    df: pd.DataFrame, column: str = "timestamp", unit: str = "ms"
) -> pd.DataFrame:
    """
    Convert the specified timestamp column from a given unit since epoch to
    timezone-aware datetime in UTC+8.

    Args:
        df: Input DataFrame containing the timestamp column.
        column: Name of the timestamp column to convert.
        unit: Unit of the timestamp (e.g., 'ms', 's', 'ns').

    Returns:
        DataFrame with the converted timestamp column.
    """
    tz = timezone(timedelta(hours=8))
    if column in df.columns:
        df[column] = pd.to_datetime(df[column], unit=unit, utc=True).dt.tz_convert(tz)
    return df