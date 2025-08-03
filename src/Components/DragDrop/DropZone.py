from typing import List
from src.Models.Size import Size
from pygame import draw, Surface, Rect
from src.Components.Component import Component

class DropZone:
  def __init__(self, rect: Rect):
    self.parent_rect: Rect = rect

    self.slot_count: int = 2
    self.slot_padding: int = 10
    self.slot_size: Size = Size(38, 38)

    self.objects_inside: List[Component] = []
    self.slot_positions = self.calc_slot_positions()

  def can_accept(self) -> bool:
    return len(self.objects_inside) < self.slot_count
  
  def is_inside(self, component: Component) -> bool:
    return component.rect.colliderect(self.parent_rect)

  def calc_slot_positions(self):
    slot_y = self.parent_rect.y + (self.parent_rect.height - self.slot_size.height) // 2
    positions = [
      (self.parent_rect.x + self.slot_padding, slot_y),
      (self.parent_rect.x + self.parent_rect.width - self.slot_padding - self.slot_size.width, slot_y)
    ]
    return positions
  
  def listen(self) -> None:
    pass
  
  def draw(self, screen: Surface) -> None:
    for pos in self.slot_positions:
      draw.rect(screen, (255, 255, 255), (*pos, *self.slot_size.as_tuple()), border_radius=6)
      draw.rect(screen, (120, 120, 120), (*pos, *self.slot_size.as_tuple()), width=3, border_radius=6)