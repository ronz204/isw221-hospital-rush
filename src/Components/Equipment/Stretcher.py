from typing import List
from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Constants.Assets import Equipment
from src.Helpers.AssetHelper import AssetHelper
from src.Components.DragDrop.DropZone import DropZone
from src.Components.DragDrop.Draggable import Draggable
from src.Components.Equipment.BaseEquipment import BaseEquipment

class Stretcher(BaseEquipment):
  def __init__(self, coords: Coord):
    super().__init__(coords=coords, size=Size(150, 90))
    self.image = AssetHelper.load_image(Equipment.STRETCHER.value, self.size.as_tuple())

    left_zone_coords = Coord(self.rect.x + 10, self.rect.y + (self.rect.height - 38) // 2)
    right_zone_coords = Coord(self.rect.x + self.rect.width - 10 - 38, self.rect.y + (self.rect.height - 38) // 2)

    self.dropzones = [
      DropZone(coords=left_zone_coords),
      DropZone(coords=right_zone_coords),]

  def listen(self, event, draggables: List[Draggable]) -> None:
    for zone in self.dropzones:
      zone.listen(event, draggables)
      zone.update()

  def draw(self, screen) -> None:
    for zone in self.dropzones:
      zone.rect.x = self.rect.x + (10 if zone is self.dropzones[0] else self.rect.width - 10 - 38)
      zone.rect.y = self.rect.y + (self.rect.height - 38) // 2
      zone.draw(screen)