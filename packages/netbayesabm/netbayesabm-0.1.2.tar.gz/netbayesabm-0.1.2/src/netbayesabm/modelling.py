#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NetBayesABM - Modelling Module
==============================

This module provides the core functions to build and simulate
agent-based models (ABM) of plant–pollinator networks.

The functions cover:
- Initialization of agents (plants and pollinators) with random,
  empirical, or regular spatial distributions.
- Construction of bipartite plant–pollinator networks.
- Evolution rules for agent movement and interaction.
- Updating of network edges and weights over time.

Typical workflow
----------------
1. Generate agents using initialization functions (e.g., `initial_pollinators_random`).
2. Create a bipartite network with `initial_network`.
3. Simulate dynamics with update functions (`update`, `update_totalinks`).
4. Analyze resulting structures with network metrics or export to data frames.

Notes
-----
- This module relies on classes defined in `classes.py` (e.g., `Agent_Plant`, `Agent_Pol`)
  for representing agents.
- The functions are designed to be flexible: randomization, classification of species,
  and movement dynamics can be adapted depending on the scenario.
- Networks are handled using NetworkX.

Examples
--------
>>> from netbayesabm import modelling as mdl
>>> generalists, poll_df = mdl.initial_pollinators_random(dist, 2, 50, 0, 10, 0, 10)
>>> B = mdl.initial_network(poll_df["Specie"].unique(), plant_ids)
>>> mdl.update_totalinks(100, env_pol, env_plant, B, 0, 10, 0, 10)
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import networkx as nx


def initial_pollinators_random(
    dist_pol: pd.Series,
    n_pols: int,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    classify: bool = True,
    random_distribution: bool = False
) -> tuple[list[str], pd.DataFrame]:
    """
    Generate the initial distribution of pollinators with customizable options.

    Parameters
    ----------
    dist_pol : pandas.Series
        Abundance distribution of pollinator species. Index must correspond to species labels.
    n_pols : int
        Total number of pollinator individuals.
    xmin, xmax, ymin, ymax : float
        Spatial boundaries for generating coordinates.
    classify : bool, default=True
        If True, classify pollinator species into generalists and specialists using K-means.
    random_distribution : bool, default=False
        If True, ignore `dist_pol` and assign individuals randomly using a Dirichlet distribution.

    Returns
    -------
    generalists : list of str
        List of species classified as generalists (empty if `classify=False`).
    df_final : pandas.DataFrame
        DataFrame with pollinator attributes:
        - ``Pol_id`` : unique ID of each pollinator
        - ``Specie`` : species label
        - ``x, y`` : spatial coordinates
        - ``Radius`` : interaction radius (larger for generalists)
        - ``Tipo`` : category (Generalist, Specialist, or Unclassified)

    Examples
    --------
    >>> dist = pd.Series([0.4, 0.6], index=["bee", "fly"])
    >>> generalists, df = initial_pollinators_random(dist, 2, 50, 0, 10, 0, 10)
    >>> df.head()
       Pol_id Specie     x     y  Radius         Tipo
    0    1000    bee  2.33  8.12      15  Generalista
    """
    generalists = []

    if classify:
        # Cluster species into generalists and specialists
        abundances = dist_pol.values.reshape(-1, 1)
        c1 = np.mean(dist_pol.values[:-2])
        c2 = np.mean(dist_pol.values[2:])
        initial_centroids = np.array([[c1], [c2]])

        kmeans = KMeans(n_clusters=2, init=initial_centroids, random_state=42)
        kmeans.fit(abundances)

        labels = kmeans.labels_
        df_intermediate = pd.DataFrame(
            {"Abundance": abundances.flatten(), "Label": labels},
            index=dist_pol.index
        )
        df_intermediate["Label"] = df_intermediate["Label"].map(
            {0: "Specialist", 1: "Generalist"}
        )
        generalists = df_intermediate.loc[
            df_intermediate["Label"] == "Generalist"
        ].index.tolist()

    # Probability distribution
    if random_distribution:
        probabilities = np.random.dirichlet(np.ones(len(dist_pol)), size=1).flatten()
    else:
        probabilities = dist_pol

    # Sample pollinator species
    pollinators = np.random.choice(dist_pol.index, n_pols, p=probabilities)

    # Attributes
    ids = np.arange(1000, 1000 + n_pols)
    xs = np.round(xmin + np.random.rand(n_pols) * (xmax - xmin), 3)
    ys = np.round(ymin + np.random.rand(n_pols) * (ymax - ymin), 3)

    if classify:
        radii = np.where(np.isin(pollinators, generalists), 15, 5)
    else:
        radii = np.random.gamma(10, 2, size=n_pols)

    df_final = pd.DataFrame(
        {"Pol_id": ids, "Specie": pollinators, "x": xs, "y": ys, "Radius": radii},
        index=ids,
    )

    if classify:
        df_final["Tipo"] = np.where(
            df_final["Specie"].isin(generalists), "Generalist", "Specialist"
        )
    else:
        df_final["Tipo"] = "Unclassified"

    return generalists, df_final



