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
from src.Components.Scenarios.ResultSurfaceBuilder import ResultSurfaceBuilder

class RoomScenario(BaseScenario):
  BACKGROUND = Scenario.ROOM
  
  SUCCESS_COLOR = (34, 139, 34)
  FAILURE_COLOR = (220, 20, 60)
  RESULT_BG_COLOR = (240, 248, 255)
  TEXT_SHADOW_COLOR = (105, 105, 105)
  RESULT_BORDER_COLOR = (70, 130, 180)

  def __init__(self):
    super().__init__()
    self._initialize_game_objects()
    self._initialize_game_state()
    self._initialize_characters()

  def _initialize_game_objects(self) -> None:
    self.triages = Group()
    self.stretchers = Group()
    self.characters = Group()

  def _initialize_game_state(self) -> None:
    self.game_over = False
    self.time_limit = 60000
    self.start_time = time.get_ticks()
    self.result_surface = None
    self.menu_button = None

  def _initialize_characters(self) -> None:
    advanced_diagnosis = SkillManager.get_skill("Advanced Diagnosis")
    surgical_precision = SkillManager.get_skill("Surgical Precision")

    # Doctores
    self.characters.add(
      DoctorCharacter(Coord(490, 160), Character.DOCTOR1, [advanced_diagnosis]),
      DoctorCharacter(Coord(540, 180), Character.DOCTOR2, [surgical_precision])
    )
    
    # Pacientes
    self.characters.add(
      PatientCharacter(Coord(530, 330), Character.PATIENT1, [advanced_diagnosis]),
      PatientCharacter(Coord(560, 380), Character.PATIENT2, [surgical_precision])
    )
    
    # Triage
    self.triages.add(
      TriageCharacter(Coord(350, 400), Character.TRIAGE1)
    )

    # Camillas
    self.stretchers.add(
      Stretcher(Coord(290, 190)),
      Stretcher(Coord(110, 300))
    )

  def listen(self, event) -> None:
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      if self.game_over and self.menu_button:
        self.menu_button.on_event(event)

    if not self.game_over:
      for character in self.characters:
        character.listen(event)

      for triage in self.triages:
        triage.listen(event, self.stretchers)

      for stretcher in self.stretchers:
        stretcher.listen(event, self.characters, list(self.characters.sprites()))

  def update(self) -> None:
    if not self.game_over:
      self._check_game_conditions()

  def _check_game_conditions(self) -> None:
    elapsed_time = time.get_ticks() - self.start_time
    if elapsed_time > self.time_limit:
      self.end_game()
      return
    
    patients_remaining = len([c for c in self.characters if isinstance(c, PatientCharacter)])
    if patients_remaining == 0:
      self.end_game()

  def draw(self, screen) -> None:
    super().draw(screen)
    
    if not self.game_over:
      self._draw_game_elements(screen)
      self.draw_timer(screen)
    else:
      self._draw_game_over_screen(screen)

  def _draw_game_elements(self, screen) -> None:
    self.triages.draw(screen)
    self.stretchers.draw(screen)
    self.characters.draw(screen)

    for character in self.characters:
      character.draw(screen)

    for stretcher in self.stretchers:
      stretcher.draw(screen)

  def _draw_game_over_screen(self, screen) -> None:
    if self.result_surface:
      surface_x = (screen.get_width() - self.result_surface.get_width()) // 2
      surface_y = (screen.get_height() - self.result_surface.get_height()) // 2
      screen.blit(self.result_surface, (surface_x, surface_y))
    
    if self.menu_button:
      self.menu_button.draw(screen)

  def end_game(self) -> None:
    if self.game_over: return
      
    self.game_over = True
    patients_remaining = len([c for c in self.characters if isinstance(c, PatientCharacter)])
    total_patients = 2
    patients_treated = total_patients - patients_remaining
    
    HistoryManager.save_game(patients_treated=patients_treated, max_wave=1)    
    self._create_result_surface(patients_remaining == 0, patients_treated, patients_remaining)


  def _create_result_surface(self, victory: bool, treated: int, remaining: int) -> None:
    self.result_surface = ResultSurfaceBuilder.build(
      width=500,
      height=300,
      victory=victory,
      treated=treated,
      remaining=remaining,
      success_color=self.SUCCESS_COLOR,
      failure_color=self.FAILURE_COLOR,
      bg_color=self.RESULT_BG_COLOR,
      border_color=self.RESULT_BORDER_COLOR,
      text_shadow_color=self.TEXT_SHADOW_COLOR)

  def _create_menu_button(self, screen) -> None:
    button_width = 180 
    button_x = (screen.get_width() - button_width) // 2
    button_y = 400
    self.menu_button = MenuButton(Coord(button_x, button_y))

  def _draw_game_over_screen(self, screen) -> None:
    if self.result_surface:
      surface_x = (screen.get_width() - self.result_surface.get_width()) // 2
      surface_y = (screen.get_height() - self.result_surface.get_height()) // 2
      screen.blit(self.result_surface, (surface_x, surface_y))

      if not self.menu_button:
        self._create_menu_button(screen)
    if self.menu_button:
      self.menu_button.draw(screen)

  def draw_timer(self, screen) -> None:
    elapsed_time = time.get_ticks() - self.start_time
    remaining_time = max(0, (self.time_limit - elapsed_time) // 1000)
    
    if remaining_time <= 0 and not self.game_over:
      self.end_game()
      return

    if remaining_time > 30:
      timer_color = (255, 255, 255)
    elif remaining_time > 10:
      timer_color = (255, 255, 0)
    else:
      timer_color = (255, 0, 0)
    
    timer_text = f"Tiempo: {remaining_time}s"
    timer_surface = AssetHelper.load_font(Font.HERCULES.value, 22, timer_text, timer_color)
    
    timer_x = screen.get_width() - timer_surface.get_width() - 20
    screen.blit(timer_surface, (timer_x, 20))

  def reset(self) -> None:
    self._initialize_game_objects()
    self._initialize_game_state()
    self._initialize_characters()
