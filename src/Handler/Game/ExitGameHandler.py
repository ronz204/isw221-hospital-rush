import sys
import pygame

class ExitGameHandler:
  def execute(self) -> None:
    pygame.quit()
    sys.exit()
