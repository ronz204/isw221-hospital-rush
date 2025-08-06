import random
from enum import Enum
from typing import List
from pygame import mouse
from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Skills.SkillBase import Skill
from src.Helpers.AssetHelper import AssetHelper
from src.Constants.Assets import Character, Font
from src.Components.DragDrop.Draggable import Draggable
from src.Components.Characters.BaseCharacter import BaseCharacter

class PatientSeverity(Enum):
  LOW = "Baja"
  MEDIUM = "Media"
  HIGH = "Alta"

class PatientCharacter(BaseCharacter, Draggable):
  def __init__(self, coords: Coord, image: Character, required_skills: List[Skill]):
    super().__init__(coords=coords, size=Size(45, 55), image=image)
    Draggable.__init__(self)

    self.hovered: bool = False
    self.required_skills: List[Skill] = required_skills
    self.severity = random.choice(list(PatientSeverity))

  def listen(self, event) -> None:
    self.listen_drag(event)

    mouse_pos = mouse.get_pos()
    self.hovered = self.rect.collidepoint(mouse_pos)

  def draw(self, screen) -> None:
    if self.hovered:
      self.draw_info_box(screen)
  
  def draw_info_box(self, screen) -> None:
    doctor_box_height = 90 + 22 * len(getattr(self, 'skills', []))
    margin_right = 20
    margin_top = 60
    margin_between = 24

    box_width = 280
    box_height = 90 + 22 * len(self.required_skills)
    box_x = screen.get_width() - box_width - margin_right
    box_y = margin_top + doctor_box_height + margin_between

    bg_color = (255, 250, 240)
    border_color = (246, 157, 57)
    text_color = (30, 30, 30)

    import pygame
    pygame.draw.rect(screen, bg_color, (box_x, box_y, box_width, box_height), border_radius=12)
    pygame.draw.rect(screen, border_color, (box_x, box_y, box_width, box_height), 2, border_radius=12)

    title = "Paciente"
    title_surf = AssetHelper.load_font(Font.HERCULES.value, 22, title, border_color)
    screen.blit(title_surf, (box_x + 16, box_y + 10))

    severity_text = f"Gravedad: {self.severity.value}"
    severity_surf = AssetHelper.load_font(Font.HERCULES.value, 17, severity_text, text_color)
    screen.blit(severity_surf, (box_x + 16, box_y + 40))

    req_y = box_y + 68
    req_title = AssetHelper.load_font(Font.HERCULES.value, 17, "Requiere:", text_color)
    screen.blit(req_title, (box_x + 16, req_y))
    for idx, skill in enumerate(self.required_skills):
        skill_surf = AssetHelper.load_font(Font.HERCULES.value, 15, f"- {skill.name}", text_color)
        screen.blit(skill_surf, (box_x + 32, req_y + 22 + idx * 22))
