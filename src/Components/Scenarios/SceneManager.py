from pygame import Surface
from pygame.event import Event
from src.Components.Scenarios.BaseScenario import BaseScenario

class SceneManager:
  CURRENT: BaseScenario

  @staticmethod
  def switch(scenario: BaseScenario):
    SceneManager.CURRENT = scenario

  @staticmethod
  def listen(event: Event):
    SceneManager.CURRENT.listen(event)

  @staticmethod
  def draw(screen: Surface):
    SceneManager.CURRENT.draw(screen)