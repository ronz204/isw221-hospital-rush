from src.Constants.Assets import Scenario
from src.Constants.Details import WIDTH, HEIGHT
from src.Helpers.AssetHelper import AssetHelper
from src.Components.Scenarios.BaseScenario import BaseScenario

class HistoryScenario(BaseScenario):
  def __init__(self):
    super().__init__()

  def listen(self, event) -> None:
    pass

  def draw(self, screen) -> None:
    screen.blit(AssetHelper.load_image(Scenario.HISTORY.value, (WIDTH, HEIGHT)), (0, 0))