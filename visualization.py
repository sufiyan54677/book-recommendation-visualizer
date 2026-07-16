import matplotlib.pyplot as plt
import logging

logger = logging.getLogger("book_viz.visualization")


def render_genre_chart(genre_summary, export_path: str = None):
    """Render (and optionally export) the mean-rating-by-genre bar chart."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(genre_summary.index, genre_summary.values, color="skyblue")
    ax.set_title("Average Book Rating by Genre")
    ax.set_xlabel("Genre")
    ax.set_ylabel("Mean Rating (1-5)")

    if export_path:
        fig.savefig(export_path, dpi=150, bbox_inches="tight")
        logger.info("Chart exported to %s", export_path)
    return fig
