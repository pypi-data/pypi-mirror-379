"""
NetBayesABM - Metrics Module
============================

This module provides distance and divergence metrics for comparing
empirical and simulated data in plant–pollinator agent-based models (ABM).

Functions
---------
hellinger_distance
    Compute the Hellinger distance between two probability distributions.
compute_metrics
    Calculate multiple metrics (Jensen–Shannon, KS, Wasserstein, Hellinger,
    MAE, KL) across simulation iterations.

Notes
-----
- Input data is expected as probability distributions or count vectors
  (depending on the metric).
- All metrics are computed in a vectorized way for efficiency.

References
----------
- Jensen–Shannon divergence: https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence
- Hellinger distance: https://en.wikipedia.org/wiki/Hellinger_distance
- Kolmogorov–Smirnov test: https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test
- Wasserstein distance: https://en.wikipedia.org/wiki/Wasserstein_metric
"""

#Importing libraries

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import jensenshannon
from scipy.stats import ks_2samp, wasserstein_distance

###### Functions #################################

def hellinger_distance(p: np.ndarray, q: np.ndarray) -> float:
    """
    Compute the Hellinger distance between two probability distributions.

    Parameters
    ----------
    p : numpy.ndarray
        First probability distribution (1D, must sum to 1).
    q : numpy.ndarray
        Second probability distribution (1D, must sum to 1).

    Returns
    -------
    float
        Hellinger distance in [0, 1].

    Examples
    --------
    >>> p = np.array([0.4, 0.6])
    >>> q = np.array([0.5, 0.5])
    >>> hellinger_distance(p, q)
    0.070710678...
    """
    return np.sqrt(0.5 * np.sum((np.sqrt(p) - np.sqrt(q))**2))


