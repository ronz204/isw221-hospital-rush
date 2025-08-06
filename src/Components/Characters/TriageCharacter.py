import pygame
from typing import List
from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Constants.Assets import Character
from src.Components.Equipment.Stretcher import Stretcher
from src.Components.Characters.BaseCharacter import BaseCharacter

class TriageCharacter(BaseCharacter):
  def __init__(self, coords: Coord, image: Character):
    super().__init__(coords=coords, size=Size(55, 55), image=image)

  def listen(self, event, stretchers: List[Stretcher]) -> None:
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      mouse_pos = pygame.mouse.get_pos()

      if self.rect.collidepoint(mouse_pos):
        for stretcher in stretchers:
          if stretcher.needs_repair:
              stretcher.reset_uses()
