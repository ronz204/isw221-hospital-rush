from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Constants.Assets import Button
from src.Components.Buttons.BaseButton import BaseButton
from src.Components.Scenarios.SceneManager import SceneManager

class BackButton(BaseButton):
  def __init__(self, coords: Coord, scene: str):
    self.previus: str = scene
    super().__init__(coords=coords, size=Size(40, 40), image=Button.BACK)

  def on_click(self) -> None:
    SceneManager.switch(self.previus)