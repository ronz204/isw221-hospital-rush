from pygame import Surface
from src.Constants.Assets import Scenario
from src.Helpers.AssetHelper import AssetHelper
from src.Constants.Details import WIDTH, HEIGHT

class ScenarioStore:
  SCENARIO: Surface

  @staticmethod
  def set_scenario(scenario: Scenario) -> None:
    ScenarioStore.SCENARIO = AssetHelper.load_image(scenario.value, (WIDTH, HEIGHT))
