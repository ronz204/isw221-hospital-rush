from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Constants.Assets import Character
from src.Components.Characters.BaseCharacter import BaseCharacter

class PatientCharacter(BaseCharacter):
  def __init__(self, coords: Coord, image: Character):
    super().__init__(coords=coords, size=Size(45, 55), image=image)