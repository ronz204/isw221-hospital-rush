from typing import Tuple

class Size:
  def __init__(self, width: int, height: int):
    self.width: int = width
    self.height: int = height

  def as_tuple(self) -> Tuple[int, int]:
    return (self.width, self.height)
