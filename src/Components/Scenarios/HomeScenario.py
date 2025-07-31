import pygame
from src.Constants.Assets import Scenario
from src.Components.Scenarios.BaseScenario import BaseScenario
from src.Components.Scenarios.SceneManager import SceneManager

class HomeScenario(BaseScenario):
  BACKGROUND = Scenario.HOME

  def __init__(self):
    super().__init__()

  def listen(self, event) -> None:
    if (event.type == pygame.KEYDOWN):
      if (event.key == pygame.K_RETURN):
        SceneManager.switch("menu")

  def draw(self, screen) -> None:
    super().draw(screen)
