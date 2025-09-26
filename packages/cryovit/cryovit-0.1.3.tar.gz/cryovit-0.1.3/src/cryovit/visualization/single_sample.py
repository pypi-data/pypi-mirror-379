"""Make plots comparing single sample performance."""

import functools
from pathlib import Path

import pandas as pd

from cryovit.types import Sample
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
    ax,
):
    # import here to avoid unnecessary dependencies if function not used
    import matplotlib
    import seaborn as sns
    from statannotations.Annotator import Annotator

    matplotlib.use("Agg")
    colors = sns.color_palette("deep")[:2]
    sns.set_theme(style="darkgrid", font="Open Sans")

    hue_palette = {
        "3D U-Net": colors[0],
        "CryoViT": colors[1],
    }

    sample_counts = df["sample"].value_counts()
    num_models = df[key].nunique()
    sorted_samples = sample_counts.sort_values(ascending=True).index.tolist()

    params = {
        "x": "sample",
        "y": "dice_metric",
        "hue": key,
        "data": df,
        "order": sorted_samples,
    }

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

    current_labels = ax.get_xticklabels()
    new_labels = [
        f"{Sample[label.get_text()].value}\n(n={sample_counts[label.get_text()] // num_models})"
        for label in current_labels
    ]

    ax.set_ylim(-0.05, 1.15)
    ax.set_title(title)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xticks(range(len(new_labels)))
    ax.set_xticklabels(new_labels, ha="center")

    handles, labels = ax.get_legend_handles_labels()
    if title == "HD":
        ax.legend(handles[:2], labels[:2], loc="lower center", shadow=True)
    else:
        ax.legend().remove()
    return handles, labels


def process_single_experiment(
    exp_type: str,
    exp_group: str,
    exp_names: dict[str, dict[str, list[str]]],
    exp_dir: Path,
    result_dir: Path,
):
    """Plot single sample experiment results with box and strip plots including annotations for statistical tests.

    Args:
        exp_type (str): Type of experiment, e.g. "sparse"
        exp_group (str): Group of experiments, e.g. "hd", "ad"
        exp_names (dict[str, dict[str, list[str]]]): Dictionary mapping experiment groups to experiment names and models
        exp_dir (Path): Directory containing experiment results
        result_dir (Path): Directory to save results
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set_theme(style="darkgrid", font="Open Sans")

    result_dir.mkdir(parents=True, exist_ok=True)
    dfs = {
        group: merge_experiments(exp_dir, exp_names[group], keys=["model", "group"])  # type: ignore
        for group in exp_names
    }
    exp_counts = [df["sample"].nunique() for df in dfs.values()]
    fig, axes = plt.subplots(
        1,
        len(dfs),
        figsize=(20, 6),
        sharey="row",
        gridspec_kw={"width_ratios": exp_counts},
    )

    for ax, (group, df) in zip(axes, dfs.items(), strict=True):
        test_fn = functools.partial(
            significance_test,
            model_A=("CryoViT"),
            model_B=("3D U-Net"),
            key="model",
            test_fn="wilcoxon",
        )
        p_values = compute_stats(
            df,
            group_keys=["sample", "model"],
            file_name=str(
                result_dir / f"{group.lower()}_{exp_type}_stats.csv"
            ),
            test_fn=test_fn,
        )
        title = f"{group}"
        _plot_df(
            df,
            p_values,
            "model",
            title,
            ax,
        )

    # Adjust layout and save the figure
    fig.suptitle("Model Comparison on Individual Samples for Mitochondria")
    fig.supxlabel("Sample Name (Count)")
    fig.supylabel("Dice Score")

    plt.tight_layout(rect=(0.01, 0.01, 1.0, 1.0))
    plt.savefig(result_dir / f"{exp_group.lower()}_{exp_type}.svg")
    plt.savefig(result_dir / f"{exp_group.lower()}_{exp_type}.png", dpi=300)
