#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NetBayesABM - Agent and Environment Classes
===========================================

This module defines the core classes for representing agents
(plants and pollinators) and their environments in the 
agent-based models (ABM) of plant–pollinator networks.

Classes
-------
Agent_Plant
    Dataclass representing a plant agent with species information and spatial coordinates.
Agent_Pol
    Dataclass representing a pollinator agent with species information, 
    spatial coordinates, and an interaction radius. Includes a method for random movement.
Environment_plant
    Container class that builds a list of `Agent_Plant` objects from a DataFrame.
    Supports three modes of plant positioning: 
    - as provided in the DataFrame
    - random within spatial boundaries
    - regular grid within spatial boundaries
Environment_pol
    Container class that builds a list of `Agent_Pol` objects from a DataFrame.

Typical workflow
----------------
1. Load empirical plant and pollinator data into pandas DataFrames.
2. Initialize agents with `Environment_plant` and `Environment_pol`.
3. Use the generated agent lists (`plant_list`, `pol_list`) as inputs 
   for the modelling functions in `modelling.py`.

Notes
-----
- These classes encapsulate the basic agent properties and their environment,
  but do not define network interactions or simulation dynamics (handled in `modelling.py`).
- Agent movement and interaction rules can be extended by adding methods to `Agent_Pol`
  or creating new environment classes.

