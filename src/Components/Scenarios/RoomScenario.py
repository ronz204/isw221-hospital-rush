from pygame.sprite import Group
from pygame import mouse, Surface
from src.Models.Coord import Coord
from src.Helpers.AssetHelper import AssetHelper
from src.Components.Equipment.Stretcher import Stretcher
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

    self.characters.add(
      DoctorCharacter(Coord(490, 160), Character.DOCTOR1),
      DoctorCharacter(Coord(540, 180), Character.DOCTOR2),
      
      PatientCharacter(Coord(530, 330), Character.PATIENT1),
      PatientCharacter(Coord(560, 380), Character.PATIENT2),)

    self.stretchers.add(
      Stretcher(Coord(290, 190)),
      Stretcher(Coord(110, 300)),)

  def listen(self, event) -> None:
    for character in self.characters:
      character.listen(event)

    for stretcher in self.stretchers:
      stretcher.listen(event, list(self.characters.sprites()))

  def draw(self, screen) -> None:
    super().draw(screen)
    self.stretchers.draw(screen)
    self.characters.draw(screen)

    for character in self.characters:
      character.draw(screen)

    for stretcher in self.stretchers:
      stretcher.draw(screen)
