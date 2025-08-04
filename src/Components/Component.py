from pygame.event import Event
from pygame import Surface, Rect
from pygame.sprite import Sprite
from src.Models.Size import Size
from src.Models.Coord import Coord

class Component(Sprite):
  def __init__(self, coords: Coord, size: Size):
    super().__init__()
    self.size: Size = size
    self.image: Surface = None
    self.coords: Coord = coords
    self.rect = Rect(self.coords.x, self.coords.y, self.size.width, self.size.height)
  
  def listen(self, event: Event) -> None: pass
  
  def draw(self, screen: Surface) -> None: pass
