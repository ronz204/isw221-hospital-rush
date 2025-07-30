from typing import Tuple

class Coord:
  def __init__(self, x: int, y: int):
    self.x: int = x
    self.y: int = y

  def as_tuple(self) -> Tuple[int, int]:
    return (self.x, self.y)
