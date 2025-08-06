from typing import List
from pygame import mouse
from src.Models.Size import Size
from src.Models.Coord import Coord
from src.Helpers.AssetHelper import AssetHelper
from src.Constants.Assets import Equipment, Font
from src.Components.DragDrop.DropZone import DropZone
from src.Components.DragDrop.Draggable import Draggable
from src.Components.DragDrop.Interaction import Interaction
from src.Components.Equipment.BaseEquipment import BaseEquipment
from src.Components.Characters.DoctorCharacter import DoctorCharacter
from src.Components.Characters.PatientCharacter import PatientCharacter

class Stretcher(BaseEquipment):
  def __init__(self, coords: Coord):
    super().__init__(coords=coords, size=Size(150, 90))

    self.uses: int = 0
    self.hovered: bool = False
    self.needs_repair: bool = False
    self.image = AssetHelper.load_image(Equipment.STRETCHER.value, self.size.as_tuple())
  
    doctor_dropzone_coords = Coord(self.rect.x + 1, self.rect.y + (self.rect.height - 38) // 2)
    stretcher_dropzone_coords = Coord(self.rect.x + (self.rect.width - 38) // 2, self.rect.y + (self.rect.height - 38) // 2)

    self.doctor_zone = DropZone(coords=doctor_dropzone_coords, accepted_type=DoctorCharacter)
    self.patient_zone = DropZone(coords=stretcher_dropzone_coords, accepted_type=PatientCharacter)

    self.dropzones = [self.doctor_zone, self.patient_zone]
    self.interaction = Interaction(self.doctor_zone, self.patient_zone)

  def reset_uses(self) -> None:
    self.uses = 0
    self.needs_repair = False

  def listen(self, event, characters, draggables: List[Draggable]) -> None:
    mouse_pos = mouse.get_pos()
    self.hovered = self.rect.collidepoint(mouse_pos)
    if self.needs_repair: return

    for zone in self.dropzones:
      zone.listen(event, draggables)
      zone.update()

    self.interaction.validate_interaction()
    self.interaction.update_treatment(self, characters)

    if self.uses >= 2: self.needs_repair = True

  def draw(self, screen) -> None:
    self.interaction.draw_treatment_indicator(screen, self)

    if self.hovered:
      self.draw_info_box(screen)

    if self.needs_repair:
      repair_surf = AssetHelper.load_font(Font.KARMATIC.value, 12, "Reparar", (200,86,75))
      screen.blit(repair_surf, (self.coords.x + 20, self.coords.y - 10))

    for zone in self.dropzones:
      zone.draw(screen)

  def draw_info_box(self, screen) -> None:
    doctor_box_height = 90 + 22 * len(getattr(self, 'skills', []))
    patient_box_height = 90 + 22 * len(getattr(self, 'required_skills', []))
    margin_right = 20
    margin_top = 60
    margin_between = 24

    box_width = 250
    box_height = 100
    box_x = screen.get_width() - box_width - margin_right
    box_y = margin_top + doctor_box_height + margin_between + patient_box_height + margin_between

    bg_color = (245, 245, 255)
    border_color = (200, 86, 75)
    text_color = (30, 30, 30)

    import pygame
    pygame.draw.rect(screen, bg_color, (box_x, box_y, box_width, box_height), border_radius=12)
    pygame.draw.rect(screen, border_color, (box_x, box_y, box_width, box_height), 2, border_radius=12)

    title = "Camilla"
    title_surf = AssetHelper.load_font(Font.HERCULES.value, 22, title, border_color)
    screen.blit(title_surf, (box_x + 16, box_y + 10))

    usos_text = f"Usos: {self.uses}/2"
    usos_surf = AssetHelper.load_font(Font.HERCULES.value, 17, usos_text, text_color)
    screen.blit(usos_surf, (box_x + 16, box_y + 40))

    if self.needs_repair:
      repair_surf = AssetHelper.load_font(Font.HERCULES.value, 16, "¡Necesita reparación!", border_color)
      screen.blit(repair_surf, (box_x + 16, box_y + 66))
