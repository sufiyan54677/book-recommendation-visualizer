import pandas as pd
import logging

logger = logging.getLogger("book_viz.analytics")


def compute_genre_summary(df: pd.DataFrame) -> pd.Series:
    """Return mean rating per genre, sorted descending."""
    if df.empty:
        raise ValueError("Cannot summarise an empty dataset")
    summary = df.groupby("genre")["rating"].mean().sort_values(ascending=False)
    logger.info("Computed mean rating for %d genres", len(summary))
    return summary
