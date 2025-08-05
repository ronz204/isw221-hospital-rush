from src.Skills.SkillBase import Skill

class RepairStretcher(Skill):
  def __init__(self):
    name: str = "Repair Strecher"
    description: str = "Skill to repair stretchers in the hospital."
    super().__init__(name=name, description=description)
