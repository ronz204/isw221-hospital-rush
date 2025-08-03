import pygame
from typing import Tuple
from pygame.event import Event

class Draggable:
  def __init__(self):
    self.drag_offset_x: int = 0
    self.drag_offset_y: int = 0
    self.is_dragging: bool = False

  def is_hovered(self, position: Tuple[int, int]) -> bool:
    return self.rect.collidepoint(position)

  def start_drag(self, position: Tuple[int, int]) -> None:
    self.is_dragging = True
    mouse_x, mouse_y = position

    self.drag_offset_x = mouse_x - self.rect.x
    self.drag_offset_y = mouse_y - self.rect.y

  def stop_drag(self) -> None:
    self.is_dragging = False

  def handle_drag(self, position) -> None:
    if (self.is_dragging):
      mouse_x, mouse_y = position
      self.rect.x = mouse_x - self.drag_offset_x
      self.rect.y = mouse_y - self.drag_offset_y

  def listen_drag(self, event: Event) -> None:
    if (event.type == pygame.MOUSEBUTTONDOWN):
      if (event.button == 1 and self.is_hovered(event.pos)):
        self.start_drag(event.pos)

    elif (event.type == pygame.MOUSEBUTTONUP):
      if (event.button == 1):
        self.stop_drag()

    elif (event.type == pygame.MOUSEMOTION):
      self.handle_drag(event.pos)
