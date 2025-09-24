#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NetBayesABM - Visualization Module
==================================

This module provides visualization tools for plant–pollinator
agent-based models (ABM). The functions generate high-quality plots 
suitable for analysis, comparison, and publication.

Functions
---------
plot_abundances
    Plot a histogram of species abundances.
plot_priors
    Plot prior distributions of specialists and generalists.
plot_agents
    Display the spatial distribution of plants and pollinators in the environment.
comparative_plot
    Generic comparative plotting function for pollinators vs plants.
box_plot_comp
    Comparative boxplot of pollinator vs plant distributions.
KDE_plot_comp
    Comparative kernel density estimation (KDE) plot.
Cumulative_comp
    Comparative cumulative histogram of pollinator vs plant distributions.
LogLog_comp
    Comparative log-log histogram of pollinator vs plant distributions.
LogLog_comp_scatter
    Comparative log-log scatter plot of pollinator vs plant distributions.

Notes
-----
- Most plotting functions return the matplotlib `Axes` object to 
  allow further customization.
- Figures can be optionally saved with high resolution for publication.

Examples
--------
>>> from netbayesabm import visualization as viz
>>> ax = viz.plot_abundances(dist, "abundance_hist", bins=20, save=True)
>>> fig, axes = viz.box_plot_comp(deg_pol, deg_pla, "Degree Distribution")
"""

# visualization.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def plot_abundances(
    dist_pol: pd.Series | pd.DataFrame,
    name_file: str,
    bins: int = 30,
    save: bool = False
) -> plt.Axes:
    """
    Plot a histogram of species abundances with publication-quality settings.

    Parameters
    ----------
    dist_pol : pandas.Series or pandas.DataFrame
        Abundance data of species. If DataFrame, each column is treated separately.
    name_file : str
        Title for the plot. If `save=True`, this string is also used as the filename.
    bins : int, default=30
        Number of bins in the histogram.
    save : bool, default=False
        If True, saves the figure to `<name_file>.png` with high resolution.

    Returns
    -------
    matplotlib.axes.Axes
        The Axes object of the generated plot.

    Examples
    --------
    >>> import pandas as pd
    >>> dist = pd.Series([10, 12, 15, 7, 20, 30])
    >>> ax = plot_abundances(dist, "abundance_hist", bins=5, save=False)
    """
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

    dist_pol.hist(bins=bins, color="skyblue", edgecolor="black", ax=ax)
    ax.set_xlabel("P(Abundances)", fontsize=12)
    ax.set_ylabel("Number of Species", fontsize=12)
    ax.set_title(name_file, fontsize=14)

    if save:
        fig.savefig(f"{name_file}.png", dpi=300, bbox_inches="tight")

    return ax
    
def plot_priors(
    prior_e: pd.Series | np.ndarray,
    prior_g: pd.Series | np.ndarray,
    name_priors: str,
    bins: int = 100,
    save: bool = False
) -> plt.Axes:
    """
    Plot histograms of prior distributions for specialists and generalists.

    Parameters
    ----------
    prior_e : pandas.Series or numpy.ndarray
        Prior distribution values for specialists.
    prior_g : pandas.Series or numpy.ndarray
        Prior distribution values for generalists.
    name_priors : str
        Suffix for the plot title. If `save=True`, also used as filename.
    bins : int, default=100
        Number of bins for the histograms.
    save : bool, default=False
        If True, saves the figure as `<name_priors>_priors.png`.

    Returns
    -------
    matplotlib.axes.Axes
        The Axes object of the generated plot.

    Examples
    --------
    >>> import numpy as np
    >>> prior_e = np.random.gamma(2, 1, 1000)
    >>> prior_g = np.random.gamma(5, 1, 1000)
    >>> ax = plot_priors(prior_e, prior_g, "example")
    """
    fig, ax = plt.subplots(figsize=(8, 5), dpi=300)

    ax.hist(prior_e, bins=bins, alpha=0.5, label="prior_specialists", density=True)
    ax.hist(prior_g, bins=bins, alpha=0.5, label="prior_generalists", density=True)

    ax.set_title(f"Priors gamma {name_priors}")
    ax.set_xlabel("Value")
    ax.set_ylabel("Density")
    ax.legend()

    if save:
        fig.savefig(f"{name_priors}_priors.png", dpi=300, bbox_inches="tight")

    return ax


def plot_agents(
    env_plant,
    env_pol,
    plot: str,
    month: int,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    save: bool = False
) -> plt.Axes:
    """
    Plot the spatial distribution of plant and pollinator agents.

    Parameters
    ----------
    env_plant : Environment_plant
        Environment containing the list of plant agents (`plant_list`).
    env_pol : Environment_pol
        Environment containing the list of pollinator agents (`pol_list`).
    plot : str
        Identifier of the plot (for title).
    month : int
        Month identifier (for title).
    xmin, xmax, ymin, ymax : float
        Spatial boundaries of the environment.
    save : bool, default=False
        If True, saves the figure as `agents_plot_<plot>_<month>.png`.

    Returns
    -------
    matplotlib.axes.Axes
        The Axes object of the generated plot.

    Examples
    --------
    >>> ax = plot_agents(env_plants, env_pols, "A", 5, 0, 10, 0, 10)
    >>> ax.get_title()
    'Plant and Pollinator Locations: Plot A month 5'
    """
    fig, ax = plt.subplots(figsize=(10, 10), dpi=300)

    for plant in env_plant.plant_list:
        ax.scatter(plant.x, plant.y, color="green", label="Plants")

    for pol in env_pol.pol_list:
        ax.scatter(pol.x, pol.y, color="red", label="Pollinators")

    # Remove duplicate labels in legend
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys())

    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    ax.set_title(f"Plant and Pollinator Locations: Plot {plot} month {month}")
    ax.set_xlabel("X coordinate")
    ax.set_ylabel("Y coordinate")

    if save:
        fig.savefig(f"agents_plot_{plot}_{month}.png", dpi=300, bbox_inches="tight")

    return ax

def comparative_plot(
    deg_pol: pd.Series | np.ndarray,
    deg_pla: pd.Series | np.ndarray,
    text: str,
    plot_function,
    show: bool = True,
    **kwargs
) -> tuple[plt.Figure, np.ndarray]:
    """
    Generic comparative plot of pollinator vs plant degree distributions.

    Parameters
    ----------
    deg_pol : pandas.Series or numpy.ndarray
        Degree distribution (or other metric) for pollinators.
    deg_pla : pandas.Series or numpy.ndarray
        Degree distribution (or other metric) for plants.
    text : str
        Label used in plot titles (e.g., "Degree distribution").
    plot_function : callable
        Plotting function (e.g., seaborn.boxplot, seaborn.histplot).
        Must accept `ax` and `data` as arguments.
    show : bool, default=True
        If True, displays the figure with `plt.show()`.
    **kwargs
        Additional keyword arguments passed to `plot_function`.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The created figure.
    axes : numpy.ndarray
        Array of matplotlib.axes.Axes objects (length 2).

    Examples
    --------
    >>> comparative_plot(deg_pol, deg_pla, "Degree", sns.boxplot)
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), dpi=300)

    axes[0].set_title(text + " of Pollinators")
    plot_function(ax=axes[0], data=deg_pol, **kwargs)

    axes[1].set_title(text + " of Plants")
    plot_function(ax=axes[1], data=deg_pla, **kwargs)

    if show:
        plt.show()

    return fig, axes

