from src.Constants.Assets import Scenario
from src.Components.Scenarios.BaseScenario import BaseScenario

class RoomScenario(BaseScenario):
  BACKGROUND = Scenario.ROOM

  def __init__(self):
    super().__init__()

  def listen(self, event) -> None:
    pass

  def draw(self, screen) -> None:
    super().draw(screen)