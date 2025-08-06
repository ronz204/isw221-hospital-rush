import pygame
from pygame import time
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
    self.initial_coords: Coord = coords

    self.in_recovery: bool = False
    self.recovery_start_time: int = 0
    self.recovery_duration: int = 3000

  def can_treat(self, patient_skills: List[Skill]) -> bool:
    return all(skill in self.skills for skill in patient_skills)
  
  def reset_position(self) -> None:
    self.coords = self.initial_coords
    self.rect.topleft = (self.coords.x, self.coords.y)

  def listen(self, event) -> None:
    self.update_recovery()
    if self.in_recovery: return

    if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(mouse.get_pos()):
      self.initial_coords = self.coords
    self.listen_drag(event)

    mouse_pos = mouse.get_pos()
    self.hovered = self.rect.collidepoint(mouse_pos)
    self.update_recovery()

  def update_recovery(self) -> None:
    if self.in_recovery:
      elapsed_time = time.get_ticks() - self.recovery_start_time
      if elapsed_time >= self.recovery_duration:
        self.in_recovery = False
        self.fatigue = 0
  
  def start_recovery(self) -> None:
    self.in_recovery = True
    self.recovery_start_time = time.get_ticks()

  def draw(self, screen) -> None:
    if self.hovered:
      self.draw_info_box(screen)

    if self.in_recovery:
      remaining_time = max(0, (self.recovery_duration - (time.get_ticks() - self.recovery_start_time)) // 1000)
      recovery_surf = AssetHelper.load_font(Font.KARMATIC.value, 12, f"Recuperación {remaining_time}s", (255, 0, 0))
      screen.blit(recovery_surf, (self.coords.x - 50, self.coords.y - 20))

  def increase_fatigue(self) -> None:
    self.fatigue += 1
    if self.fatigue == 2:
      self.start_recovery()
  
  def draw_info_box(self, screen) -> None:
    box_width = 270
    box_height = 90 + 22 * len(self.skills)
    margin_right = 20
    margin_top = 60

    box_x = screen.get_width() - box_width - margin_right
    box_y = margin_top

    bg_color = (245, 245, 255)
    border_color = (59, 61, 96)
    text_color = (30, 30, 30)

    import pygame
    pygame.draw.rect(screen, bg_color, (box_x, box_y, box_width, box_height), border_radius=12)
    pygame.draw.rect(screen, border_color, (box_x, box_y, box_width, box_height), 2, border_radius=12)

    title = "Doctor"
    title_surf = AssetHelper.load_font(Font.HERCULES.value, 22, title, border_color)
    screen.blit(title_surf, (box_x + 16, box_y + 10))

    fatigue_text = f"Fatiga: {self.fatigue}"
    fatigue_surf = AssetHelper.load_font(Font.HERCULES.value, 17, fatigue_text, text_color)
    screen.blit(fatigue_surf, (box_x + 16, box_y + 40))

    skill_y = box_y + 68
    skills_title = AssetHelper.load_font(Font.HERCULES.value, 17, "Habilidades:", text_color)
    screen.blit(skills_title, (box_x + 16, skill_y))
    for idx, skill in enumerate(self.skills):
        skill_surf = AssetHelper.load_font(Font.HERCULES.value, 15, f"- {skill.name}", text_color)
        screen.blit(skill_surf, (box_x + 32, skill_y + 22 + idx * 22))