import pygame
from src.Constants.Assets import Scenario
from src.Constants.Details import WIDTH, HEIGHT
from src.Helpers.AssetHelper import AssetHelper
from src.Components.Scenarios.BaseScenario import BaseScenario

from src.Components.Scenarios.SceneManager import SceneManager
from src.Components.Scenarios.MenuScenario import MenuScenario

class HomeScenario(BaseScenario):
  def __init__(self):
    super().__init__()

  def listen(self, event) -> None:
    if (event.type == pygame.KEYDOWN):
      if (event.key == pygame.K_RETURN):
        SceneManager.switch("menu")

  def draw(self, screen) -> None:
    screen.blit(AssetHelper.load_image(Scenario.HOME.value, (WIDTH, HEIGHT)), (0, 0))