Examples
--------
>>> import pandas as pd
>>> from netbayesabm.classes import Environment_plant, Environment_pol
>>> df_plants = pd.DataFrame({
...     "Plant_id": [1, 2],
...     "Plant_sp": ["rose", "daisy"],
...     "X": [0.0, 1.0],
...     "Y": [0.0, 1.0],
...     "Plant_sp_complete": ["Rosa sp.", "Bellis perennis"]
... })
>>> env_plants = Environment_plant(df_plants)
>>> len(env_plants.plant_list)
2
"""

from dataclasses import dataclass
import numpy as np


@dataclass
class Agent_Plant:
    """
    Plant agent in the pollination network.

    Parameters
    ----------
    id : int
        Unique identifier of the plant.
    sp : str
        Short species label.
    x : float
        X-coordinate of the plant in the environment.
    y : float
        Y-coordinate of the plant in the environment.
    sp_complete : str
        Full species name.
    """
    id: int
    sp: str
    x: float
    y: float
    sp_complete: str


@dataclass
class Agent_Pol:
    """
    Pollinator agent in the pollination network.

    Parameters
    ----------
    id : int
        Unique identifier of the pollinator.
    specie : str
        Species label of the pollinator.
    x : float
        X-coordinate of the pollinator in the environment.
    y : float
        Y-coordinate of the pollinator in the environment.
    radioAccion : float
        Action radius of the pollinator, defining its interaction range.
    """
    id: int
    specie: str
    x: float
    y: float
    radioAccion: float

    def random_xy_pol(self, xmin: float, xmax: float, ymin: float, ymax: float) -> None:
        """
        Move the pollinator agent using a Brownian-like movement.

        The new position is wrapped within the spatial boundaries of the environment.

        Parameters
        ----------
        xmin, xmax : float
            Minimum and maximum x-coordinates of the environment.
        ymin, ymax : float
            Minimum and maximum y-coordinates of the environment.

        Returns
        -------
        None
            The pollinator's `x` and `y` attributes are updated in place.

        Examples
        --------
        >>> p = Agent_Pol(id=1, specie="bee", x=5.0, y=5.0, radioAccion=1.0)
        >>> p.random_xy_pol(0, 10, 0, 10)
        >>> 0 <= p.x <= 10 and 0 <= p.y <= 10
        True
        """
        m = self.radioAccion
        self.x = (self.x + np.random.uniform(-m, m) - xmin) % (xmax - xmin) + xmin
        self.y = (self.y + np.random.uniform(-m, m) - ymin) % (ymax - ymin) + ymin


class Environment_plant:
    """
    Environment for plant agents.

    Builds a list of `Agent_Plant` objects from a pandas DataFrame, assigning
    spatial positions either as provided, randomly, or in a regular grid.

    Parameters
    ----------
    df_plantPM : pandas.DataFrame
        DataFrame containing plant information. Must include the following columns:
        - ``Plant_id`` : int, unique identifier of the plant
        - ``Plant_sp`` : str, short species name
        - ``X`` : float, x-coordinate (if no random/regular positioning)
        - ``Y`` : float, y-coordinate (if no random/regular positioning)
        - ``Plant_sp_complete`` : str, full species name
    random_position : bool, default=False
        If True, assign random coordinates uniformly within the given boundaries.
    regular_position : bool, default=False
        If True, assign coordinates on a regular grid within the given boundaries.
    xmin, xmax, ymin, ymax : float, optional
        Spatial boundaries. Required if `random_position=True` or `regular_position=True`.

    Attributes
    ----------
    plant_list : list of Agent_Plant
        List of plant agents created from the DataFrame.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "Plant_id": [1, 2, 3, 4],
    ...     "Plant_sp": ["rose", "daisy", "tulip", "sunflower"],
    ...     "X": [0, 0, 0, 0],
    ...     "Y": [0, 0, 0, 0],
    ...     "Plant_sp_complete": ["Rosa sp.", "Bellis perennis", "Tulipa sp.", "Helianthus annuus"]
    ... })
    >>> env = Environment_plant(df, regular_position=True, xmin=0, xmax=10, ymin=0, ymax=10)
    >>> all(isinstance(p.x, float) and isinstance(p.y, float) for p in env.plant_list)
    True
    """

    def __init__(
        self,
        df_plantPM,
        random_position: bool = False,
        regular_position: bool = False,
        xmin: float | None = None,
        xmax: float | None = None,
        ymin: float | None = None,
        ymax: float | None = None,
    ):
        if random_position or regular_position:
            if None in [xmin, xmax, ymin, ymax]:
                raise ValueError("xmin, xmax, ymin, ymax must be provided for random or regular positioning")

        if random_position:
            # Random coordinates
            df_plantPM["X"] = np.random.uniform(xmin, xmax, len(df_plantPM))
            df_plantPM["Y"] = np.random.uniform(ymin, ymax, len(df_plantPM))

        elif regular_position:
            # Regular grid coordinates
            num_plants = len(df_plantPM)
            num_rows = int(np.ceil(np.sqrt(num_plants)))
            num_cols = int(np.ceil(num_plants / num_rows))

            x_vals = np.linspace(xmin, xmax, num_cols)
            y_vals = np.linspace(ymin, ymax, num_rows)
            xy_combinations = [(x, y) for y in y_vals for x in x_vals]

            xy_combinations = xy_combinations[:num_plants]
            for i in range(num_plants):
                df_plantPM.iloc[i, df_plantPM.columns.get_loc("X")] = xy_combinations[i][0]
                df_plantPM.iloc[i, df_plantPM.columns.get_loc("Y")] = xy_combinations[i][1]

        self.plant_list = df_plantPM.apply(
            lambda row: Agent_Plant(
                id=row.Plant_id,
                sp=row.Plant_sp,
                x=row.X,
                y=row.Y,
                sp_complete=row.Plant_sp_complete,
            ),
            axis=1,
        ).tolist()

class Environment_pol:
    """
    Environment for pollinator agents.

    Builds a list of `Agent_Pol` objects from a pandas DataFrame.

    Parameters
    ----------
    df_polPM : pandas.DataFrame
        DataFrame containing pollinator information. Must include the following columns:
        - ``Pol_id`` : int, unique identifier of the pollinator
        - ``Specie`` : str, species name
        - ``x`` : float, x-coordinate
        - ``y`` : float, y-coordinate
        - ``Radius`` : float, action radius of the pollinator

    Attributes
    ----------
    pol_list : list of Agent_Pol
        List of pollinator agents created from the DataFrame.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "Pol_id": [1, 2],
    ...     "Specie": ["bee", "fly"],
    ...     "x": [1.0, 2.0],
    ...     "y": [3.0, 4.0],
    ...     "Radius": [1.5, 2.0]
    ... })
    >>> env = Environment_pol(df)
    >>> len(env.pol_list)
    2
    """

    def __init__(self, df_polPM):
        self.pol_list = df_polPM.apply(
            lambda row: Agent_Pol(
                id=row.Pol_id,
                specie=row.Specie,
                x=row.x,
                y=row.y,
                radioAccion=row.Radius,
            ),
            axis=1,
        ).tolist()
