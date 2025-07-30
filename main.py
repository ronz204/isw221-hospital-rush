import sys
import pygame
from src.Constants.Details import WIDTH, HEIGHT, CAPTION

from src.Components.Scenarios.HomeScenario import HomeScenario
from src.Components.Scenarios.SceneManager import SceneManager

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption(CAPTION)
screen = pygame.display.set_mode((WIDTH, HEIGHT))


home_scenario = HomeScenario()
SceneManager.switch(home_scenario)


while True:
  for event in pygame.event.get():
    SceneManager.listen(event)
    
    if (event.type == pygame.QUIT):
      pygame.quit()
      sys.exit()

  SceneManager.draw(screen)
  pygame.display.flip()
  clock.tick(60)
