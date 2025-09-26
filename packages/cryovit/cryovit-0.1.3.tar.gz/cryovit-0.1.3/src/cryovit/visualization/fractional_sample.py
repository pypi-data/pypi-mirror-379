"""Make plots comparing fractional LOO sample performance."""

import functools
from pathlib import Path

import pandas as pd

from cryovit.visualization.utils import (
    compute_stats,
    merge_experiments,
    significance_test,
)


def _plot_df(
    df: pd.DataFrame,
    pvalues: pd.Series,
    key: str,
    title: str,
    file_name: str,
    plot_points: bool = True,
):
    import matplotlib
    import matplotlib.pyplot as plt
    import seaborn as sns
    from statannotations.Annotator import Annotator

    matplotlib.use("Agg")
    colors = sns.color_palette("deep")[:3]
    sns.set_theme(style="darkgrid", font="Open Sans")

    hue_palette = {
        "3D U-Net": colors[0],
        "CryoViT": colors[1],
    }

    figsize = (20, 6) if "Mito" in title else (10, 6)
    fig = plt.figure(figsize=figsize)
    ax = plt.gca()
    df["split_id"] = df["split_id"].astype(int)
    label_counts = df["split_id"].value_counts()
    num_models = df[key].nunique()

    params = {
        "x": "split_id",
        "y": "dice_metric",
        "hue": key,
        "data": df,
    }

    if plot_points:
        sns.boxplot(
            showfliers=False,
            palette=hue_palette,
            linewidth=1,
            medianprops={"linewidth": 2, "color": "firebrick"},
            ax=ax,
            **params,
        )
        sns.stripplot(
            dodge=True,
            marker=".",
            alpha=0.5,
            palette="dark:black",
            ax=ax,
            **params,
        )

        k1, k2 = df[key].unique()
        pairs = [[(s, k1), (s, k2)] for s in pvalues.index]

        annotator = Annotator(ax, pairs, **params)
        annotator.configure(color="blue", line_width=1, verbose=False)
        annotator.set_pvalues_and_annotate(pvalues.values)
    else:
        sns.lineplot(
            marker="o",
            markersize=8,
            linewidth=2,
            palette=hue_palette,
            ax=ax,
            **params,
        )
        ax.set_xticks(df["split_id"].unique())

    current_labels = ax.get_xticklabels()
    new_labels = [f"{label.get_text()}0%" for label in current_labels]
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(new_labels, ha="center")

    ax.set_ylim(-0.05, 1.15)
    ax.set_xlabel("")
    ax.set_ylabel("")

    fig.suptitle(title)
    fig.supxlabel(
        f"Fraction of Training Data\n(n={label_counts[10] // num_models})"
    )
    fig.supylabel("Dice Score")

    handles, labels = ax.get_legend_handles_labels()
    plt.legend(handles[:2], labels[:2], loc="lower center", shadow=True)

    plt.tight_layout()
    plt.savefig(f"{file_name}{'_line' if not plot_points else ''}.svg")
    plt.savefig(
        f"{file_name}{'_line' if not plot_points else ''}.png", dpi=300
    )


def process_fractional_experiment(
    exp_type: str,
    label: str,
    exp_names: dict[str, list[str]],
    exp_dir: Path,
    result_dir: Path,
    plot_points: bool = True,
):
    """Plot fractional experiment results with box and strip plots including annotations for statistical tests.

    Args:
        exp_type (str): Type of experiment, e.g., "fractional", "sparse"
        label (str): The label being analyzed, e.g., "mito", "cristae"
        exp_names (dict[str, list[str]]): Dictionary mapping experiment names to model used
        exp_dir (Path): Directory containing the experiment results
        result_dir (Path): Directory to save the results
    """

    df = merge_experiments(exp_dir, exp_names, keys=["model"])
    test_fn = functools.partial(
        significance_test,
        model_A=("CryoViT"),
        model_B=("3D U-Net"),
        key="model",
        test_fn="ttest_rel",
    )
    full_labels = {
        "mito": "Mitochondria",
        "cristae": "Cristae",
        "microtubule": "Microtubules",
        "granule": "Granules",
        "bacteria": "Bacteria",
    }
    p_values = compute_stats(
        df,
        group_keys=["split_id", "model"],
        file_name=str(result_dir / f"{label}_{exp_type}_stats.csv"),
        test_fn=test_fn,
    )
    _plot_df(
        df,
        p_values,
        "model",
        f"Fractional Model Comparison for {full_labels[label]}",
        str(result_dir / f"{label}_{exp_type}_comparison"),
        plot_points=plot_points,
    )
