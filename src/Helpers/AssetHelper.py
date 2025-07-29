import os
import pygame
from typing import Optional, Tuple

class AssetHelper:
  BASE_ASSETS_DIR = os.path.join(os.path.dirname(__file__), '..', 'Assets')

  @staticmethod
  def get_asset_path(path: str) -> str:
    return os.path.join(AssetHelper.BASE_ASSETS_DIR, path)
  
  @staticmethod
  def load_image(path: str, scale: Optional[Tuple[int, int]]) -> pygame.Surface:
    asset_path = AssetHelper.get_asset_path(path)
    image = pygame.image.load(asset_path).convert_alpha()

    if scale:
      image = pygame.transform.scale(image, scale)
    return image