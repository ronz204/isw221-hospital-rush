import pygame
from pygame import Surface
from src.Helpers.AssetHelper import AssetHelper
from src.Constants.Assets import Font

class ResultSurfaceBuilder:
  @staticmethod
  def build(
    width: int,
    height: int,
    victory: bool,
    treated: int,
    remaining: int,
    success_color,
    failure_color,
    bg_color,
    border_color,
    text_shadow_color
  ) -> Surface:
    surface = Surface((width, height))
    surface.fill(bg_color)
        
    pygame.draw.rect(surface, border_color, (0, 0, width, height), 8)
    pygame.draw.rect(surface, (255, 255, 255), (8, 8, width-16, height-16), 4)

    result_text = "¡MISION COMPLETADA!" if victory else "TIEMPO AGOTADO"
    title_color = success_color if victory else failure_color
        
    title_shadow = AssetHelper.load_font(Font.KARMATIC.value, 32, result_text, text_shadow_color)
    title_surface = AssetHelper.load_font(Font.KARMATIC.value, 32, result_text, title_color)
        
    title_x = (width - title_surface.get_width()) // 2
    surface.blit(title_shadow, (title_x + 2, 52))
    surface.blit(title_surface, (title_x, 50))

    stats_y = 110
    stats_color = (60, 60, 60)
        
    treated_text = f"Pacientes tratados: {treated}"
    treated_surface = AssetHelper.load_font(Font.KARMATIC.value, 20, treated_text, stats_color)
    treated_x = (width - treated_surface.get_width()) // 2
    surface.blit(treated_surface, (treated_x, stats_y))
        
    if remaining > 0:
      remaining_text = f"Pacientes restantes: {remaining}"
      remaining_surface = AssetHelper.load_font(Font.KARMATIC.value, 20, remaining_text, stats_color)
      remaining_x = (width - remaining_surface.get_width()) // 2
      surface.blit(remaining_surface, (remaining_x, stats_y + 35))

      motivation_y = stats_y + (80 if remaining > 0 else 45)

    if victory:
      motivation_text = "¡Excelente trabajo, Doctor!"
      motivation_color = success_color
    else:
      motivation_text = "¡Intentalo de nuevo!"
      motivation_color = failure_color
        
      motivation_surface = AssetHelper.load_font(Font.KARMATIC.value, 18, motivation_text, motivation_color)
      motivation_x = (width - motivation_surface.get_width()) // 2
      surface.blit(motivation_surface, (motivation_x, motivation_y))

    return surface
