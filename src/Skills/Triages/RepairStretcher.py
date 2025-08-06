from src.Skills.SkillBase import Skill

class RepairStretcher(Skill):
  def __init__(self):
    name = "Repair Stretcher"
    description = "Skill to repair stretchers in the hospital."
    super().__init__(name=name, description=description)

  def use(self, stretchers):
    for stretcher in stretchers:
      if hasattr(stretcher, "needs_repair") and stretcher.needs_repair:
        stretcher.reset_uses()
