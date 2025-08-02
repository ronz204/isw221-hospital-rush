from pygame import mouse
from pygame import Surface, draw
from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Constants.Assets import Font
from src.Helpers.AssetHelper import AssetHelper
from src.Components.Equipment.BaseEquipment import BaseEquipment

class Stretcher(BaseEquipment):
  def __init__(self, coords: Coord):
    super().__init__(coords=coords, size=Size(90, 90))
    self.image = Surface(self.size.as_tuple())
    self.image = self.image.convert_alpha()
    self.image.fill((0,0,0,0))

    draw.rect(self.image, (173, 216, 230), self.image.get_rect(), border_radius=14)
    draw.rect(self.image, (200, 200, 200), self.image.get_rect(), width=3, border_radius=14)

    self.hovered_flag = False
    
  def listen(self, event) -> None:
    cursor = mouse.get_pos()
    self.hovered_flag = False

    if (self.rect.collidepoint(cursor)):
      self.hovered_flag = True

  def draw(self, screen) -> None:
    if (self.hovered_flag):
      screen.blit(AssetHelper.load_font(Font.KARMATIC.value, 10, "testing"), (20, 20))
