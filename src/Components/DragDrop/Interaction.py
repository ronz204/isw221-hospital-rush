from src.Components.DragDrop.DropZone import DropZone
from src.Components.Characters.DoctorCharacter import DoctorCharacter
from src.Components.Characters.PatientCharacter import PatientCharacter

class Interaction:
  def __init__(self, doctor_zone: DropZone, patient_zone: DropZone):
    self.doctor_zone = doctor_zone
    self.patient_zone = patient_zone

  def validate_interaction(self) -> None:
    if self.doctor_zone.object_inside and self.patient_zone.object_inside:
      doctor = self.doctor_zone.object_inside
      patient = self.patient_zone.object_inside
      
      if isinstance(doctor, DoctorCharacter) and isinstance(patient, PatientCharacter):
        if doctor.can_treat(patient.required_skills):
          print(f"El doctor puede tratar al paciente.")
        else:
          print(f"El doctor NO puede tratar al paciente.")