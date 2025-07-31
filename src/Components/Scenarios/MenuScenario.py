import pygame
from pygame.sprite import Group
from src.Models.Coord import Coord
from src.Constants.Assets import Scenario
from src.Components.Buttons.ExitButton import ExitButton
from src.Components.Buttons.StartButton import StartButton
from src.Components.Buttons.HistoryButton import HistoryButton
from src.Components.Scenarios.BaseScenario import BaseScenario

class MenuScenario(BaseScenario):
  BACKGROUND = Scenario.MENU

  def __init__(self):
    super().__init__()
    self.buttons = Group()

    self.buttons.add(
      ExitButton(Coord(150, 250)),
      StartButton(Coord(400, 250)),
      HistoryButton(Coord(650, 250),))

  def listen(self, event):
    if (event.type == pygame.MOUSEBUTTONDOWN):
      if (event.button == 1):

        for button in self.buttons:
          button.on_event(event)

  def draw(self, screen) -> None:
    super().draw(screen)
    self.buttons.draw(screen)
