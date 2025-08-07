from typing import Dict
from src.Skills.SkillBase import Skill
from src.Skills.Triages.RepairStretcher import RepairStretcher
from src.Skills.Doctors.EmotionalSupport import EmotionalSupport
from src.Skills.Doctors.AdvancedDiagnosis import AdvancedDiagnosis
from src.Skills.Doctors.SurgicalPrecision import SurgicalPrecision

class SkillManager:
  SKILLS: Dict[str, Skill] = {
    "Repair Stretcher": RepairStretcher(),
    "Emotional Support": EmotionalSupport(),
    "Advanced Diagnosis": AdvancedDiagnosis(),
    "Surgical Precision": SurgicalPrecision(),
  }

  @staticmethod
  def get_skill(name: str) -> Skill | None:
    return SkillManager.SKILLS.get(name)
