from src.Skills.SkillBase import Skill

class EmotionalSupport(Skill):
  def __init__(self):
    name = "Emotional Support"
    description = "Skill to provide emotional support to patients."
    super().__init__(name=name, description=description)
