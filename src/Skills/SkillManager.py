from typing import Dict
from src.Skills.SkillBase import Skill
from src.Skills.Doctors.Fundamentals import Fundamentals
from src.Skills.Triages.RepairStretcher import RepairStretcher
from src.Skills.Doctors.AdvancedDiagnosis import AdvancedDiagnosis
from src.Skills.Doctors.SurgicalPrecision import SurgicalPrecision

class SkillManager:
  SKILLS: Dict[str, Skill] = {
    "Repair Stretcher": RepairStretcher(),
    "Medical Fundamentals": Fundamentals(),
    "Advanced Diagnosis": AdvancedDiagnosis(),
    "Surgical Precision": SurgicalPrecision(),
  }

  @staticmethod
  def get_skill(name: str) -> Skill | None:
    return SkillManager.SKILLS.get(name)
