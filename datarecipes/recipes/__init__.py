from datarecipes.recipes.general import FromFunction
from datarecipes.recipes.general import Object

__all__ = [
    "Object",
    "FromFunction",
]

try:
    from datarecipes.recipes.static_frame import FrameFromDelimited
    from datarecipes.recipes.static_frame import FrameFromRecipes
    from datarecipes.recipes.static_frame import SeriesFromDelimited
except ModuleNotFoundError:
    pass
else:
    __all__.extend(
        [
            "SeriesFromDelimited",
            "FrameFromDelimited",
            "FrameFromRecipes",
        ]
    )
