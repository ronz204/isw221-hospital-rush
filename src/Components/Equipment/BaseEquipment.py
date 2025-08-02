from pygame import Surface
from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Components.Component import Component

class BaseEquipment(Component):
  def __init__(self, coords: Coord, size: Size):
    super().__init__(coords=coords, size=size)
