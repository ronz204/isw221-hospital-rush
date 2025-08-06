from typing import List
from src.Models.History import History

class HistoryManager:
  COUNTER: int = 0
  HISTORY: List[History] = []

  @staticmethod
  def save_game(patients_treated: int, max_wave: int) -> None:
    HistoryManager.COUNTER += 1
    game = History(
      max_wave=max_wave,
      patients_treated=patients_treated,
      game_number=HistoryManager.COUNTER,)
    HistoryManager.HISTORY.append(game)

  @staticmethod
  def get_history() -> List[History]:
    return HistoryManager.HISTORY
