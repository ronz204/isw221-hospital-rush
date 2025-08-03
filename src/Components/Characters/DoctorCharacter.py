from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Constants.Assets import Character
from src.Components.DragDrop.Draggable import Draggable
from src.Components.Characters.BaseCharacter import BaseCharacter

class DoctorCharacter(BaseCharacter, Draggable):
  def __init__(self, coords: Coord, image: Character):
    super().__init__(coords=coords, size=Size(55, 55), image=image)
    Draggable.__init__(self)

  def listen(self, event) -> None:
    self.listen_drag(event)