def initial_pollinators(
    dist_pol: pd.Series,
    n_pols: int,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float
) -> tuple[list[str], pd.DataFrame]:
    """
    Generate the initial distribution of pollinators (always classified into generalists
    and specialists).

    Parameters
    ----------
    dist_pol : pandas.Series
        Abundance distribution of pollinator species. Index must correspond to species labels.
    n_spe_pol : int
        Number of pollinator species.
    n_pols : int
        Total number of pollinator individuals.
    xmin, xmax, ymin, ymax : float
        Spatial boundaries for generating coordinates.

    Returns
    -------
    generalists : list of str
        List of species classified as generalists.
    df_final : pandas.DataFrame
        DataFrame with pollinator attributes:
        - ``Pol_id`` : unique ID of each pollinator
        - ``Specie`` : species label
        - ``x, y`` : spatial coordinates
        - ``Radius`` : interaction radius
        - ``Tipo`` : category (Generalist or Specialist)

    Examples
    --------
    >>> dist = pd.Series([0.3, 0.7], index=["bee", "butterfly"])
    >>> generalists, df = initial_pollinators(dist, 2, 30, 0, 5, 0, 5)
    >>> len(df)
    30
    """
    abundances = dist_pol.values.reshape(-1, 1)
    c1 = np.mean(dist_pol.values[:-2])
    c2 = np.mean(dist_pol.values[2:])
    initial_centroids = np.array([[c1], [c2]])

    kmeans = KMeans(n_clusters=2, init=initial_centroids, random_state=42)
    kmeans.fit(abundances)

    labels = kmeans.labels_
    df_intermediate = pd.DataFrame(
        {"Abundance": abundances.flatten(), "Label": labels}, index=dist_pol.index
    )
    df_intermediate["Label"] = df_intermediate["Label"].map(
        {0: "Specialist", 1: "Generalist"}
    )
    generalists = df_intermediate.loc[
        df_intermediate["Label"] == "Generalist"
    ].index.tolist()

    pollinators = np.random.choice(dist_pol.index, n_pols, p=dist_pol)

    ids = np.arange(1000, 1000 + n_pols)
    xs = np.round(xmin + np.random.rand(n_pols) * (xmax - xmin), 3)
    ys = np.round(ymin + np.random.rand(n_pols) * (ymax - ymin), 3)
    radii = np.where(np.isin(pollinators, generalists), 15, 5)

    df_final = pd.DataFrame(
        {"Pol_id": ids, "Specie": pollinators, "x": xs, "y": ys, "Radius": radii},
        index=ids,
    )
    df_final["Tipo"] = np.where(
        df_final["Specie"].isin(generalists), "Generalist", "Specialist"
    )

    return generalists, df_final

# Network Functions

def initial_network(
    pollinators: list[str],
    plants: list[str]
) -> nx.DiGraph:
    """
    Create the initial bipartite directed network of pollinators and plants.

    The initial graph is a complete directed bipartite graph with all edges
    from pollinators to plants, initialized with weight = 0.

    Parameters
    ----------
    pollinators : list of str
        Labels (IDs) of pollinator nodes.
    plants : list of str
        Labels (IDs) of plant nodes.

    Returns
    -------
    networkx.DiGraph
        Directed bipartite graph with:
        - Nodes in two partitions (pollinators, plants).
        - Edges from pollinators to plants with weight = 0.

    Examples
    --------
    >>> pollinators = ["bee", "fly"]
    >>> plants = ["rose", "daisy"]
    >>> G = initial_network(pollinators, plants)
    >>> G.number_of_edges()
    4
    """
    B = nx.DiGraph()
    B.add_nodes_from(pollinators, bipartite=0)
    B.add_nodes_from(plants, bipartite=1)
    B.add_weighted_edges_from((u, v, 0) for u in pollinators for v in plants)
    return B

def remove_zero(B: nx.DiGraph) -> None:
    """
    Remove edges with zero weight from a bipartite network.

    Parameters
    ----------
    B : networkx.DiGraph
        Directed bipartite graph with weighted edges.

    Returns
    -------
    None
        The graph is modified in place.

    Examples
    --------
    >>> G = initial_network(["bee"], ["rose"])
    >>> remove_zero(G)
    >>> G.number_of_edges()
    0
    """
    edge_list = [(u, v) for (u, v, w) in B.edges(data=True) if w["weight"] == 0]
    B.remove_edges_from(edge_list)

