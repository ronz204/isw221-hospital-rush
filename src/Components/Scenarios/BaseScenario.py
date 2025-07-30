from pygame import Surface
from pygame.event import Event

class BaseScenario:
  def listen(self, event: Event) -> None:
    raise NotImplementedError()

  def draw(self, screen: Surface) -> None:
    raise NotImplementedError()
  