def box_plot_comp(
    deg_pol: pd.Series | np.ndarray,
    deg_pla: pd.Series | np.ndarray,
    text: str,
    show: bool = True
):
    """
    Comparative boxplot of pollinator vs plant distributions.
    """
    return comparative_plot(deg_pol, deg_pla, text, sns.boxplot, show=show)

def KDE_plot_comp(
    deg_pol: pd.Series | np.ndarray,
    deg_pla: pd.Series | np.ndarray,
    text: str,
    show: bool = True
):
    """
    Comparative kernel density estimation (KDE) plot
    for pollinator vs plant distributions.
    """
    return comparative_plot(deg_pol, deg_pla, text, sns.kdeplot, show=show)

def Cumulative_comp(
    deg_pol: pd.Series | np.ndarray,
    deg_pla: pd.Series | np.ndarray,
    text: str,
    show: bool = True
):
    """
    Comparative cumulative histogram of pollinator vs plant distributions.
    """
    return comparative_plot(
        deg_pol, deg_pla, text, sns.histplot,
        show=show, bins=50, stat="density", element="step",
        fill=False, cumulative=True, common_norm=False
    )

def LogLog_comp(
    deg_pol: pd.Series | np.ndarray,
    deg_pla: pd.Series | np.ndarray,
    text: str,
    show: bool = True
):
    """
    Comparative log-log histogram of pollinator vs plant distributions.
    """
    log_deg_pol = np.log(deg_pol)
    log_deg_pla = np.log(deg_pla)
    return comparative_plot(
        log_deg_pol, log_deg_pla, text, sns.histplot,
        show=show, bins=50, stat="density", element="step",
        fill=False, common_norm=False
    )

def LogLog_comp_scatter(
    deg_pol: pd.Series | np.ndarray,
    deg_pla: pd.Series | np.ndarray,
    text: str,
    show: bool = True
):
    """
    Comparative log-log scatter plot of pollinator vs plant distributions.
    """
    log_deg_pol = np.log(deg_pol)
    log_deg_pla = np.log(deg_pla)
    return comparative_plot(
        log_deg_pol, log_deg_pla, text, sns.scatterplot, show=show
    )
