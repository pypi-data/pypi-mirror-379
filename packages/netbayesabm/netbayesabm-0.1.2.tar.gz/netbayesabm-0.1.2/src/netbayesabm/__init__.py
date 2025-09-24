"""
NetBayesABM
===========

A Python library for simulating agent-based models (ABM) of 
plant–pollinator networks with Approximate Bayesian Computation (ABC).

Submodules
----------
classes
    Agent and environment classes for plants and pollinators.
modelling
    Core functions to initialize agents, construct bipartite networks,
    and evolve them over time.
data_analysis
    Helper functions to preprocess empirical datasets for ABM simulations.
visualization
    Tools for visualizing agents, networks, and simulation results.

Example
-------
>>> import netbayesabm as nb
>>> from netbayesabm import modelling as mdl, classes as cls
>>> # Initialize agents and environment
>>> generalists, poll_df = mdl.initial_pollinators_random(dist, 2, 50, 0, 10, 0, 10)
>>> env_pol = cls.Environment_pol(poll_df)
"""

__version__ = "0.1.0"
__author__ = "Javier Galeano, Blanca Arroyo-Correa"
__email__ = "javier.galeano@upm.es"

from . import classes
from . import modelling
from . import data_analysis
from . import visualization

__all__ = ["classes", "modelling", "data_analysis", "visualization"]