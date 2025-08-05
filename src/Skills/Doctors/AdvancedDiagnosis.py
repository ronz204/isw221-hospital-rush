from src.Skills.SkillBase import Skill

class AdvancedDiagnosis(Skill):
  def __init__(self):
    name: str = "Advanced Diagnosis"
    description: str = "Skill to perform advanced medical diagnoses with precision."
    super().__init__(name=name, description=description)
