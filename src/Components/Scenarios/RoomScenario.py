from pygame.sprite import Group
from src.Models.Coord import Coord
from src.Constants.Assets import Scenario, Character
from src.Components.Scenarios.BaseScenario import BaseScenario
from src.Components.Characters.DoctorCharacter import DoctorCharacter
from src.Components.Characters.TriageCharacter import TriageCharacter
from src.Components.Characters.PatientCharacter import PatientCharacter

class RoomScenario(BaseScenario):
  BACKGROUND = Scenario.ROOM

  def __init__(self):
    super().__init__()
    self.characters = Group()

    self.characters.add(
      DoctorCharacter(Coord(30, 30), Character.DOCTOR1),
      DoctorCharacter(Coord(30, 120), Character.DOCTOR2),
      DoctorCharacter(Coord(30, 210), Character.DOCTOR3),
      DoctorCharacter(Coord(30, 300), Character.DOCTOR4),
      
      TriageCharacter(Coord(120, 30), Character.TRIAGE1),
      TriageCharacter(Coord(120, 120), Character.TRIAGE2),)

  def listen(self, event) -> None:
    pass

  def draw(self, screen) -> None:
    super().draw(screen)
    self.characters.draw(screen)