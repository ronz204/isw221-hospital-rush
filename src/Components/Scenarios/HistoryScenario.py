import pygame
from pygame.sprite import Group
from src.Models.Coord import Coord
from src.Constants.Assets import Scenario
from src.Components.Buttons.BackButton import BackButton
from src.Components.Scenarios.BaseScenario import BaseScenario

class HistoryScenario(BaseScenario):
  BACKGROUND = Scenario.HISTORY

  def __init__(self):
    super().__init__()
    self.buttons = Group()

    self.buttons.add(BackButton(Coord(20, 20), scene="menu"))

  def listen(self, event) -> None:
    if (event.type == pygame.MOUSEBUTTONDOWN):
      if (event.button == 1):

        for button in self.buttons:
          button.on_event(event)

  def draw(self, screen) -> None:
    super().draw(screen)
    self.buttons.draw(screen)