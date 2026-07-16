import logging
from data_ingestion import load_book_data, DataIngestionError
from analytics import compute_genre_summary
from visualization import render_genre_chart

logging.basicConfig(level=logging.INFO)


def run_pipeline(csv_path: str):
    try:
        df = load_book_data(csv_path)
        summary = compute_genre_summary(df)
        render_genre_chart(summary, export_path="genre_ratings.png")
    except DataIngestionError as e:
        logging.error("Pipeline aborted: %s", e)


if __name__ == "__main__":
    run_pipeline("config/book_data.csv")  # path now
