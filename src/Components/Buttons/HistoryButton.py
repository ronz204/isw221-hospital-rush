from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Constants.Assets import Button
from src.Components.Buttons.BaseButton import Base
from src.Components.Scenarios.SceneManager import SceneManager

class HistoryButton(Base):
  def __init__(self, coords: Coord):
    super().__init__(coords=coords, size=Size(180, 60), image=Button.HISTORY)

  def on_click(self) -> None:
    SceneManager.switch("history")
