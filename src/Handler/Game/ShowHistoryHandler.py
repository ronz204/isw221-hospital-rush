from src.Constants.Assets import Scenario
from src.Stores.ScenarioStore import ScenarioStore

class ShowHistoryHandler:
  def execute(self) -> None:
    ScenarioStore.set_scenario(Scenario.HISTORY)