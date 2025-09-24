#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

NetBayesABM - Data Analysis Module
==================================

This module provides helper functions for preprocessing and analyzing
plant–pollinator datasets prior to running the agent-based models (ABM).

The functions include utilities for:
- Extracting subsets of plants by plot and month.
- Computing species frequencies and abundance distributions.
- Determining spatial boundaries for simulation environments.
- Preparing input data structures for agent initialization.

Typical workflow
----------------
1. Load empirical plant–pollinator data into a pandas DataFrame.
2. Use `freq_plant` to filter plants by plot and month and calculate species frequencies.
3. Use `area_plot` to compute spatial boundaries for the environment.
4. Pass the processed data to environment classes (`Environment_plant`, `Environment_pol`)
   for ABM simulations.

Notes
-----
- All functions expect input data in the form of pandas DataFrames with specific columns
  (e.g., ``Plot``, ``Month``, ``Plant_sp_complete``, ``X``, ``Y``).
- The module does not perform simulations directly, but prepares data for the core modelling
  functions in `modelling.py`.

Examples
--------
>>> from netbayesabm import data_analysis as da
>>> df_sub, freq_table = da.freq_plant("A", 5, df_plants)
>>> xmin, xmax, ymin, ymax = da.area_plot(df_sub)
"""

import pandas as pd
import numpy as np

def freq_plant(
    plot: str,
    month: int,
    df_plant: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Calculate frequency of plant species for a given plot and month.

    Parameters
    ----------
    plot : str
        Plot identifier to filter the data.
    month : int
        Month to filter the data.
    df_plant : pandas.DataFrame
        DataFrame containing plant records. Must include columns:
        - ``Plot`` : str
        - ``Month`` : int
        - ``Plant_sp_complete`` : str (full species name)

    Returns
    -------
    df_plant_pm : pandas.DataFrame
        Subset of the original DataFrame filtered by plot and month.
    table_plants : pandas.DataFrame
        Frequency table of plant species with columns:
        - ``Plant_sp_complete`` : str
        - ``counts`` : int
        - ``Freq`` : float (relative frequency)

    Examples
    --------
    >>> df_sub, freq_table = freq_plant("A", 5, df)
    >>> freq_table.head()
      Plant_sp_complete  counts  Freq
    0          Rosa sp.       10  0.25
    """
    df_plant_pm = df_plant.query("Plot == @plot and Month == @month")

    counts = df_plant_pm["Plant_sp_complete"].value_counts().rename("counts")
    freqs = counts / counts.sum()

    table_plants = (
        pd.DataFrame({"counts": counts, "Freq": freqs})
        .reset_index()
        .rename(columns={"index": "Plant_sp_complete"})
        .round(3)
    )

    return df_plant_pm, table_plants

def area_plot(
    df_plantPM: pd.DataFrame,
    margin: float = 2.0
) -> tuple[float, float, float, float]:
    """
    Calculate the spatial boundaries (xmin, xmax, ymin, ymax) for a set of plants.

    The function computes the minimum and maximum x and y coordinates of plants
    in the DataFrame, and extends them by a given margin.

    Parameters
    ----------
    df_plantPM : pandas.DataFrame
        DataFrame containing plant data. Must include columns:
        - ``X`` : float, x-coordinate
        - ``Y`` : float, y-coordinate
    margin : float, default=2.0
        Value added/subtracted to extend the boundaries beyond min/max.

    Returns
    -------
    xmin : float
        Minimum x-coordinate minus margin.
    xmax : float
        Maximum x-coordinate plus margin.
    ymin : float
        Minimum y-coordinate minus margin.
    ymax : float
        Maximum y-coordinate plus margin.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({"X": [1.0, 2.5, 4.0], "Y": [0.5, 3.0, 2.0]})
    >>> area_plot(df, margin=1.0)
    (0.0, 5.0, -0.5, 4.0)
    """
    xmin = df_plantPM["X"].min() - margin
    xmax = df_plantPM["X"].max() + margin
    ymin = df_plantPM["Y"].min() - margin
    ymax = df_plantPM["Y"].max() + margin

    return xmin, xmax, ymin, ymax
