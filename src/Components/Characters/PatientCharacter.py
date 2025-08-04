import random
from enum import Enum
from pygame import mouse
from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Helpers.AssetHelper import AssetHelper
from src.Constants.Assets import Character, Font
from src.Components.DragDrop.Draggable import Draggable
from src.Components.Characters.BaseCharacter import BaseCharacter

class PatientSeverity(Enum):
  LOW = "Baja"
  MEDIUM = "Media"
  HIGH = "Alta"

class PatientCharacter(BaseCharacter, Draggable):
  def __init__(self, coords: Coord, image: Character):
    super().__init__(coords=coords, size=Size(45, 55), image=image)
    Draggable.__init__(self)

    self.hovered: bool = False
    self.severity = random.choice(list(PatientSeverity))

  def listen(self, event) -> None:
    self.listen_drag(event)

    mouse_pos = mouse.get_pos()
    self.hovered = self.rect.collidepoint(mouse_pos)

  def draw(self, screen) -> None:
    if self.hovered:
      severity_surf = AssetHelper.load_font(Font.KARMATIC.value, 18, f"Severidad {self.severity.value}")
      screen.blit(severity_surf, (10, 30))