from src.Constants.Assets import Scenario
from src.Stores.ScenarioStore import ScenarioStore

class StartGameHandler:
  def execute(self) -> None:
    ScenarioStore.set_scenario(Scenario.MENU)
