class datarecipesError(Exception):
    """Base class for frame factory errors"""


class ConfigurationError(datarecipesError):
    """The specified configuration is invalid"""


class MissingDependencyError(datarecipesError):
    """An upstream dependency is missing and at least one dependency does not allow missing"""
