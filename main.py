import sys
import pygame

from src.Constants.Assets import Scenarios
from src.Helpers.AssetHelper import AssetHelper
from src.Constants.Details import WIDTH, HEIGHT, CAPTION

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption(CAPTION)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = AssetHelper.load_image(Scenarios.HOME.value, (WIDTH, HEIGHT))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

  screen.blit(background, (0, 0))
  pygame.display.flip()
  clock.tick(60)
