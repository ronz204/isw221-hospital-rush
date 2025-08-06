import pygame
from pygame.sprite import Group
from pygame import Surface, time
from src.Models.Coord import Coord
from src.Helpers.AssetHelper import AssetHelper
from src.Skills.SkillManager import SkillManager
from src.Helpers.HistoryHelper import HistoryManager
from src.Components.Equipment.Stretcher import Stretcher
from src.Components.Buttons.MenuButton import MenuButton
from src.Constants.Assets import Scenario, Character, Font
from src.Components.Scenarios.BaseScenario import BaseScenario
from src.Components.Characters.DoctorCharacter import DoctorCharacter
from src.Components.Characters.TriageCharacter import TriageCharacter
from src.Components.Characters.PatientCharacter import PatientCharacter

class RoomScenario(BaseScenario):
  BACKGROUND = Scenario.ROOM

  def __init__(self):
    super().__init__()
    self.triages = Group()
    self.stretchers = Group()
    self.characters = Group()

    self.game_over = False
    self.time_limit = 5000
    self.result_surface = None
    self.start_time = time.get_ticks()

    advanced_diagnosis = SkillManager.get_skill("Advanced Diagnosis")
    surgical_precision = SkillManager.get_skill("Surgical Precision")

    self.characters.add(
      DoctorCharacter(Coord(490, 160), Character.DOCTOR1, [advanced_diagnosis]),
      DoctorCharacter(Coord(540, 180), Character.DOCTOR2, [surgical_precision]),

      PatientCharacter(Coord(530, 330), Character.PATIENT1, [advanced_diagnosis]),
      PatientCharacter(Coord(560, 380), Character.PATIENT2, [surgical_precision]),)
    
    self.triages.add(
      TriageCharacter(Coord(350, 400), Character.TRIAGE1))

    self.stretchers.add(
      Stretcher(Coord(290, 190)),
      Stretcher(Coord(110, 300)),)

  def listen(self, event) -> None:
    if (event.type == pygame.MOUSEBUTTONDOWN):
      if (event.button == 1):
        self.menu_button.on_event(event)

    for character in self.characters:
      character.listen(event)

    for triage in self.triages:
      triage.listen(event, self.stretchers)

    for stretcher in self.stretchers:
      stretcher.listen(event, self.characters, list(self.characters.sprites()))

  def draw(self, screen) -> None:
    super().draw(screen)
    self.triages.draw(screen)
    self.stretchers.draw(screen)
    self.characters.draw(screen)

    for character in self.characters:
      character.draw(screen)

    for stretcher in self.stretchers:
      stretcher.draw(screen)

    if not self.game_over:
      self.draw_timer(screen)
    else:
      screen.blit(self.result_surface, (240, 140))
      self.menu_button.draw(screen)

  def end_game(self) -> None:
    self.game_over = True
    patients_remaining = len([c for c in self.characters if isinstance(c, PatientCharacter)])
    result_text = "Ganaste" if patients_remaining == 0 else "Perdiste"

    HistoryManager.save_game(patients_treated=len(self.characters) - patients_remaining, max_wave=1)

    self.result_surface = Surface((400, 200))
    self.result_surface.fill((0, 0, 0))
    result_text_surface = AssetHelper.load_font(Font.KARMATIC.value, 36, result_text, (255, 255, 255))
    self.result_surface.blit(result_text_surface, (200 - result_text_surface.get_width() // 2, 50))

    self.menu_button = MenuButton(Coord(200 - 90, 120))

  def draw_timer(self, screen) -> None:
    elapsed_time = time.get_ticks() - self.start_time
    remaining_time = max(0, (self.time_limit - elapsed_time) // 1000)

    timer_surface = AssetHelper.load_font(Font.KARMATIC.value, 22, f"Tiempo: {remaining_time}s", (255, 255, 255))
    screen.blit(timer_surface, (480 - timer_surface.get_width() // 2, 20))

    if remaining_time == 0:
      self.end_game()
