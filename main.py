import sys
import pygame

from src.Models.Coord import Coord
from src.Constants.Assets import Scenario
from src.Constants.Details import WIDTH, HEIGHT, CAPTION
from src.Stores.ScenarioStore import ScenarioStore

from src.Components.Buttons import StartButton, ExitButton, HistoryButton


pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption(CAPTION)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
ScenarioStore.set_scenario(Scenario.HOME)


btn_exit = ExitButton(Coord(200, 300))
btn_start = StartButton(Coord(200, 200))
btn_history = HistoryButton(Coord(200, 400))

buttons = pygame.sprite.Group()
buttons.add(btn_start, btn_exit, btn_history)


while True:
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      pygame.quit()
      sys.exit()

    if (event.type == pygame.MOUSEBUTTONDOWN):
      if (event.button == 1):

        for btn in buttons:
          btn.on_event(event)

  screen.blit(ScenarioStore.SCENARIO, (0, 0))
  buttons.draw(screen)
  pygame.display.flip()
  clock.tick(60)
