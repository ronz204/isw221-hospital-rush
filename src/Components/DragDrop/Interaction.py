from typing import Dict
from pygame import time, Surface
from src.Constants.Assets import Font
from src.Helpers.AssetHelper import AssetHelper
from src.Components.DragDrop.DropZone import DropZone
from src.Components.Characters.DoctorCharacter import DoctorCharacter
from src.Components.Characters.PatientCharacter import PatientCharacter

DURATIONS: Dict[str, int] = {
  "Baja": 2,
  "Media": 4,
  "Alta": 6,
}

class Interaction:
  def __init__(self, doctor_zone: DropZone, patient_zone: DropZone):
    self.current_doctor = None
    self.current_patient = None

    self.doctor_zone = doctor_zone
    self.patient_zone = patient_zone

    self.treatment_end_time = 0
    self.treatment_in_progress = False

  def validate_interaction(self) -> None:
    if self.doctor_zone.object_inside and self.patient_zone.object_inside:
      doctor = self.doctor_zone.object_inside
      patient = self.patient_zone.object_inside
      
      if isinstance(doctor, DoctorCharacter) and isinstance(patient, PatientCharacter):
        if not doctor.can_treat(patient.required_skills):
          doctor.reset_position()
          self.doctor_zone.object_inside = None
        else:
          self.start_treatment(doctor, patient)

  def start_treatment(self, doctor: DoctorCharacter, patient: PatientCharacter) -> None:
    if not self.treatment_in_progress:
      treatment_duration = DURATIONS[patient.severity.value]
      self.treatment_end_time = time.get_ticks() + treatment_duration * 1000
      self.treatment_in_progress = True
      self.current_doctor = doctor
      self.current_patient = patient
  
  def update_treatment(self, stretcher, characters) -> None:
    if self.treatment_in_progress and time.get_ticks() >= self.treatment_end_time:
      self.current_doctor.increase_fatigue()
      stretcher.uses += 1

      self.current_doctor.reset_position()
      self.doctor_zone.object_inside = None
      self.patient_zone.object_inside = None

      if self.current_patient in characters:
        characters.remove(self.current_patient)

      self.current_doctor = None
      self.current_patient = None
      self.treatment_in_progress = False

  def draw_treatment_indicator(self, screen: Surface, stretcher) -> None:
    if not self.treatment_in_progress: return
    remaining_time = max(0, (self.treatment_end_time - time.get_ticks()) // 1000)
    indicator_surf = AssetHelper.load_font(Font.KARMATIC.value, 12, f"Tratamiento {remaining_time}s", (0, 255, 0))
    screen.blit(indicator_surf, (stretcher.coords.x, stretcher.coords.y - 20))
