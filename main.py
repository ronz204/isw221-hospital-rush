import sys
import pygame
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

SceneManager.SCENARIOS = {
  "home": HomeScenario(),
  "menu": MenuScenario(),
  "room": RoomScenario(),
  "history": HistoryScenario()}
SceneManager.switch("room")

while True:
  for event in pygame.event.get():
    SceneManager.listen(event)
    
    if (event.type == pygame.QUIT):
      pygame.quit()
      sys.exit()

  SceneManager.draw(screen)
  pygame.display.flip()
  clock.tick(60)
