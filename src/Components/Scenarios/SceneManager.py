from typing import Dict
from pygame import Surface
from pygame.event import Event
from src.Components.Scenarios.BaseScenario import BaseScenario

class SceneManager:
  CURRENT: BaseScenario
  SCENARIOS: Dict[str, BaseScenario] = {}

  @staticmethod
  def switch(scenario: str):
    SceneManager.CURRENT = SceneManager.SCENARIOS[scenario]
    if hasattr(SceneManager.CURRENT, "reset"):
      SceneManager.CURRENT.reset()

  @staticmethod
  def listen(event: Event):
    SceneManager.CURRENT.listen(event)

  @staticmethod
  def draw(screen: Surface):
    SceneManager.CURRENT.draw(screen)