from typing import List
from pygame import mouse
from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Skills.SkillBase import Skill
from src.Helpers.AssetHelper import AssetHelper
from src.Constants.Assets import Character, Font
from src.Components.DragDrop.Draggable import Draggable
from src.Components.Characters.BaseCharacter import BaseCharacter

class DoctorCharacter(BaseCharacter, Draggable):
  def __init__(self, coords: Coord, image: Character, skills: List[Skill]):
    super().__init__(coords=coords, size=Size(55, 55), image=image)
    Draggable.__init__(self)

    self.fatigue: int = 0
    self.hovered: bool = False
    self.skills: List[Skill] = skills

  def can_treat(self, patient_skills: List[Skill]) -> bool:
    return all(skill in self.skills for skill in patient_skills)

  def listen(self, event) -> None:
    self.listen_drag(event)

    mouse_pos = mouse.get_pos()
    self.hovered = self.rect.collidepoint(mouse_pos)

  def draw(self, screen) -> None:
    if self.hovered:
      fatigue_surf = AssetHelper.load_font(Font.KARMATIC.value, 18, f"Fatiga {self.fatigue}", (59,61,96))
      screen.blit(fatigue_surf, (10, 35))