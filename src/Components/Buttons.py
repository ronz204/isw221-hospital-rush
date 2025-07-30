from pygame.event import Event
from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Constants.Assets import Button
from src.Components.Component import Component
from src.Helpers.AssetHelper import AssetHelper

from src.Handler.Game.ExitGameHandler import ExitGameHandler
from src.Handler.Game.StartGameHandler import StartGameHandler
from src.Handler.Game.ShowHistoryHandler import ShowHistoryHandler

exitGameHandler = ExitGameHandler()
startGameHandler = StartGameHandler()
showHistoryHandler = ShowHistoryHandler()

class Base(Component):
  def __init__(self, coords: Coord, size: Size, image: Button):
    super().__init__(coords=coords, size=size)
    self.image = AssetHelper.load_image(image.value, size.as_tuple())

  def on_event(self, event: Event) -> None:
    if (self.rect.collidepoint(event.pos)):
      self.handling()

  def on_click(self) -> None:
    raise NotImplementedError()


class StartButton(Base):
  def __init__(self, coords: Coord):
    super().__init__(coords=coords, size=Size(180, 60), image=Button.START)

  def on_click(self) -> None:
    startGameHandler.execute()


class ExitButton(Base):
  def __init__(self, coords: Coord):
    super().__init__(coords=coords, size=Size(180, 60), image=Button.EXIT)

  def on_click(self) -> None:
    exitGameHandler.execute()


class HistoryButton(Base):
  def __init__(self, coords: Coord):
    super().__init__(coords=coords, size=Size(180, 60), image=Button.HISTORY)

  def on_click(self) -> None:
    showHistoryHandler.execute()
