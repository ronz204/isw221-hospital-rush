from enum import Enum

class Scenario(Enum):
  HOME = "Scenarios/HomeScenario.png"
  ROOM = "Scenarios/RoomScenario.png"
  MENU = "Scenarios/MenuScenario.png"
  HISTORY = "Scenarios/HistoryScenario.png"

class Button(Enum):
  EXIT = "Buttons/ExitButton.png"
  BACK = "Buttons/BackButton.png"
  START = "Buttons/StartButton.png"
  HISTORY = "Buttons/HistoryButton.png"

class Character(Enum):
  DOCTOR1 = "Sprites/Doctors/Doctor1.png"
  DOCTOR2 = "Sprites/Doctors/Doctor2.png"
  DOCTOR3 = "Sprites/Doctors/Doctor3.png"
  DOCTOR4 = "Sprites/Doctors/Doctor4.png"

  PATIENT1 = "Sprites/Patients/Patient1.png"
  PATIENT2 = "Sprites/Patients/Patient2.png"
  PATIENT3 = "Sprites/Patients/Patient3.png"
  PATIENT4 = "Sprites/Patients/Patient4.png"

  TRIAGE1 = "Sprites/Triages/Triage1.png"
  TRIAGE2 = "Sprites/Triages/Triage2.png"
  TRIAGE3 = "Sprites/Triages/Triage3.png"