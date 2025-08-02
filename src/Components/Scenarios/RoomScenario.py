from pygame.sprite import Group
from src.Models.Coord import Coord
from src.Helpers.AssetHelper import AssetHelper
from src.Constants.Assets import Scenario, Character, Font
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

    """ self.characters.add(
      DoctorCharacter(Coord(430, 160), Character.DOCTOR1),
      DoctorCharacter(Coord(500, 180), Character.DOCTOR2),
      
      TriageCharacter(Coord(330, 340), Character.TRIAGE1),
      TriageCharacter(Coord(380, 350), Character.TRIAGE2),
      
      PatientCharacter(Coord(530, 330), Character.PATIENT1),
      PatientCharacter(Coord(560, 380), Character.PATIENT2),
      PatientCharacter(Coord(585, 300), Character.PATIENT3),
      PatientCharacter(Coord(610, 350), Character.PATIENT4),) """

  def listen(self, event) -> None:
    pass

  def draw(self, screen) -> None:
    super().draw(screen)
    self.characters.draw(screen)
    self.stretchers.draw(screen)
