import os
import sys
import pygame
from src.Core.Constants import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hospital Rush")

clock = pygame.time.Clock()

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, 'src', 'Assets', 'Scenarios', 'HomeScenario.png')

try:
  background_image = pygame.image.load(image_path).convert()
  background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
except pygame.error as e:
  print(f"Error loading background image from {image_path}: {e}")
  sys.exit()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

  screen.blit(background_image, (0, 0))
  
  pygame.display.flip()
  clock.tick(60)
