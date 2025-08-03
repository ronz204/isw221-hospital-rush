import pygame
from typing import List
from pygame.event import Event
from src.Models.Size import Size
from pygame import draw, Surface, Rect
from src.Components.Component import Component
from src.Components.DragDrop.Draggable import Draggable

class DropZone:
  def __init__(self, rect: Rect):
    self.parent_rect = rect
    self.slot_count: int = 2
    self.slot_padding: int = 10
    self.slot_size: Size = Size(38, 38)
    self.objects_inside: List[Component] = []

  @property
  def can_accept(self):
    return len(self.objects_inside) < self.slot_count

  @property
  def slot_positions(self):
    y = self.parent_rect.y + (self.parent_rect.height - self.slot_size.height) // 2
    return [
      (self.parent_rect.x + self.slot_padding, y),
      (self.parent_rect.x + self.parent_rect.width - self.slot_padding - self.slot_size.width, y)]
  
  def is_inside(self, component: Component) -> bool:
    return component.rect.colliderect(self.parent_rect)
  
  def update_positions(self):
    for index, drag in enumerate(self.objects_inside):
      if index < len(self.slot_positions):
        drag.rect.topleft = self.slot_positions[index]

  def update_slots(self):
    self.objects_inside = [obj for obj in self.objects_inside if self.is_inside(obj)]
    self.update_positions()
  
  def listen(self, event: Event, draggables: List[Draggable]) -> None:
    if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.can_accept):
      for drag in draggables:
        if not drag.is_dragging and drag not in self.objects_inside and self.is_inside(drag):
          self.objects_inside.append(drag)
          self.update_positions()
          break
  
  def draw(self, screen: Surface) -> None:
    for i, pos in enumerate(self.slot_positions):
      color = (100, 200, 100) if i < len(self.objects_inside) else (255, 255, 255)
      draw.rect(screen, color, (*pos, *self.slot_size.as_tuple()), border_radius=6)
      draw.rect(screen, (120, 120, 120), (*pos, *self.slot_size.as_tuple()), width=3, border_radius=6)