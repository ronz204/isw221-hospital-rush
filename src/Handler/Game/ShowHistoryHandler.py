from src.Components.Scenarios.SceneManager import SceneManager
from src.Components.Scenarios.HistoryScenario import HistoryScenario

class ShowHistoryHandler:
  def execute(self) -> None:
    SceneManager.switch("history")