import pygame
from enum import Enum
from typing import List, Tuple
from pygame.event import Event
from src.Models.Size import Size
from pygame import draw, Surface
from src.Components.Component import Component
from src.Components.DragDrop.Draggable import Draggable

class DropZoneState(Enum):
  EMPTY = (120, 120, 120)
  VALID = (100, 200, 100)
  INVALID = (200, 100, 100)

class DropZone(Component):
  def __init__(self, coords, accepted_type: Draggable, size: Size = Size(38, 38)):
    super().__init__(coords=coords, size=size)

    self.object_inside: Component = None
    self.accepted_type: Draggable = accepted_type

  @property
  def position(self):
    return (self.rect.x, self.rect.y)

  def is_inside(self, component: Component) -> bool:
    return component.rect.colliderect(self.rect)
  
  def center_drag(self, component: Component):
    component.rect.center = self.rect.center

  def is_valid_object(self, draggable: Draggable) -> bool:
    if self.accepted_type is None: return True
    return isinstance(draggable, self.accepted_type)
  
  def get_border_color(self) -> Tuple[int, int, int]:
    if not self.object_inside:
      return DropZoneState.EMPTY.value
    
    if self.is_valid_object(self.object_inside):
      return DropZoneState.VALID.value
    return DropZoneState.INVALID.value

  def update(self) -> None:
    if (self.object_inside):
      if not self.is_inside(self.object_inside):
        self.object_inside = None
      else:
        self.center_drag(self.object_inside)

  def listen(self, event: Event, draggables: List[Draggable]) -> None:
    if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.object_inside is None):
      for drag in draggables:
        if isinstance(drag, Draggable):
          if not drag.is_dragging and self.is_inside(drag):
            self.object_inside = drag
            self.center_drag(self.object_inside)
            break

  def draw(self, screen: Surface) -> None:
    border_color = self.get_border_color()
    draw.rect(screen, border_color, self.rect, width=3, border_radius=6)
