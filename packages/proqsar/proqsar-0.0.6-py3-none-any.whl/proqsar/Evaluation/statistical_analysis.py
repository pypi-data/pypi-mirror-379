import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pingouin as pg
import seaborn as sns
import math
import os
import warnings
from copy import deepcopy
from scipy import stats
from scipy.stats import levene
from statsmodels.stats.anova import AnovaRM
from statsmodels.stats.libqsturng import psturng, qsturng
from typing import Optional, Union, Tuple, List, Dict
import scikit_posthocs as sp
import logging


class StatisticalAnalysis:
    """
    Static utilities for statistical evaluation of model scoring results.

    Provides methods for:
      - extracting and reshaping scoring DataFrames,
      - testing assumptions (homogeneity of variance, normality),
      - parametric (ANOVA + Tukey HSD) and non-parametric (Friedman + Conover) tests,
      - posthoc analyses with visualization,
      - and high-level convenience pipelines.

    .. note::
       This class is stateless: all methods are static and operate directly on
       pandas DataFrames passed in.

    :ivar None: This class is intentionally stateless; no attributes are stored.
    """

    @staticmethod
    def extract_scoring_dfs(
        report_df: pd.DataFrame,
        scoring_list: Optional[Union[list, str]] = None,
        method_list: Optional[Union[list, str]] = None,
        melt: bool = False,
    ) -> Tuple[pd.DataFrame, List[str], List[str]]:
        """
        Extract and optionally reshape scoring data.

        :param report_df: Input DataFrame containing at least columns ``['scoring','cv_cycle',...]``.
        :type report_df: pandas.DataFrame
        :param scoring_list: One or more metrics to extract. If None, all unique ``report_df['scoring']`` are used.
        :type scoring_list: Optional[Union[list, str]]
        :param method_list: One or more method column names to include. If None, all except ``scoring``
        and ``cv_cycle``.
        :type method_list: Optional[Union[list, str]]
        :param melt: If True, returns a long-format DataFrame with ``['scoring','cv_cycle','method','value']``.
        :type melt: bool
        :return: Tuple of (scoring_dfs, scoring_list, method_list)
        :rtype: Tuple[pandas.DataFrame, List[str], List[str]]
        :raises ValueError: If a provided scoring metric is not present in the DataFrame.
        :raises Exception: If unexpected errors occur.
        """
        try:
            # Normalize scoring_list input to list
            if isinstance(scoring_list, str):
                scoring_list = [scoring_list]

            if scoring_list is None:
                scoring_list = report_df["scoring"].unique()

            # Normalize method_list input to list
            if isinstance(method_list, str):
                method_list = [method_list]

            if method_list is None:
                method_list = report_df.drop(
                    columns=["scoring", "cv_cycle"]
                ).columns.tolist()

            scoring_list = [scoring.lower() for scoring in scoring_list]

            filtered_dfs = []

            for scoring in scoring_list:
                if scoring not in report_df["scoring"].unique():
                    raise ValueError(f"Invalid scoring value: {scoring}.")
                score_df = deepcopy(report_df[report_df["scoring"] == scoring])
                score_df = score_df[
                    ["scoring", "cv_cycle"] + method_list
                ]  # Select only the columns in method_list
                filtered_dfs.append(score_df)

            scoring_dfs = pd.concat(filtered_dfs)
            # exclude aggregated rows
            scoring_dfs = scoring_dfs[
                ~scoring_dfs["cv_cycle"].isin(["mean", "median", "std"])
            ]
            scoring_dfs = scoring_dfs.sort_index(axis=0).sort_index(axis=1)

            # Melt the dataframe to long format
            if melt:
                scoring_dfs = scoring_dfs.melt(
                    id_vars=["scoring", "cv_cycle"],
                    var_name="method",
                    value_name="value",
                )
            return scoring_dfs, scoring_list, method_list

        except Exception as e:
            logging.error(f"Error in extracting scoring DataFrames: {e}")
            raise

    @staticmethod
    def check_variance_homogeneity(
        report_df: pd.DataFrame,
        scoring_list: Optional[Union[list, str]] = None,
        method_list: Optional[Union[list, str]] = None,
        levene_test: bool = True,
        save_csv: bool = False,
        save_dir: str = "Project/Analysis",
        csv_name: str = "check_variance_homogeneity",
    ) -> pd.DataFrame:
        """
        Assess homogeneity of variance across methods for each metric.

        :param report_df: Input scoring DataFrame.
        :type report_df: pandas.DataFrame
        :param scoring_list: Metrics to check. If None, all are used.
        :type scoring_list: Optional[Union[list, str]]
        :param method_list: Methods to include. If None, all available methods.
        :type method_list: Optional[Union[list, str]]
        :param levene_test: If True, include Levene's test p-values.
        :type levene_test: bool
        :param save_csv: If True, save results to CSV.
        :type save_csv: bool
        :param save_dir: Directory for saved results.
        :type save_dir: str
        :param csv_name: Base name for saved CSV.
        :type csv_name: str
        :return: DataFrame indexed by scoring metric, with columns ``['variance_fold_difference','p_value']``.
        :rtype: pandas.DataFrame
        """
        try:
            report_new, scoring_list, method_list = (
                StatisticalAnalysis.extract_scoring_dfs(
                    report_df=report_df,
                    scoring_list=scoring_list,
                    method_list=method_list,
                    melt=True,
                )
            )

            if not method_list or len(method_list) == 1:
                logging.info(
                    "StatisticalAnalysis: Only one method provided. Skipping statistical test."
                )
                return None

            result = []

            for scoring in scoring_list:
                # Filter data for the current metric
                scoring_data = report_new[report_new["scoring"] == scoring]

                # Calculate variance fold difference
                variances_by_method = scoring_data.groupby("method")["value"].var()
                max_fold_diff = variances_by_method.max() / variances_by_method.min()

                scoring_result = {
                    "scoring": scoring,
                    "variance_fold_difference": max_fold_diff,
                }
                # Perform Levene's test if specified
                p_value = None
                if levene_test:
                    groups = [
                        group["value"].values
                        for _, group in scoring_data.groupby("method")
                    ]
                    stat, p_value = levene(*groups)
                    scoring_result["p_value"] = p_value

                result.append(scoring_result)

            result_df = pd.DataFrame(result).set_index("scoring")

            if save_csv:
                if save_dir and not os.path.exists(save_dir):
                    os.makedirs(save_dir, exist_ok=True)
                result_df.to_csv(f"{save_dir}/{csv_name}.csv", index=True)

            return result_df

        except Exception as e:
            logging.error(f"Error in checking variance homogeneity: {e}")
            raise

    @staticmethod
    def check_normality(
        report_df: pd.DataFrame,
        scoring_list: Optional[Union[list, str]] = None,
        method_list: Optional[Union[list, str]] = None,
        save_fig: bool = True,
        save_dir: str = "Project/Analysis",
        fig_name: str = "check_normality",
    ) -> None:
        """
        Plot histograms and Q–Q plots to visually assess normality of scores.

        :param report_df: Input DataFrame with scoring and method columns.
        :type report_df: pandas.DataFrame
        :param scoring_list: Metrics to plot. If None, all are used.
        :type scoring_list: Optional[Union[list, str]]
        :param method_list: Methods to include. If None, all available methods.
        :type method_list: Optional[Union[list, str]]
        :param save_fig: Save figure as PDF when True.
        :type save_fig: bool
        :param save_dir: Directory where figures are saved.
        :type save_dir: str
        :param fig_name: Base filename (without extension) for saved figure.
        :type fig_name: str
        :return: None
        :rtype: None
        :raises Exception: If plotting or saving fails.
        """
        try:
            report_new, scoring_list, _ = StatisticalAnalysis.extract_scoring_dfs(
                report_df=report_df,
                scoring_list=scoring_list,
                method_list=method_list,
                melt=True,
            )

            # Normalize values by subtracting the mean for each method
            df_norm = deepcopy(report_new)
            df_norm["value"] = df_norm.groupby(["method", "scoring"])[
                "value"
            ].transform(lambda x: x - x.mean())

            sns.set_context("notebook")
            sns.set_style("whitegrid")

            fig, axes = plt.subplots(
                2, len(scoring_list), figsize=(5 * len(scoring_list), 10)
            )

            # Ensure axes is 2D for consistent indexing when len(scoring_list) == 1
            if not isinstance(axes, np.ndarray):
                axes = np.array(axes)
            if axes.ndim == 1:
                axes = axes.reshape(2, 1)

            for i, scoring in enumerate(scoring_list):
                ax = axes[0, i]
                scoring_data = df_norm[df_norm["scoring"] == scoring]["value"]
                sns.histplot(scoring_data, kde=True, ax=ax, bins=10)
                ax.set_title(f"{scoring.upper()}", fontsize=16)

                ax2 = axes[1, i]
                stats.probplot(scoring_data, dist="norm", plot=ax2)
                ax2.set_title("")

            plt.tight_layout()
            if save_fig:
                if save_dir and not os.path.exists(save_dir):
                    os.makedirs(save_dir, exist_ok=True)
                plt.savefig(
                    f"{save_dir}/{fig_name}.pdf",
                    dpi=300,
                    bbox_inches="tight",
                )

        except Exception as e:
            logging.error(f"Error in checking normality: {e}")
            raise

    @staticmethod
    def test(
        report_df: pd.DataFrame,
        scoring_list: Optional[Union[list, str]] = None,
        method_list: Optional[list] = None,
        select_test: str = "AnovaRM",
        showmeans: bool = True,
        save_fig: bool = True,
        save_dir: str = "Project/Analysis",
        fig_name: Optional[str] = None,
    ) -> None:
        """
        Perform statistical tests (repeated-measures ANOVA or Friedman).

        Produces annotated boxplots per metric with p-values.

        :param report_df: Melted DataFrame with columns ['scoring','cv_cycle','method','value'].
        :type report_df: pandas.DataFrame
        :param scoring_list: Metrics to test.
        :type scoring_list: Optional[Union[list, str]]
        :param method_list: Methods to compare. If len <= 1, skipped.
        :type method_list: Optional[list]
        :param select_test: 'AnovaRM' (parametric) or 'friedman' (non-parametric).
        :type select_test: str
        :param showmeans: Whether to show means on boxplots.
        :type showmeans: bool
        :param save_fig: Save figure to file when True.
        :type save_fig: bool
        :param save_dir: Directory to save plots.
        :type save_dir: str
        :param fig_name: Filename (defaults to ``select_test`` if None).
        :type fig_name: Optional[str]
        :return: None
        :rtype: None
        :raises ValueError: If `select_test` is invalid.
        """
        try:
            report_new, scoring_list, method_list = (
                StatisticalAnalysis.extract_scoring_dfs(
                    report_df=report_df,
                    scoring_list=scoring_list,
                    method_list=method_list,
                    melt=True,
                )
            )
            # If only one method is provided, skip the test.
            if not method_list or len(method_list) == 1:
                logging.info("Only one method provided. Skipping statistical test.")
                return

            if select_test not in ["AnovaRM", "friedman"]:
                raise ValueError(
                    f"Unsupported test: {select_test}."
                    "Please choose 'AnovaRM' for a parametric test or 'friedman' for a non-parametric test."
                )

            sns.set_context("notebook")
            sns.set_style("whitegrid")

            nrow = math.ceil(len(scoring_list) / 2)
            nmethod = len(method_list)

            figure, axes = plt.subplots(
                nrow, 2, sharex=False, sharey=False, figsize=(3 * nmethod, 7 * nrow)
            )
            axes = axes.flatten()  # Turn 2D array to 1D array

            for i, scoring in enumerate(scoring_list):
                scoring_data = report_new[report_new["scoring"] == scoring]
                if select_test == "AnovaRM":
                    model = AnovaRM(
                        data=scoring_data,
                        depvar="value",
                        subject="cv_cycle",
                        within=["method"],
                    ).fit()
                    p_value = model.anova_table["Pr > F"].iloc[0]

                else:
                    p_value = pg.friedman(
                        data=scoring_data,
                        dv="value",
                        within="method",
                        subject="cv_cycle",
                    )["p-unc"].values[0]

                ax = sns.boxplot(
                    y="value",
                    x="method",
                    hue="method",
                    ax=axes[i],
                    showmeans=showmeans,
                    data=scoring_data,
                    palette="plasma",
                    legend=False,
                    width=0.5,
                )
                ax.set_title(f"p={p_value:.1e}", fontsize=16)
                ax.set_xlabel("")
                ax.set_ylabel(scoring.upper())

                # Wrap labels
                labels = [item.get_text() for item in ax.get_xticklabels()]
                new_labels = []
                for label in labels:
                    if "Regression" in label:
                        new_label = label.replace("Regression", "\nRegression")
                    elif "Regressor" in label:
                        new_label = label.replace("Regressor", "\nRegressor")
                    elif "Classifier" in label:
                        new_label = label.replace("Classifier", "\nClassifier")
                    else:
                        new_label = label
                    new_labels.append(new_label)

                ax.set_xticks(list(range(0, len(labels))))
                ax.set_xticklabels(new_labels)
                ax.tick_params(axis="both", labelsize=12)

            # If there are less plots than cells in the grid, hide the remaining cells
            if (len(scoring_list) % 2) != 0:
                for i in range(len(scoring_list), nrow * 2):
                    axes[i].set_visible(False)

            plt.tight_layout()

            fig_name = fig_name or select_test
            if save_fig:
                if save_dir and not os.path.exists(save_dir):
                    os.makedirs(save_dir, exist_ok=True)
                plt.savefig(
                    f"{save_dir}/{fig_name}.pdf",
                    dpi=300,
                    bbox_inches="tight",
                )
            logging.info(
                f"StatisticalAnalysis: Figure saved at {save_dir}/{fig_name}.pdf"
            )

        except Exception as e:
            logging.error(f"An error occurred during the test: {e}")
            raise

    @staticmethod
    def posthoc_conover_friedman(
        report_df: pd.DataFrame,
        scoring_list: Optional[Union[list, str]] = None,
        method_list: Optional[list] = None,
        plot: Optional[Union[list, str]] = None,
        axis_text_size: float = 12,
        title_size: float = 16,
        save_fig: bool = True,
        save_result: bool = True,
        save_dir: str = "Project/Analysis",
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, pd.Series]]:
        """
        Run Conover posthoc tests after Friedman, with plots.

        :param report_df: Input DataFrame (wide or melted).
        :type report_df: pandas.DataFrame
        :param scoring_list: Metrics to test.
        :type scoring_list: Optional[Union[list, str]]
        :param method_list: Methods to compare.
        :type method_list: Optional[list]
        :param plot: Plot types: 'sign', 'ccd', or both.
        :type plot: Optional[Union[list, str]]
        :param axis_text_size: Axis tick font size.
        :type axis_text_size: float
        :param title_size: Title font size.
        :type title_size: float
        :param save_fig: Save figures when True.
        :type save_fig: bool
        :param save_result: Save results as CSV when True.
        :type save_result: bool
        :param save_dir: Directory to save results.
        :type save_dir: str
        :return: Tuple of two dicts:
            - pc_results: metric -> pairwise adjusted p-values (DataFrame)
            - rank_results: metric -> average ranks (Series)
        :rtype: Tuple[Dict[str, pd.DataFrame], Dict[str, pd.Series]]
        """
        try:
            report_new, scoring_list, method_list = (
                StatisticalAnalysis.extract_scoring_dfs(
                    report_df=report_df,
                    scoring_list=scoring_list,
                    method_list=method_list,
                    melt=False,
                )
            )
            # If only one method is provided, skip the test.
            if not method_list or len(method_list) == 1:
                logging.info(
                    "StatisticalAnalysis: Only one method provided. Skipping statistical test."
                )
                return None, None

            # Precompute posthoc Conover-Friedman results for each metric
            pc_results = {}
            rank_results = {}

            for scoring in scoring_list:
                scoring_df_filtered = report_new[report_new["scoring"] == scoring]
                scoring_df_filtered = scoring_df_filtered.drop(
                    columns="scoring"
                ).set_index("cv_cycle")
                pc_results[scoring] = sp.posthoc_conover_friedman(
                    scoring_df_filtered, p_adjust="holm"
                )
                # Compute the mean rank for each method
                rank_results[scoring] = scoring_df_filtered.rank(
                    axis=1, method="average", pct=True
                ).mean(axis=0)

                if save_result:
                    if save_dir and not os.path.exists(save_dir):
                        os.makedirs(save_dir, exist_ok=True)
                    pc_results[scoring].to_csv(
                        f"{save_dir}/cofried_pc_{scoring}.csv", index=False
                    )
                    logging.info(
                        "StatisticalAnalysis: Posthoc Conover-Friedman results saved at"
                        + f" {save_dir}/cofried_pc_{scoring}.csv"
                    )

            if not plot:
                plot = ["sign", "ccd"]
            elif isinstance(plot, str):
                plot = [plot]

            for type in plot:
                if type not in ["sign", "ccd"]:
                    raise ValueError(
                        f"Invalid plot type: {type}. Please choose 'sign' or 'ccd'."
                    )
                if type == "sign":
                    StatisticalAnalysis._make_sign_plots(
                        pc_results=pc_results,
                        scoring_list=scoring_list,
                        axis_text_size=axis_text_size,
                        title_size=title_size,
                        save_fig=save_fig,
                        save_dir=save_dir,
                    )

                if type == "ccd":
                    StatisticalAnalysis._make_critical_difference_diagrams(
                        pc_results=pc_results,
                        rank_results=rank_results,
                        scoring_list=scoring_list,
                        axis_text_size=axis_text_size,
                        title_size=title_size,
                        save_fig=save_fig,
                        save_dir=save_dir,
                    )

            return pc_results, rank_results

        except Exception as e:
            logging.error(
                f"An error occurred during the posthoc Conover-Friedman analysis: {e}"
            )

            return {}, {}

    def _make_sign_plots(
        pc_results: dict,
        scoring_list: list,
        axis_text_size: float = 12,
        title_size: float = 16,
        save_fig: bool = True,
        save_dir: str = "Project/Analysis",
    ) -> None:
        """
        Internal: create significance heatmaps from Conover-Friedman results.

        :param pc_results: Mapping metric -> p-values DataFrame.
        :type pc_results: dict
        :param scoring_list: Ordered list of metrics.
        :type scoring_list: list
        :param axis_text_size: Axis font size.
        :type axis_text_size: float
        :param title_size: Title font size.
        :type title_size: float
        :param save_fig: Save figure when True.
        :type save_fig: bool
        :param save_dir: Directory to save plots.
        :type save_dir: str
        :return: None
        :rtype: None
        """
        heatmap_args = {
            "linewidths": 0.25,
            "linecolor": "black",
            "clip_on": True,
            "square": True,
        }
        sns.set_context("notebook")
        sns.set_style("whitegrid")

        figure, axes = plt.subplots(
            1,
            len(scoring_list),
            sharex=False,
            sharey=True,
            figsize=(6 * len(scoring_list), 10),
        )

        if not isinstance(axes, np.ndarray):
            axes = np.array([axes])

        for i, scoring in enumerate(scoring_list):
            pc = pc_results[scoring]
            sub_ax, sub_c = sp.sign_plot(
                pc, **heatmap_args, ax=axes[i], xticklabels=True
            )
            sub_ax.tick_params(labelsize=axis_text_size)
            sub_ax.set_title(scoring.upper(), fontsize=title_size)

        if save_fig:
            if save_dir and not os.path.exists(save_dir):
                os.makedirs(save_dir, exist_ok=True)
            plt.savefig(
                f"{save_dir}/cofried_sign_plot.pdf",
                dpi=300,
                bbox_inches="tight",
            )
            logging.info(
                f"StatisticalAnalysis: Sign plots saved at {save_dir}/cofried_sign_plot.pdf"
            )

    def _make_critical_difference_diagrams(
        pc_results: dict,
        rank_results: dict,
        scoring_list: list,
        axis_text_size: float = 12,
        title_size: float = 16,
        save_fig: bool = True,
        save_dir: str = "Project/Analysis",
    ) -> None:
        """
        Internal: draw critical difference diagrams per metric.

        :param pc_results: Mapping metric -> pairwise p-values.
        :type pc_results: dict
        :param rank_results: Mapping metric -> average ranks.
        :type rank_results: dict
        :param scoring_list: Ordered list of metrics.
        :type scoring_list: list
        :param axis_text_size: Axis font size.
        :type axis_text_size: float
        :param title_size: Title font size.
        :type title_size: float
        :param save_fig: Save plots when True.
        :type save_fig: bool
        :param save_dir: Directory to save figures.
        :type save_dir: str
        """
        sns.set_context("notebook")
        sns.set_style("whitegrid")
        figure, axes = plt.subplots(
            len(scoring_list),
            1,
            sharex=True,
            sharey=False,
            figsize=(20, 3 * len(scoring_list)),
        )
        if not isinstance(axes, np.ndarray):
            axes = np.array([axes])

        for i, scoring in enumerate(scoring_list):
            pc = pc_results[scoring]
            avg_rank = rank_results[scoring]
            sp.critical_difference_diagram(
                avg_rank, pc, ax=axes[i], label_props={"fontsize": axis_text_size}
            )
            axes[i].set_title(scoring.upper(), fontsize=title_size)
            axes[i].tick_params(labelsize=axis_text_size)

        plt.tight_layout()
        if save_fig:
            if save_dir and not os.path.exists(save_dir):
                os.makedirs(save_dir, exist_ok=True)
            plt.savefig(
                f"{save_dir}/cofried_ccd.pdf",
                dpi=300,
                bbox_inches="tight",
            )
            logging.info(
                f"StatisticalAnalysis: Critical difference diagrams saved at {save_dir}/cofried_ccd.pdf"
            )

    @staticmethod
    def posthoc_tukeyhsd(
        report_df: pd.DataFrame,
        scoring_list: Optional[Union[list, str]] = None,
        method_list: Optional[list] = None,
        plot: Optional[Union[list, str]] = None,
        alpha: float = 0.05,
        direction_dict: dict = {},
        effect_dict: dict = {},
        title_size: float = 16,
        cell_text_size: float = 12,
        axis_text_size: float = 12,
        left_xlim: float = -0.5,
        right_xlim: float = 0.5,
        save_fig: bool = True,
        save_result: bool = True,
        save_dir: str = "Project/Analysis",
    ) -> Dict[str, Dict[str, pd.DataFrame]]:
        """
        Perform Tukey HSD posthoc comparisons for repeated-measures data.

        :param report_df: Input DataFrame (wide or melted).
        :type report_df: pandas.DataFrame
        :param scoring_list: Metrics to test.
        :type scoring_list: Optional[Union[list, str]]
        :param method_list: Methods to compare.
        :type method_list: Optional[list]
        :param plot: Plot types: 'mcs' (heatmap), 'ci' (confidence interval), or both.
        :type plot: Optional[Union[list, str]]
        :param alpha: Significance level for intervals.
        :type alpha: float
        :param direction_dict: Mapping metric -> 'maximize' or 'minimize'.
        :type direction_dict: dict
        :param effect_dict: Mapping metric -> effect size threshold for colormap scaling.
        :type effect_dict: dict
        :param title_size: Title font size.
        :type title_size: float
        :param cell_text_size: Annotation font size.
        :type cell_text_size: float
        :param axis_text_size: Axis label font size.
        :type axis_text_size: float
        :param left_xlim: Left x-axis limit for CI plots.
        :type left_xlim: float
        :param right_xlim: Right x-axis limit for CI plots.
        :type right_xlim: float
        :param save_fig: If True, save figures.
        :type save_fig: bool
        :param save_result: If True, save results as CSV.
        :type save_result: bool
        :param save_dir: Directory for outputs.
        :type save_dir: str
        :return: Mapping metric -> dict of results including tables, means, differences, and p-values.
        :rtype: Dict[str, Dict[str, pandas.DataFrame]]
        """
        try:
            report_new, scoring_list, method_list = (
                StatisticalAnalysis.extract_scoring_dfs(
                    report_df=report_df,
                    scoring_list=scoring_list,
                    method_list=method_list,
                    melt=True,
                )
            )
            # If only one method is provided, skip the test.
            if not method_list or len(method_list) == 1:
                logging.info(
                    "StatisticalAnalysis: Only one method provided. Skipping statistical test."
                )
                return None

            # Set defaults
            for key in scoring_list:
                direction_dict.setdefault(
                    key, "maximize" if key != "max_error" else "minimize"
                )

            for key in scoring_list:
                effect_dict.setdefault(key, 0.1)

            direction_dict = {k.lower(): v for k, v in direction_dict.items()}
            effect_dict = {k.lower(): v for k, v in effect_dict.items()}

            tukey_results = {}

            for scoring in scoring_list:

                scoring_data = report_new[report_new["scoring"] == scoring]

                if direction_dict and scoring in direction_dict:
                    if direction_dict[scoring] == "maximize":
                        df_means = (
                            scoring_data.groupby("method")
                            .mean(numeric_only=True)
                            .sort_values("value", ascending=False)
                        )
                    elif direction_dict[scoring] == "minimize":
                        df_means = (
                            scoring_data.groupby("method")
                            .mean(numeric_only=True)
                            .sort_values("value", ascending=True)
                        )
                    else:
                        raise ValueError(
                            "Invalid direction. Expected 'maximize' or 'minimize'."
                        )
                else:
                    df_means = scoring_data.groupby("method").mean(numeric_only=True)

                with warnings.catch_warnings():
                    warnings.filterwarnings("ignore", category=RuntimeWarning)
                    aov = pg.rm_anova(
                        dv="value",
                        within="method",
                        subject="cv_cycle",
                        data=scoring_data,
                        detailed=True,
                    )

                mse = aov.loc[1, "MS"]
                df_resid = aov.loc[1, "DF"]

                methods = df_means.index
                n_groups = len(methods)
                n_per_group = scoring_data["method"].value_counts().mean()

                tukey_se = np.sqrt(2 * mse / n_per_group)
                q = qsturng(1 - alpha, n_groups, df_resid)

                num_comparisons = len(methods) * (len(methods) - 1) // 2
                result_tab = pd.DataFrame(
                    index=range(num_comparisons),
                    columns=["group1", "group2", "meandiff", "lower", "upper", "p-adj"],
                )

                df_means_diff = pd.DataFrame(index=methods, columns=methods, data=0.0)
                pc = pd.DataFrame(index=methods, columns=methods, data=1.0)

                row_idx = 0
                for i, method1 in enumerate(methods):
                    for j, method2 in enumerate(methods):
                        if i < j:
                            group1 = scoring_data[scoring_data["method"] == method1][
                                "value"
                            ]
                            group2 = scoring_data[scoring_data["method"] == method2][
                                "value"
                            ]
                            mean_diff = group1.mean() - group2.mean()
                            studentized_range = np.abs(mean_diff) / tukey_se
                            adjusted_p = psturng(
                                studentized_range * np.sqrt(2), n_groups, df_resid
                            )
                            if isinstance(adjusted_p, np.ndarray):
                                adjusted_p = adjusted_p[0]
                            lower = mean_diff - (q / np.sqrt(2) * tukey_se)
                            upper = mean_diff + (q / np.sqrt(2) * tukey_se)
                            result_tab.loc[row_idx] = [
                                method1,
                                method2,
                                mean_diff,
                                lower,
                                upper,
                                adjusted_p,
                            ]
                            pc.loc[method1, method2] = adjusted_p
                            pc.loc[method2, method1] = adjusted_p
                            df_means_diff.loc[method1, method2] = mean_diff
                            df_means_diff.loc[method2, method1] = -mean_diff
                            row_idx += 1

                df_means_diff = df_means_diff.astype(float)

                result_tab["group1_mean"] = result_tab["group1"].map(df_means["value"])
                result_tab["group2_mean"] = result_tab["group2"].map(df_means["value"])

                result_tab.index = result_tab["group1"] + " - " + result_tab["group2"]

                tukey_results[scoring] = {
                    "result_tab": result_tab,
                    "df_means": df_means,
                    "df_means_diff": df_means_diff,
                    "pc": pc,
                }
                if save_result:
                    if save_dir and not os.path.exists(save_dir):
                        os.makedirs(save_dir, exist_ok=True)
                    result_tab.to_csv(
                        f"{save_dir}/tukey_result_tab_{scoring}.csv", index=False
                    )
                    df_means.to_csv(
                        f"{save_dir}/tukey_df_means_{scoring}.csv", index=False
                    )
                    df_means_diff.to_csv(
                        f"{save_dir}/tukey_df_means_diff_{scoring}.csv", index=False
                    )
                    pc.to_csv(f"{save_dir}/tukey_pc_{scoring}.csv", index=False)
                    logging.info(
                        f"StatisticalAnalysis: Tukey HSD results saved at {save_dir}"
                    )

            if not plot:
                plot = ["mcs", "ci"]
            elif isinstance(plot, str):
                plot = [plot]

            for type in plot:
                if type not in ["mcs", "ci"]:
                    raise ValueError(
                        f"Unsupported plot: {type}."
                        "Please choose 'mcs' for MCS plots or 'ci' for CI plots."
                    )

                if type == "mcs":
                    StatisticalAnalysis._make_mcs_plot_grid(
                        tukey_results,
                        scoring_list,
                        method_list,
                        direction_dict,
                        effect_dict,
                        show_diff=True,
                        cell_text_size=cell_text_size,
                        axis_text_size=axis_text_size,
                        title_size=title_size,
                        save_fig=save_fig,
                        save_dir=save_dir,
                    )

                if type == "ci":
                    StatisticalAnalysis._make_ci_plot_grid(
                        tukey_results,
                        scoring_list,
                        method_list,
                        title_size=title_size,
                        axis_text_size=axis_text_size,
                        left_xlim=left_xlim,
                        right_xlim=right_xlim,
                        save_fig=save_fig,
                        save_dir=save_dir,
                    )

            return tukey_results

        except Exception as e:
            logging.error(
                f"An error occurred during the posthoc Tukey HSD analysis: {e}"
            )
            return {}

    @staticmethod
    def _mcs_plot(
        pc: pd.DataFrame,
        effect_size: pd.DataFrame,
        means: pd.DataFrame,
        labels: bool = True,
        cmap: Optional[str] = None,
        cbar_ax_bbox: Optional[tuple] = None,
        ax: Optional[plt.Axes] = None,
        show_diff: bool = True,
        cell_text_size: float = 16,
        axis_text_size: float = 12,
        show_cbar: bool = True,
        reverse_cmap: bool = False,
        vlim: Optional[float] = None,
        **kwargs,
    ) -> plt.Axes:
        """
        Internal: draw matrix-of-comparisons (MCS) heatmap.

        :param pc: Pairwise p-values.
        :type pc: pandas.DataFrame
        :param effect_size: Effect size matrix.
        :type effect_size: pandas.DataFrame
        :param means: Per-method means.
        :type means: pandas.DataFrame
        :param labels: Annotate with method names and means.
        :type labels: bool
        :param cmap: Colormap name.
        :type cmap: Optional[str]
        :param cbar_ax_bbox: Optional colorbar position.
        :type cbar_ax_bbox: Optional[tuple]
        :param ax: Matplotlib axis to draw on.
        :type ax: Optional[matplotlib.axes.Axes]
        :param show_diff: Annotate cells with differences.
        :type show_diff: bool
        :param cell_text_size: Font size for cell text.
        :type cell_text_size: float
        :param axis_text_size: Axis font size.
        :type axis_text_size: float
        :param show_cbar: Show colorbar when True.
        :type show_cbar: bool
        :param reverse_cmap: Reverse colormap when True.
        :type reverse_cmap: bool
        :param vlim: Effect size clipping limit.
        :type vlim: Optional[float]
        :return: Axis with heatmap drawn.
        :rtype: matplotlib.axes.Axes
        """
        try:
            for key in ["cbar", "vmin", "vmax", "center"]:
                if key in kwargs:
                    del kwargs[key]

            if not cmap:
                cmap = "coolwarm"
            if reverse_cmap:
                cmap = cmap + "_r"

            significance = pc.copy().astype(object)
            significance[(pc < 0.001) & (pc >= 0)] = "***"
            significance[(pc < 0.01) & (pc >= 0.001)] = "**"
            significance[(pc < 0.05) & (pc >= 0.01)] = "*"
            significance[(pc >= 0.05)] = ""

            np.fill_diagonal(significance.values, "")

            # Create a DataFrame for the annotations
            if show_diff:
                annotations = effect_size.round(3).astype(str) + significance
            else:
                annotations = significance

            hax = sns.heatmap(
                effect_size,
                cmap=cmap,
                annot=annotations,
                fmt="",
                cbar=show_cbar,
                ax=ax,
                annot_kws={"size": cell_text_size},
                vmin=-2 * vlim if vlim else None,
                vmax=2 * vlim if vlim else None,
                **kwargs,
            )

            if show_cbar:
                cbar = hax.collections[0].colorbar
                cbar.ax.tick_params(labelsize=axis_text_size)

            if labels:
                label_list = list(means.index)

                x_label_list = []

                for label in label_list:
                    if "Regression" in label:
                        new_label = label.replace("Regression", "\nRegression")
                    elif "Regressor" in label:
                        new_label = label.replace("Regressor", "\nRegressor")
                    elif "Classifier" in label:
                        new_label = label.replace("Classifier", "\nClassifier")
                    else:
                        new_label = label

                    new_label = new_label + f"\n{means.loc[label].values[0].round(3)}"

                    x_label_list.append(new_label)

                hax.set_xticklabels(
                    x_label_list,
                    size=axis_text_size,
                    ha="center",
                    va="top",
                    rotation=0,
                    rotation_mode="anchor",
                )
                hax.set_yticklabels(
                    x_label_list,
                    size=axis_text_size,
                    ha="center",
                    va="bottom",
                    rotation=90,
                    rotation_mode="anchor",
                )

            hax.set_xlabel("")
            hax.set_ylabel("")

            return hax

        except Exception as e:
            logging.error(f"An error occurred in _mcs_plot: {e}")
            return ax

    @staticmethod
    def _make_mcs_plot_grid(
        tukey_results: dict,
        scoring_list: list,
        method_list: list,
        direction_dict: dict = {},
        effect_dict: dict = {},
        show_diff: bool = True,
        cell_text_size: float = 16,
        axis_text_size: float = 12,
        title_size: float = 16,
        save_fig: bool = True,
        save_dir: str = "Project/Analysis",
    ) -> None:
        """
        Internal: create confidence interval plots from Tukey results.

        :param tukey_results: Mapping metric -> Tukey results.
        :type tukey_results: dict
        :param scoring_list: Metrics to plot.
        :type scoring_list: list
        :param method_list: Compared methods.
        :type method_list: list
        :param title_size: Title font size.
        :type title_size: float
        :param axis_text_size: Axis label font size.
        :type axis_text_size: float
        :param left_xlim: Left x-limit for CIs.
        :type left_xlim: float
        :param right_xlim: Right x-limit for CIs.
        :type right_xlim: float
        :param save_fig: Save plots when True.
        :type save_fig: bool
        :param save_dir: Output directory.
        :type save_dir: str
        """
        try:
            # Set defaults
            for key in scoring_list:
                direction_dict.setdefault(
                    key, "maximize" if key != "max_error" else "minimize"
                )

            for key in scoring_list:
                effect_dict.setdefault(key, 0.1)

            direction_dict = {k.lower(): v for k, v in direction_dict.items()}
            effect_dict = {k.lower(): v for k, v in effect_dict.items()}

            nrow = math.ceil(len(scoring_list) / 3)
            nmethod = len(method_list)
            fig, ax = plt.subplots(
                nrow, 3, figsize=(4.7 * nmethod, 1.4 * nmethod * nrow)
            )

            ax = ax.flatten()

            for i, scoring in enumerate(scoring_list):
                scoring = scoring.lower()

                if scoring not in direction_dict:
                    raise ValueError(
                        f"Stat '{scoring}' is missing in direction_dict. Please set its value."
                    )
                if scoring not in effect_dict:
                    raise ValueError(
                        f"Stat '{scoring}' is missing in effect_dict. Please set its value."
                    )

                reverse_cmap = False
                if direction_dict[scoring] == "minimize":
                    reverse_cmap = True

                df_means = tukey_results[scoring]["df_means"]
                df_means_diff = tukey_results[scoring]["df_means_diff"]
                pc = tukey_results[scoring]["pc"]

                hax = StatisticalAnalysis._mcs_plot(
                    pc=pc,
                    effect_size=df_means_diff,
                    means=df_means,
                    show_diff=show_diff,
                    ax=ax[i],
                    cbar=True,
                    cell_text_size=cell_text_size,
                    axis_text_size=axis_text_size,
                    reverse_cmap=reverse_cmap,
                    vlim=effect_dict[scoring],
                )
                hax.set_title(scoring.upper(), fontsize=title_size)

            # If there are less plots than cells in the grid, hide the remaining cells
            if (len(scoring_list) % 3) != 0:
                for i in range(len(scoring_list), nrow * 3):
                    ax[i].set_visible(False)

            plt.tight_layout()

            if save_fig:
                if save_dir and not os.path.exists(save_dir):
                    os.makedirs(save_dir, exist_ok=True)
                plt.savefig(
                    f"{save_dir}/tukey_mcs.pdf",
                    dpi=300,
                    bbox_inches="tight",
                )
                logging.info(
                    f"StatisticalAnalysis: MCS plot grid saved at {save_dir}/tukey_mcs.pdf"
                )

        except Exception as e:
            logging.error(f"An error occurred in _make_mcs_plot_grid: {e}")

    @staticmethod
    def _make_ci_plot_grid(
        tukey_results: dict,
        scoring_list: list,
        method_list: list,
        title_size: float = 16,
        axis_text_size: float = 12,
        left_xlim: float = -0.5,
        right_xlim: float = 0.5,
        save_fig: bool = True,
        save_dir: str = "Project/Analysis",
    ) -> None:
        """
        Create confidence-interval plots (mean differences with CI bars) for Tukey comparisons.

        Parameters
        ----------
        tukey_results
            Output from posthoc_tukeyhsd.
        scoring_list
            Ordered list of scoring metrics.
        method_list
            List of method names.
        title_size, axis_text_size
            Plot text sizes.
        left_xlim, right_xlim
            X-axis limits for CI axis.
        save_fig
            Save output to save_dir/tukey_ci.pdf if True.
        save_dir
            Directory to save plots.
        """
        try:
            nmethod = len(method_list)
            ncouple = nmethod * (nmethod - 1) // 2
            figure, axes = plt.subplots(
                len(scoring_list),
                1,
                figsize=(12, (1.2 + 0.25 * ncouple) * len(scoring_list)),
                sharex=False,
            )

            if not isinstance(axes, np.ndarray):
                axes = np.array([axes])

            for i, scoring in enumerate(scoring_list):
                result_tab = tukey_results[scoring]["result_tab"]

                result_err = np.array(
                    [
                        result_tab["meandiff"] - result_tab["lower"],
                        result_tab["upper"] - result_tab["meandiff"],
                    ]
                )
                sns.set_context("notebook")
                sns.set_style("whitegrid")
                ax = sns.pointplot(
                    x=result_tab.meandiff,
                    y=result_tab.index,
                    marker="o",
                    linestyle="",
                    ax=axes[i],
                    color="red",
                    markersize=5,
                )
                ax.errorbar(
                    y=result_tab.index,
                    x=result_tab["meandiff"],
                    xerr=result_err,
                    fmt="ro",
                    capsize=4,
                    ecolor="red",
                    markerfacecolor="red",
                )
                ax.axvline(0, ls="--", lw=3, color="#ADD3ED")
                ax.set_xlabel("Mean Difference", fontsize=axis_text_size)
                ax.set_ylabel("")
                ax.set_title(scoring.upper(), fontsize=title_size)
                ax.set_xlim(left_xlim, right_xlim)
                ax.tick_params(labelsize=axis_text_size)
                ax.grid(True, axis="x")

            plt.tight_layout()

            if save_fig:
                if save_dir and not os.path.exists(save_dir):
                    os.makedirs(save_dir, exist_ok=True)
                plt.savefig(
                    f"{save_dir}/tukey_ci.pdf",
                    dpi=300,
                    bbox_inches="tight",
                )
                logging.info(
                    f"StatisticalAnalysis: CI plot grid saved at {save_dir}/tukey_ci.pdf"
                )

        except Exception as e:
            logging.error(f"An error occurred in _make_ci_plot_grid: {e}")

    @staticmethod
    def analysis(
        report_df,
        scoring_list=None,
        method_list=None,
        check_assumptions=True,
        method: str = "all",
        save_dir="Project/Analysis",
    ) -> Dict[str, object]:
        """
        High-level pipeline: assumptions + tests + posthoc analyses.

        :param report_df: Input scoring DataFrame.
        :type report_df: pandas.DataFrame
        :param scoring_list: Metrics to analyze.
        :type scoring_list: Optional[Union[list, str]]
        :param method_list: Methods to include.
        :type method_list: Optional[list]
        :param check_assumptions: Run variance & normality checks first.
        :type check_assumptions: bool
        :param method: Which tests to run: 'parametric', 'non-parametric', 'all', or None.
        :type method: str
        :param save_dir: Directory for outputs.
        :type save_dir: str
        :return: Dictionary summarizing results and file paths.
        :rtype: Dict[str, object]
        """
        results: Dict[str, object] = {}

        try:
            # 1. Check Assumptions (Variance Homogeneity & Normality)
            if check_assumptions:
                # Variance Homogeneity Check
                variance_df = StatisticalAnalysis.check_variance_homogeneity(
                    report_df=report_df,
                    scoring_list=scoring_list,
                    method_list=method_list,
                    levene_test=True,
                    save_csv=True,
                    save_dir=save_dir,
                    csv_name="variance_homogeneity",
                )
                results["variance"] = variance_df

                # Normality Check
                StatisticalAnalysis.check_normality(
                    report_df=report_df,
                    scoring_list=scoring_list,
                    method_list=method_list,
                    save_fig=True,
                    save_dir=save_dir,
                    fig_name="normality",
                )
                results["normality"] = f"Normality plots saved at {save_dir}."

            # 2. Tests based on method parameter
            if method:
                if method in ["parametric", "all"]:
                    # Run parametric test: AnovaRM and posthoc Tukey HSD
                    StatisticalAnalysis.test(
                        report_df=report_df,
                        scoring_list=scoring_list,
                        method_list=method_list,
                        select_test="AnovaRM",
                        showmeans=True,
                        save_fig=True,
                        save_dir=save_dir,
                        fig_name="anova_test",
                    )
                    results["anova_test"] = (
                        f"AnovaRM test completed and figure saved at {save_dir}."
                    )

                    tukey_results = StatisticalAnalysis.posthoc_tukeyhsd(
                        report_df=report_df,
                        scoring_list=scoring_list,
                        method_list=method_list,
                        plot=[
                            "mcs",
                            "ci",
                        ],  # Use "mcs" for multiple comparisons plot (or "ci" for CI plot)
                        alpha=0.05,
                        direction_dict={},
                        effect_dict={},
                        title_size=16,
                        cell_text_size=12,
                        axis_text_size=12,
                        left_xlim=-0.5,
                        right_xlim=0.5,
                        save_fig=True,
                        save_result=True,
                        save_dir=save_dir,
                    )
                    results["posthoc_tukey"] = tukey_results

                if method in ["non-parametric", "all"]:
                    # Run non-parametric test: Friedman and posthoc Conover-Friedman
                    StatisticalAnalysis.test(
                        report_df=report_df,
                        scoring_list=scoring_list,
                        method_list=method_list,
                        select_test="friedman",
                        showmeans=True,
                        save_fig=True,
                        save_dir=save_dir,
                        fig_name="friedman_test",
                    )
                    results["friedman_test"] = (
                        f"Friedman test completed and figure saved at {save_dir}."
                    )

                    pc_results, rank_results = (
                        StatisticalAnalysis.posthoc_conover_friedman(
                            report_df=report_df,
                            scoring_list=scoring_list,
                            method_list=method_list,
                            plot=[
                                "sign",
                                "ccd",
                            ],  # Choose "sign" or "ccd" for plot type
                            axis_text_size=12,
                            title_size=16,
                            save_fig=True,
                            save_result=True,
                            save_dir=save_dir,
                        )
                    )
                    results["posthoc_conover"] = {
                        "pc_results": pc_results,
                        "rank_results": rank_results,
                    }

            return results

        except Exception as e:
            print(f"An error occurred during analysis: {e}")
            raise
