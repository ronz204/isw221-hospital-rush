from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Constants.Assets import Character
from src.Components.Component import Component
from src.Helpers.AssetHelper import AssetHelper

class BaseCharacter(Component):
  def __init__(self, coords: Coord, size: Size, image: Character):
    super().__init__(coords=coords, size=size)
    self.image = AssetHelper.load_image(image.value, size.as_tuple())
