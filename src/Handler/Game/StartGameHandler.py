from src.Components.Scenarios.SceneManager import SceneManager
from src.Components.Scenarios.RoomScenario import RoomScenario

class StartGameHandler:
  def execute(self) -> None:
    SceneManager.switch(RoomScenario())
