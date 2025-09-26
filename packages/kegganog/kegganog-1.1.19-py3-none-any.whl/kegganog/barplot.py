import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, Tuple, Union
import shutil
from pathlib import Path


class KgnBarplot:
    def __init__(self, fig: plt.Figure, ax: plt.Axes):
        self.fig = fig
        self.ax = ax

    def plotfig(self) -> plt.Figure:
        self.fig.tight_layout()
        plt.show()
        return self.fig

    def savefig(self, path: str, dpi: int = 300, bbox_inches: str = "tight"):
        """
        Save the figure to a file.

        Parameters:
        - path: Path to save the figure (e.g. "plot.png", "plot.svg").
        - dpi: Dots per inch (resolution) of the output image. Default is 300.
        - bbox_inches: Bounding box option passed to matplotlib. Default is "tight".
        """
        self.fig.savefig(path, dpi=dpi, bbox_inches=bbox_inches)


def barplot(
    df,
    figsize: Tuple[int, int] = (8, 12),
    cmap: Optional[Union[str, list]] = "Greens",
    cmap_range: Tuple[int, int] = (8, 30),
    title: Optional[str] = None,
    title_fontsize: float = 16.0,
    title_color: str = "black",
    title_weight: str = "normal",
    title_style: str = "normal",
    xlabel: str = "Pathway completeness",
    xlabel_fontsize: float = 14.0,
    xlabel_color: str = "black",
    xlabel_weight: str = "normal",
    xlabel_style: str = "normal",
    ylabel: str = "Pathway",
    ylabel_fontsize: float = 14.0,
    ylabel_color: str = "black",
    ylabel_weight: str = "normal",
    ylabel_style: str = "normal",
    xticks_fontsize: float = 12.0,
    xticks_color: str = "black",
    xtick_weight: str = "normal",
    xtick_style: str = "normal",
    yticks_fontsize: float = 12.0,
    yticks_color: str = "black",
    ytick_weight: str = "normal",
    ytick_style: str = "normal",
    grid: bool = True,
    grid_linestyle: str = "--",
    grid_alpha: float = 0.7,
    background_color: str = "white",
    sort_order: str = "descending",
):
    """
    Generates a customizable horizontal barplot showing pathway completeness.

    Parameters:
    - df: Pandas DataFrame containing the dataset.
    - figsize: Tuple (width, height) of the figure.
    - cmap: Colormap name (str) or list of colors.
    - cmap_range: Tuple (start, end) to subset the colormap.
    - title: Title of the plot.
    - title_fontsize, title_color, title_weight, title_style: Title styling.
    - xlabel, ylabel: Labels for axes.
    - xlabel_fontsize, xlabel_color, xlabel_weight, xlabel_style: X-axis label styling.
    - ylabel_fontsize, ylabel_color, ylabel_weight, ylabel_style: Y-axis label styling.
    - xticks_fontsize, xticks_color, xtick_weight, xtick_style: X-ticks styling.
    - yticks_fontsize, yticks_color, ytick_weight, ytick_style: Y-ticks styling.
    - grid: Whether to show grid lines.
    - grid_linestyle, grid_alpha: Grid styling.
    - background_color: Figure background color.
    - sort_order: "ascending" or "descending" sort of completeness scores.

    Returns:
    - Displays a horizontal barplot of pathway completeness.
    """

    # Load and process data
    df = df.drop(columns=["Function"], errors="ignore")
    df = df.loc[:, (df > 0).any(axis=0)]
    df_melted = df.melt(var_name="Pathway", value_name="Score")

    # Sort by score
    df_melted = df_melted.sort_values(
        by="Score", ascending=(sort_order == "ascending")
    ).reset_index(drop=True)

    # Capitalize lowercase pathway names
    df_melted["Pathway"] = df_melted["Pathway"].apply(
        lambda x: x.capitalize() if isinstance(x, str) and x.islower() else x
    )

    # Set figure
    fig, ax = plt.subplots(figsize=figsize, facecolor=background_color)

    # Color palette
    if isinstance(cmap, str):
        palette = sns.color_palette(cmap, n_colors=cmap_range[1])[cmap_range[0] :]
    else:
        palette = cmap  # Custom list of colors

    sns.barplot(
        data=df_melted,
        x="Score",
        y="Pathway",
        hue="Score",
        palette=palette,
        dodge=False,
        legend=False,
        ax=ax,
    )

    ax.set_title(
        title,
        fontsize=title_fontsize,
        color=title_color,
        weight=title_weight,
        style=title_style,
    )
    ax.set_xlabel(
        xlabel,
        fontsize=xlabel_fontsize,
        color=xlabel_color,
        weight=xlabel_weight,
        style=xlabel_style,
    )
    ax.set_ylabel(
        ylabel,
        fontsize=ylabel_fontsize,
        color=ylabel_color,
        weight=ylabel_weight,
        style=ylabel_style,
    )

    for label in ax.get_xticklabels():
        label.set_fontsize(xticks_fontsize)
        label.set_color(xticks_color)
        label.set_weight(xtick_weight)
        label.set_style(xtick_style)

    for label in ax.get_yticklabels():
        label.set_fontsize(yticks_fontsize)
        label.set_color(yticks_color)
        label.set_weight(ytick_weight)
        label.set_style(ytick_style)

    if grid:
        ax.grid(axis="x", linestyle=grid_linestyle, alpha=grid_alpha, zorder=0)

    ax.invert_yaxis()
    ax.set_xlim(0, 1.0)
    ax.set_axisbelow(True)

    # Get the path to the current directory (same location as the script)
    current_dir = Path(__file__).resolve().parent
    pycache_dir = current_dir / "__pycache__"

    # Check if __pycache__ exists and remove it
    if pycache_dir.exists() and pycache_dir.is_dir():
        shutil.rmtree(pycache_dir)

    plt.close(fig)

    return KgnBarplot(fig, ax)
