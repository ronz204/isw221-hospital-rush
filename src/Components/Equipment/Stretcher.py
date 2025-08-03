from typing import List
from pygame import Surface, draw
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

    self.dropzone = DropZone(self.rect)

  def listen(self, event, draggables: List[Draggable]) -> None:
    self.dropzone.listen(event, draggables)
    self.dropzone.update_slots()

  def draw(self, screen) -> None:
    self.dropzone.parent_rect = self.rect
    self.dropzone.draw(screen)
