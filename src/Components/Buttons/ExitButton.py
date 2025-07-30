from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Constants.Assets import Button
from src.Components.Buttons.BaseButton import Base
from src.Handler.Game.ExitGameHandler import ExitGameHandler

class ExitButton(Base):
  def __init__(self, coords: Coord):
    super().__init__(coords=coords, size=Size(180, 60), image=Button.EXIT)

  def on_click(self) -> None:
    ExitGameHandler().execute()