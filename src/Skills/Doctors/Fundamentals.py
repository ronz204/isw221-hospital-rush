from src.Skills.SkillBase import Skill

class Fundamentals(Skill):
  def __init__(self):
    name: str = "Fundamentals"
    description: str = "Basic medical knowledge for all doctors."
    super().__init__(name=name, description=description)
