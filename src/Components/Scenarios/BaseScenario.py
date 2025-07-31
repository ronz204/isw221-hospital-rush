from pygame import Surface
from pygame.event import Event
from src.Constants.Assets import Scenario
from src.Helpers.AssetHelper import AssetHelper
from src.Constants.Details import WIDTH, HEIGHT

class BaseScenario:
  BACKGROUND: Scenario

  def listen(self, event: Event) -> None:
    raise NotImplementedError()

  def draw(self, screen: Surface) -> None:
    screen.blit(AssetHelper.load_image(self.BACKGROUND.value, (WIDTH, HEIGHT)), (0,0))
  