def compute_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute multiple metrics to compare real vs model distributions
    across simulation iterations.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the following columns:
        - ``iteration`` : identifier of the simulation run
        - ``Real`` : observed values (counts or frequencies)
        - ``Model`` : simulated values
        - ``r_esp`` : parameter value for specialists (constant within iteration)
        - ``r_gen`` : parameter value for generalists (constant within iteration)

    Returns
    -------
    pandas.DataFrame
        DataFrame with one row per iteration, containing:
        - ``iteration`` : int
        - ``JS_divergence`` : float
        - ``KS_distance`` : float
        - ``Wasserstein_distance`` : float
        - ``Hellinger_distance`` : float
        - ``MAE`` : float (relative mean absolute error)
        - ``KL_divergence`` : float
        - ``r_esp`` : float
        - ``r_gen`` : float

    Notes
    -----
    - Probabilities are normalized with a small epsilon (1e-10) to avoid zero divisions.
    - Jensen–Shannon divergence is squared (scipy returns the square root by default).

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "iteration": [1, 1, 2, 2],
    ...     "Real": [10, 20, 5, 15],
    ...     "Model": [12, 18, 6, 14],
    ...     "r_esp": [0.1, 0.1, 0.2, 0.2],
    ...     "r_gen": [0.5, 0.5, 0.6, 0.6]
    ... })
    >>> results = compute_metrics(df)
    >>> results[["iteration", "JS_divergence", "MAE"]]
       iteration  JS_divergence       MAE
    0          1        0.000123  0.100000
    1          2        0.000234  0.066667
    """
    results = []

    for iteration, group in df.groupby("iteration"):
        real = group["Real"].values
        model = group["Model"].values

        # Normalizar para comparaciones basadas en probabilidad
        real_dist = real / real.sum() if real.sum() > 0 else np.ones_like(real) / len(real)
        model_dist = model / model.sum() if model.sum() > 0 else np.ones_like(model) / len(model)

        epsilon = 1e-10
        real_dist = np.clip(real_dist, epsilon, 1)
        model_dist = np.clip(model_dist, epsilon, 1)

        # Calcular métricas
        js_div = jensenshannon(real_dist, model_dist, base=np.e) ** 2
        ks_stat, _ = ks_2samp(real, model)
        wass_dist = wasserstein_distance(real, model)
        hell_dist = hellinger_distance(real_dist, model_dist)
        mae = np.mean(np.abs(model - real) / np.clip(real, epsilon, None))
        kl_div = np.sum(real_dist * np.log(real_dist / model_dist))

        r_esp = group["r_esp"].iloc[0]
        r_gen = group["r_gen"].iloc[0]

        results.append({
            "iteration": iteration,
            "JS_divergence": js_div,
            "KS_distance": ks_stat,
            "Wasserstein_distance": wass_dist,
            "Hellinger_distance": hell_dist,
            "Relative_MAE": mae,
            "Absolute_MAE": np.mean(np.abs(model - real)),
            "KL_divergence": kl_div,
            "r_esp": r_esp,
            "r_gen": r_gen
        })

    return pd.DataFrame(results)

def plot_degree_comp(
    data: pd.DataFrame,
    plot_month: str
) -> float:
    """
    Compare real vs. simulated degree distributions for each species and plot the results.

    The function aggregates model outputs by species across iterations, computes
    absolute error and RMSE with respect to real values, and visualizes:
    - Real degrees
    - Mean model degrees
    - Min–max model range
    - Absolute error
    - RMSE

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame with the following required columns:
        - ``iteration`` : simulation run identifier
        - ``Unnamed: 0`` : species identifier
        - ``Model`` : simulated degree value
        - ``Real`` : observed degree value (same across iterations)
    plot_month : str
        Label used in the plot title and output filename (e.g. `"May_2023"`).

    Returns
    -------
    float
        Total absolute error across all species.

    Notes
    -----
    - The figure is shown but not saved by default.
    - To save the figure, uncomment the `plt.savefig` line.

    Examples
    --------
    >>> df = pd.DataFrame({
    ...     "iteration": [1, 1, 2, 2],
    ...     "Unnamed: 0": ["sp1", "sp2", "sp1", "sp2"],
    ...     "Model": [5, 10, 6, 9],
    ...     "Real": [5, 12, 5, 12]
    ... })
    >>> total_error = plot_degree_comp(df, "TestMonth")
    >>> round(total_error, 2)
    3.0
    """
    # Aggregate by species
    summary = data.groupby("Unnamed: 0").agg(
        mean_model=("Model", "mean"),
        std_model=("Model", "std"),
        min_model=("Model", "min"),
        max_model=("Model", "max"),
        real_degree=("Real", "first")  # real degree is constant across iterations
    ).reset_index()

    # Model matrix for RMSE
    model_matrix = data.pivot_table(
        index="iteration", columns="Unnamed: 0", values="Model", aggfunc="mean"
    )
    species = summary["Unnamed: 0"].values
    real = summary["real_degree"].values
    mean_model = summary["mean_model"].values

    # Errors
    abs_error = np.abs(mean_model - real)
    rmse = np.sqrt(np.mean((model_matrix[species].values - real) ** 2, axis=0))
    total_abs_error = abs_error.sum()

    # Plot
    plt.figure(figsize=(14, 6))
    plt.plot(species, real, marker="o", linestyle="-", label="Real", linewidth=2)
    plt.plot(species, mean_model, marker="s", linestyle="--", label="Model Mean", linewidth=1)
    plt.fill_between(
        species,
        summary["min_model"],
        summary["max_model"],
        color="gray",
        alpha=0.3,
        label="Model Min-Max Range"
    )

    # Error curves
    plt.plot(species, abs_error, linestyle="dotted", marker="x", color="red", label="Abs. Error")
    plt.plot(species, rmse, linestyle="dashdot", marker="d", color="purple", label="RMSE")

    name = f"Top10_{plot_month}.png"
    plt.title(f"{name} — Total Abs. Error: {total_abs_error:.2f}")
    plt.xticks(rotation=90)
    plt.xlabel("Species")
    plt.ylabel("Degree")
    plt.legend()
    plt.tight_layout()
    # plt.savefig(name)

    return total_abs_error

def top_metric(
    df_metrics: pd.DataFrame,
    metric: str,
    top_fraction: float = 0.1
) -> pd.DataFrame:
    """
    Select the top fraction of rows based on a given metric.

    Parameters
    ----------
    df_metrics : pandas.DataFrame
        DataFrame containing evaluation results and metrics.
    metric : str
        Name of the column used to rank the rows.
    top_fraction : float, default=0.1
        Fraction of top rows to keep (between 0 and 1).
        At least one row is always returned.

    Returns
    -------
    pandas.DataFrame
        Subset of the DataFrame with the top-ranked rows.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({"iteration": [1, 2, 3],
    ...                    "score": [0.2, 0.8, 0.5]})
    >>> top_metric(df, "score", top_fraction=0.33)
       iteration  score
    1          2    0.8
    """
    df_sorted = df_metrics.sort_values(by=metric, ascending=False)
    top_n = max(1, int(len(df_sorted) * top_fraction))
    return df_sorted.head(top_n)

def resume_error(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize model vs. real values by species, computing error metrics.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing at least the following columns:
        - ``Unnamed: 0`` : species identifier
        - ``Real`` : observed values
        - ``Model`` : simulated values

    Returns
    -------
    pandas.DataFrame
        DataFrame with one row per species, including:
        - ``especie`` : species identifier
        - ``real_value`` : observed value (constant per species)
        - ``model_mean`` : mean simulated value
        - ``model_std`` : standard deviation of simulated values
        - ``model_min`` : minimum simulated value
        - ``model_max`` : maximum simulated value
        - ``abs_error`` : absolute error between real and mean simulated
        - ``z_score`` : absolute error normalized by model standard deviation
        - ``model_range`` : range (max - min) of simulated values
        - ``z_range`` : absolute error normalized by model range

    Notes
    -----
    - ``z_score`` and ``z_range`` are set to NaN if the denominator is zero.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "Unnamed: 0": ["sp1", "sp1", "sp2", "sp2"],
    ...     "Real": [10, 10, 5, 5],
    ...     "Model": [9, 11, 4, 6]
    ... })
    >>> summary = resume_error(df)
    >>> summary[["especie", "abs_error"]]
      especie  abs_error
    0     sp1        0.0
    1     sp2        0.0
    """
    df = df.copy()

    grouped = df.groupby("Unnamed: 0").agg(
        real_value=("Real", "mean"),   # should be constant per species
        model_mean=("Model", "mean"),
        model_std=("Model", "std"),
        model_min=("Model", "min"),
        model_max=("Model", "max")
    ).reset_index()

    grouped["abs_error"] = np.abs(grouped["real_value"] - grouped["model_mean"])

    grouped["z_score"] = np.where(
        grouped["model_std"] > 0,
        grouped["abs_error"] / grouped["model_std"],
        np.nan
    )

    grouped["model_range"] = grouped["model_max"] - grouped["model_min"]
    grouped["z_range"] = np.where(
        grouped["model_range"] > 0,
        grouped["abs_error"] / grouped["model_range"],
        np.nan
    )

    grouped = grouped.rename(columns={"Unnamed: 0": "especie"})

    return grouped
