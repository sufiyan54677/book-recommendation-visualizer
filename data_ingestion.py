import pandas as pd
import logging

logger = logging.getLogger("book_viz.ingestion")

REQUIRED_COLUMNS = {"genre", "rating"}


class DataIngestionError(Exception):
    pass


def load_book_data(csv_path: str) -> pd.DataFrame:
    """Load and structurally validate the book ratings CSV."""
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        logger.error("CSV not found at %s", csv_path)
        raise DataIngestionError(f"File not found: {csv_path}")
    except pd.errors.EmptyDataError:
        logger.error("CSV at %s is empty", csv_path)
        raise DataIngestionError("The CSV file contains no data")

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise DataIngestionError(f"Missing required column(s): {missing}")

    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    dropped = df["rating"].isna().sum()
    if dropped:
        logger.warning("Dropping %d rows with non-numeric/missing rating", dropped)
    df = df.dropna(subset=["rating", "genre"])

    logger.info("Loaded %d valid rows from %s", len(df), csv_path)
    return df
