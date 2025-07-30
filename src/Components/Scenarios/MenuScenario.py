import pygame
from pygame.sprite import Group
from src.Models.Coord import Coord
from src.Constants.Assets import Scenario
from src.Constants.Details import WIDTH, HEIGHT
from src.Helpers.AssetHelper import AssetHelper
from src.Components.Buttons.ExitButton import ExitButton
from src.Components.Buttons.StartButton import StartButton
from src.Components.Buttons.HistoryButton import HistoryButton
from src.Components.Scenarios.BaseScenario import BaseScenario

class MenuScenario(BaseScenario):
  def __init__(self):
    super().__init__()
    self.buttons = Group()

    self.buttons.add(
      ExitButton(Coord(200, 200)),
      StartButton(Coord(200, 300)),
      HistoryButton(Coord(200, 400),))

  def listen(self, event):
    if (event.type == pygame.MOUSEBUTTONDOWN):
      if (event.button == 1):

        for button in self.buttons:
          button.on_event(event)

  def draw(self, screen) -> None:
    screen.blit(AssetHelper.load_image(Scenario.MENU.value, (WIDTH, HEIGHT)), (0, 0))
    self.buttons.draw(screen)
