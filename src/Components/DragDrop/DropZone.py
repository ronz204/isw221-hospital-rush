import pygame
from typing import List
from pygame.event import Event
from src.Models.Size import Size
from pygame import draw, Surface
from src.Components.Component import Component
from src.Components.DragDrop.Draggable import Draggable

class DropZone(Component):
  def __init__(self, coords, size: Size = Size(38, 38), padding: int = 10):
    super().__init__(coords=coords, size=size)

    self.padding = padding
    self.object_inside: Component = None

  @property
  def position(self):
    return (self.rect.x, self.rect.y)

  def is_inside(self, component: Component) -> bool:
    return component.rect.colliderect(self.rect)
  
  def update(self) -> None:
    if (self.object_inside):
      if not self.is_inside(self.object_inside):
        self.object_inside = None
      else:
        self.object_inside.rect.topleft = self.position

  def listen(self, event: Event, draggables: List[Draggable]) -> None:
    if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.object_inside is None):
      for drag in draggables:
        if not drag.is_dragging and self.is_inside(drag):
          self.object_inside = drag
          self.object_inside.rect.topleft = self.position
          break

  def draw(self, screen: Surface) -> None:
    color = (100, 200, 100) if self.object_inside else (255, 255, 255)
    draw.rect(screen, color, self.rect, border_radius=6)
    draw.rect(screen, (120, 120, 120), self.rect, width=3, border_radius=6)
