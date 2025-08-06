from enum import Enum

class Icon(Enum):
  GAME = "Images/Indicators/HospitalRushIcon.png"

class Scenario(Enum):
  HOME = "Images/Scenarios/HomeScenario.png"
  ROOM = "Images/Scenarios/RoomScenario.png"
  MENU = "Images/Scenarios/MenuScenario.png"
  HISTORY = "Images/Scenarios/HistoryScenario.png"

class Button(Enum):
  EXIT = "Images/Buttons/ExitButton.png"
  BACK = "Images/Buttons/BackButton.png"
  MENU = "Images/Buttons/MenuButton.png"
  START = "Images/Buttons/StartButton.png"
  HISTORY = "Images/Buttons/HistoryButton.png"

class Equipment(Enum):
  STRETCHER = "Images/Sprites/Equipment/Stretcher.png"

class Character(Enum):
  DOCTOR1 = "Images/Sprites/Doctors/Doctor1.png"
  DOCTOR2 = "Images/Sprites/Doctors/Doctor2.png"
  DOCTOR3 = "Images/Sprites/Doctors/Doctor3.png"
  DOCTOR4 = "Images/Sprites/Doctors/Doctor4.png"

  PATIENT1 = "Images/Sprites/Patients/Patient1.png"
  PATIENT2 = "Images/Sprites/Patients/Patient2.png"
  PATIENT3 = "Images/Sprites/Patients/Patient3.png"
  PATIENT4 = "Images/Sprites/Patients/Patient4.png"

  TRIAGE1 = "Images/Sprites/Triages/Triage1.png"
  TRIAGE2 = "Images/Sprites/Triages/Triage2.png"
  TRIAGE3 = "Images/Sprites/Triages/Triage3.png"

class Font(Enum):
  HERCULES = "Fonts/HerculesPixel.otf"
  KARMATIC = "Fonts/KarmaticArcade.ttf"