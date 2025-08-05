from pygame.sprite import Group
from src.Models.Coord import Coord
from src.Skills.SkillManager import SkillManager
from src.Constants.Assets import Scenario, Character
from src.Components.Equipment.Stretcher import Stretcher
from src.Components.Scenarios.BaseScenario import BaseScenario
from src.Components.Characters.DoctorCharacter import DoctorCharacter
from src.Components.Characters.TriageCharacter import TriageCharacter
from src.Components.Characters.PatientCharacter import PatientCharacter

class RoomScenario(BaseScenario):
  BACKGROUND = Scenario.ROOM

  def __init__(self):
    super().__init__()
    self.stretchers = Group()
    self.characters = Group()

    advanced_diagnosis = SkillManager.get_skill("Advanced Diagnosis")
    surgical_precision = SkillManager.get_skill("Surgical Precision")

    self.characters.add(
      DoctorCharacter(Coord(490, 160), Character.DOCTOR1, [advanced_diagnosis]),
      DoctorCharacter(Coord(540, 180), Character.DOCTOR2, [surgical_precision]),

      PatientCharacter(Coord(530, 330), Character.PATIENT1, [advanced_diagnosis]),
      PatientCharacter(Coord(560, 380), Character.PATIENT2, [surgical_precision]),

      TriageCharacter(Coord(350, 400), Character.TRIAGE1),)

    self.stretchers.add(
      Stretcher(Coord(290, 190)),
      Stretcher(Coord(110, 300)),)

  def listen(self, event) -> None:
    for character in self.characters:
      character.listen(event)

    for stretcher in self.stretchers:
      stretcher.listen(event, self.characters, list(self.characters.sprites()))

  def draw(self, screen) -> None:
    super().draw(screen)
    self.stretchers.draw(screen)
    self.characters.draw(screen)

    for character in self.characters:
      character.draw(screen)

    for stretcher in self.stretchers:
      stretcher.draw(screen)
