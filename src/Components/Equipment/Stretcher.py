from typing import List
from pygame import mouse
from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Helpers.AssetHelper import AssetHelper
from src.Constants.Assets import Equipment, Font
from src.Components.DragDrop.DropZone import DropZone
from src.Components.DragDrop.Draggable import Draggable
from src.Components.Equipment.BaseEquipment import BaseEquipment
from src.Components.Characters.DoctorCharacter import DoctorCharacter
from src.Components.Characters.PatientCharacter import PatientCharacter

class Stretcher(BaseEquipment):
  def __init__(self, coords: Coord):
    super().__init__(coords=coords, size=Size(150, 90))

    self.uses: int = 0
    self.hovered: bool = False
    self.image = AssetHelper.load_image(Equipment.STRETCHER.value, self.size.as_tuple())
  
    doctor_dropzone_coords = Coord(self.rect.x + 1, self.rect.y + (self.rect.height - 38) // 2)
    stretcher_dropzone_coords = Coord(self.rect.x + (self.rect.width - 38) // 2, self.rect.y + (self.rect.height - 38) // 2)

    self.dropzones = [
      DropZone(coords=doctor_dropzone_coords, accepted_type=DoctorCharacter),
      DropZone(coords=stretcher_dropzone_coords, accepted_type=PatientCharacter),]

  def listen(self, event, draggables: List[Draggable]) -> None:
    mouse_pos = mouse.get_pos()
    self.hovered = self.rect.collidepoint(mouse_pos)

    for zone in self.dropzones:
      zone.listen(event, draggables)
      zone.update()

  def draw(self, screen) -> None:
    if self.hovered:
      severity_surf = AssetHelper.load_font(Font.KARMATIC.value, 18, f"Usos {self.uses}")
      screen.blit(severity_surf, (10, 50))

    for zone in self.dropzones:
      zone.draw(screen)