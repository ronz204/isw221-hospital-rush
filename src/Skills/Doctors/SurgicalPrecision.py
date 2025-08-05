from src.Skills.SkillBase import Skill

class SurgicalPrecision(Skill):
  def __init__(self):
    name: str = "Surgical Precision"
    description: str = "Skill to perform surgeries with high accuracy and minimal errors."
    super().__init__(name=name, description=description)