def degree_dist(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """
    Compute the degree distribution of plants and pollinators
    in a bipartite adjacency matrix.

    Parameters
    ----------
    df : pandas.DataFrame
        Bipartite adjacency matrix (rows = plants, columns = pollinators).
        Values should be numeric (0/1 or weights).

    Returns
    -------
    pol_degree : pandas.Series
        Degree distribution of pollinators (sum over rows).
    plant_degree : pandas.Series
        Degree distribution of plants (sum over columns).

    Examples
    --------
    >>> import pandas as pd
    >>> M = pd.DataFrame([[1, 0], [1, 1]], index=["plant1", "plant2"], columns=["bee", "fly"])
    >>> pol_degree, plant_degree = degree_dist(M)
    >>> pol_degree.to_dict()
    {'bee': 2, 'fly': 1}
    >>> plant_degree.to_dict()
    {'plant1': 1, 'plant2': 2}
    """
    plant_degree = df.astype(bool).sum(axis=1)
    pol_degree = df.astype(bool).sum(axis=0)
    return pol_degree, plant_degree

## Evolution programs

def plant_pol(NewAgent, env) -> list:
    """
    Find all plants within the action radius of a pollinator agent.

    Parameters
    ----------
    NewAgent : object
        Pollinator agent with attributes:
        - ``x`` (float) : x-coordinate
        - ``y`` (float) : y-coordinate
        - ``radioAccion`` (float) : action radius
    env : object
        Environment object with attribute:
        - ``plant_list`` (list) : list of plant agents, each with ``x`` and ``y``.

    Returns
    -------
    list
        List of plant agents located within the action radius of `NewAgent`.

    Examples
    --------
    >>> neighbors = plant_pol(pollinator, environment)
    >>> len(neighbors)
    3
    """
    x, y, radius = NewAgent.x, NewAgent.y, NewAgent.radioAccion
    neighbors = [
        nb for nb in env.plant_list
        if (x - nb.x) ** 2 + (y - nb.y) ** 2 < radius ** 2
    ]
    return neighbors


def update(
    envpol,
    evenp,
    B: nx.DiGraph,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float
) -> None:
    """
    Perform a single update of the pollinator–plant network.

    A random pollinator is selected, moved to a new position,
    and linked to the closest plant within its action radius.
    The corresponding edge weight in the bipartite graph is increased by 1.

    Parameters
    ----------
    envpol : object
        Environment object with attribute ``pol_list`` (list of pollinator agents).
    evenp : object
        Environment object with attribute ``plant_list`` (list of plant agents).
    B : networkx.DiGraph
        Bipartite directed graph of pollinators and plants, with weighted edges.
    xmin, xmax, ymin, ymax : float
        Spatial boundaries for repositioning pollinators.

    Returns
    -------
    None
        The graph `B` is updated in place.

    Examples
    --------
    >>> update(envpol, envplants, G, 0, 10, 0, 10)
    >>> sum(nx.get_edge_attributes(G, "weight").values()) > 0
    True
    """
    indAgent = np.random.choice(len(envpol.pol_list))
    NewAgent = envpol.pol_list[indAgent]

    NewAgent.random_xy_pol(xmin, xmax, ymin, ymax)
    neighbors = plant_pol(NewAgent, evenp)

    if neighbors:
        # compute distances to each neighbor
        distances = [
            (n, ((NewAgent.x - n.x) ** 2 + (NewAgent.y - n.y) ** 2) ** 0.5)
            for n in neighbors
        ]
        # select the closest neighbor
        selected_neigh = min(distances, key=lambda x: x[1])[0]
        B[NewAgent.id][selected_neigh.id]["weight"] += 1


def update_totalinks(
    tlink: int,
    envpol,
    evenp,
    B: nx.DiGraph,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float
) -> None:
    """
    Update the bipartite network until the total number of links reaches `tlink`.

    Parameters
    ----------
    tlink : int
        Target number of links (sum of all edge weights).
    envpol : object
        Environment object with attribute ``pol_list`` (list of pollinator agents).
    evenp : object
        Environment object with attribute ``plant_list`` (list of plant agents).
    B : networkx.DiGraph
        Bipartite directed graph of pollinators and plants, with weighted edges.
    xmin, xmax, ymin, ymax : float
        Spatial boundaries for repositioning pollinators.

    Returns
    -------
    None
        The graph `B` is updated in place until the desired total number of links is reached.

    Notes
    -----
    This function has not been extensively tested.

    Examples
    --------
    >>> update_totalinks(100, envpol, envplants, G, 0, 10, 0, 10)
    >>> sum(nx.get_edge_attributes(G, "weight").values())
    100
    """
    total_links = sum(nx.get_edge_attributes(B, "weight").values())
    while total_links < tlink:
        update(envpol, evenp, B, xmin, xmax, ymin, ymax)
        total_links += 1



