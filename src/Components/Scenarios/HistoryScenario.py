import pygame
from pygame.sprite import Group
from src.Models.Coord import Coord
from src.Helpers.AssetHelper import AssetHelper
from src.Constants.Assets import Scenario, Font
from src.Components.Buttons.BackButton import BackButton
from src.Components.Scenarios.BaseScenario import BaseScenario
from src.Helpers.HistoryHelper import HistoryManager

class HistoryScenario(BaseScenario):
  BACKGROUND = Scenario.HISTORY

  def __init__(self):
    super().__init__()
    self.buttons = Group()
    self.buttons.add(BackButton(Coord(20, 20), scene="menu"))

  def listen(self, event) -> None:
    if (event.type == pygame.MOUSEBUTTONDOWN):
      if (event.button == 1):
        for button in self.buttons:
          button.on_event(event)

  def draw(self, screen) -> None:
    super().draw(screen)
    self.buttons.draw(screen)
    self.draw_history_table(screen)

  def draw_history_table(self, screen) -> None:
    row_height = 48
    col_widths = [160, 340, 260]
    col_margin = 28
    cell_padding = 22

    headers = ["Partida", "Pacientes Atendidos", "Máxima Ronda"]
    font_size = 28

    font_color = (30, 30, 30)
    header_bg = (200, 220, 255)
    row_bg = (240, 248, 255)
    alt_row_bg = (220, 235, 245)
    border_color = (120, 150, 200)

    table_width = sum(col_widths) + col_margin * (len(col_widths) - 1)
    x = (screen.get_width() - table_width) // 2
    y = 120

    history = HistoryManager.get_history()
    table_height = row_height * (len(history) + 1)
    overlay = pygame.Surface((table_width + 32, table_height + 24), pygame.SRCALPHA)
    overlay.fill((255, 255, 255, 200))
    screen.blit(overlay, (x - 16, y - 12))

    col_x = x
    for i, header in enumerate(headers):
      rect = pygame.Rect(col_x, y, col_widths[i], row_height)
      pygame.draw.rect(screen, header_bg, rect, border_radius=10)
      pygame.draw.rect(screen, border_color, rect, 2, border_radius=10)
      text_surface = AssetHelper.load_font(Font.HERCULES.value, font_size, header, font_color)
      text_x = rect.x + cell_padding
      text_y = rect.y + (rect.height - text_surface.get_height()) // 2
      screen.blit(text_surface, (text_x, text_y))
      col_x += col_widths[i] + col_margin

    for idx, game in enumerate(history):
      row_y = y + row_height * (idx + 1)
      bg_color = row_bg if idx % 2 == 0 else alt_row_bg
      col_x = x
      for col, value in enumerate([game.game_number, game.patients_treated, game.max_wave]):
        rect = pygame.Rect(col_x, row_y, col_widths[col], row_height)
        pygame.draw.rect(screen, bg_color, rect, border_radius=10)
        pygame.draw.rect(screen, border_color, rect, 1, border_radius=10)
        text_surface = AssetHelper.load_font(Font.KARMATIC.value, font_size - 2, str(value), font_color)
        text_x = rect.x + cell_padding
        text_y = rect.y + (rect.height - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))
        col_x += col_widths[col] + col_margin
