# -*- coding: utf-8 -*-

"""Top-level package for datarecipes."""

__author__ = """Tom Rutherford"""
__email__ = "foreverwintr@gmail.com"

from importlib.metadata import version

__version__ = version("datarecipes")


from datarecipes.blueprint import Blueprint
from datarecipes.factory import Factory
from datarecipes.factory import FactoryMP
from datarecipes.recipes.base import Dependencies
from datarecipes.recipes.base import DependencyRequest
from datarecipes.recipes.base import Recipe

__all__ = [
    "Blueprint",
    "DependencyRequest",
    "Dependencies",
    "Recipe",
    "Factory",
    "FactoryMP",
]
