from pygame.event import Event
from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Constants.Assets import Button
from src.Components.Component import Component
from src.Helpers.AssetHelper import AssetHelper

class Base(Component):
  def __init__(self, coords: Coord, size: Size, image: Button):
    super().__init__(coords=coords, size=size)
    self.image = AssetHelper.load_image(image.value, size.as_tuple())

  def on_event(self, event: Event) -> None:
    if (self.rect.collidepoint(event.pos)):
      self.on_click()

  def on_click(self) -> None:
    raise NotImplementedError()
