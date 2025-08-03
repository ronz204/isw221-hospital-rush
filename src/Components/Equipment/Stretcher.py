from pygame import Surface, draw
from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Components.DragDrop.DropZone import DropZone
from src.Components.Equipment.BaseEquipment import BaseEquipment

class Stretcher(BaseEquipment):
  def __init__(self, coords: Coord):
    super().__init__(coords=coords, size=Size(150, 90))
    self.image = Surface(self.size.as_tuple())
    self.image = self.image.convert_alpha()
    self.image.fill((0,0,0,0))

    draw.rect(self.image, (173, 216, 230), self.image.get_rect(), border_radius=14)
    draw.rect(self.image, (200, 200, 200), self.image.get_rect(), width=3, border_radius=14)

    self.dropzone = DropZone(self.rect)

  def listen(self, event) -> None:
    pass

  def draw(self, screen) -> None:
    self.dropzone.parent_rect = self.rect
    self.dropzone.draw(screen)
