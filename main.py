import sys
import pygame
from src.Constants.Assets import Icon
from src.Helpers.AssetHelper import AssetHelper
from src.Constants.Details import WIDTH, HEIGHT, CAPTION
from src.Components.Scenarios.SceneManager import SceneManager
from src.Components.Scenarios.HomeScenario import HomeScenario
from src.Components.Scenarios.MenuScenario import MenuScenario
from src.Components.Scenarios.RoomScenario import RoomScenario
from src.Components.Scenarios.HistoryScenario import HistoryScenario


pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption(CAPTION)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

icon = AssetHelper.load_image(Icon.GAME.value, (50, 50))
pygame.display.set_icon(icon)

SceneManager.SCENARIOS = {
  "home": HomeScenario(),
  "menu": MenuScenario(),
  "room": RoomScenario(),
  "history": HistoryScenario()}
SceneManager.switch("home")

while True:
  for event in pygame.event.get():
    SceneManager.listen(event)
    
    if (event.type == pygame.QUIT):
      pygame.quit()
      sys.exit()

  SceneManager.draw(screen)
  pygame.display.flip()
  clock.tick(60)
