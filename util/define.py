NUM_OF_HORSE_INFO_IN_PAGE = 10

SCREEN_SHOT_X1 = 650
SCREEN_SHOT_Y1 = 0
SCREEN_SHOT_X2 = 1250
SCREEN_SHOT_Y2 = 1080

# const
MATCHED_THRESHOLD = 0.85

# Training status
STATE_UNKNOWN = 0
STATE_PRE_RACE = 1
STATE_NORMAL_RACE = 2
STATE_SUMMER = 3
STATE_FINAL = 4

# POS
RACE_POS = (1075, 870, 1200, 950)
FALL_SCREEN_POS = (0, 0, 1920, 1080)
SKILL_POS = (1070, 760, 1200, 850) # skill

## Ability
SPEED_POS = (720, 700, 770, 720)
ENDURANCE_POS = (810, 700, 860, 720)
POWER_POS = (900, 700, 950, 720)
VOLITION_POS = (990, 700, 1040, 720)
INTELLIGENCE_POS = (1070, 700, 1120, 720)
## List for abilities
ABILITY_POS_LIST = [SPEED_POS, ENDURANCE_POS, POWER_POS, VOLITION_POS, INTELLIGENCE_POS]
ABILITY_NAME_LIST = ["SPEED", "ENDURANCE", "POWER", "VOLITION", "INTELLIGENCE"]

## Ability which increase by training
TRAINING_SPEED_POS = (700, 650, 750, 680)
TRAINING_ENDURANCE_POS = (790, 650, 840, 680)
TRAINING_POWER_POS = (880, 650, 930, 680)
TRAINING_VOLITION_POS = (970, 650, 1020, 680)
TRAINING_INTELLIGENCE_POS = (1040, 650, 1090, 680)
TRAINING_SKILL_POINT_POS = (1150, 650, 1200, 680)

TRAINING_ABILITY_POS_LIST = [
    TRAINING_SPEED_POS, 
    TRAINING_ENDURANCE_POS, 
    TRAINING_POWER_POS, TRAINING_VOLITION_POS, 
    TRAINING_INTELLIGENCE_POS, 
    TRAINING_SKILL_POINT_POS,
]
TRAINING_ABILITY_NAME_LIST = [
    "TRAINING_SPEED", 
    "TRAINING_ENDURANCE", 
    "TRAINING_POWER", 
    "TRAINING_VOLITION", 
    "TRAINING_INTELLIGENCE", 
    "TRAINING_SKILL_POINT",
]

# OFFSET
OFFEST = (660, 30)

# RANGE
TRAINING_UPPER_LEFT_RANGE = (870, 775)
TRAINING_LOWER_RIGHT_RANGE = (1010, 840)
TRAINING_BACK_LEFT_RANGE = (700, 970)
TRAINING_BACK_RIGHT_RANGE = (760, 1010)

TRAINING_SPEED_UPPER_LEFT_RANGE = (720, 850)
TRAINING_SPEED_LOWER_RIGHT_RANGE = (770, 900)
TRAINING_ENDURANCE_UPPER_LEFT_RANGE = (820, 850)
TRAINING_ENDURANCE_LOWER_RIGHT_RANGE = (870, 900)
TRAINING_POWER_UPPER_LEFT_RANGE = (920, 850)
TRAINING_POWER_LOWER_RIGHT_RANGE = (970, 900)
TRAINING_VOLITION_UPPER_LEFT_RANGE = (1020, 850)
TRAINING_VOLITION_LOWER_RIGHT_RANGE = (1070, 900)
TRAINING_INTELLIGENCE_UPPER_LEFT_RANGE = (1120, 850)
TRAINING_INTELLIGENCE_LOWER_RIGHT_RANGE = (1170, 900)

## List of RANGE 
TRAINING_ABILITY_UPPER_LEFT_RANGE = [
    TRAINING_SPEED_UPPER_LEFT_RANGE,
    TRAINING_ENDURANCE_UPPER_LEFT_RANGE,
    TRAINING_POWER_UPPER_LEFT_RANGE,
    TRAINING_VOLITION_UPPER_LEFT_RANGE,
    TRAINING_INTELLIGENCE_UPPER_LEFT_RANGE,
]

TRAINING_ABILITY_LOWER_RIGHT_RANGE = [
    TRAINING_SPEED_LOWER_RIGHT_RANGE,
    TRAINING_ENDURANCE_LOWER_RIGHT_RANGE,
    TRAINING_POWER_LOWER_RIGHT_RANGE,
    TRAINING_VOLITION_LOWER_RIGHT_RANGE,
    TRAINING_INTELLIGENCE_LOWER_RIGHT_RANGE,
]

# Folder
DATA_FOLDER = "data"

# File
TEMP_FILE = "tmp.png"
SKILL_GRAY_FILE = f"./{DATA_FOLDER}/page/SKILL_gray.png"
LOCK_GRAY_FILE = f"./{DATA_FOLDER}/state/LOCK_gray.png"

# Test File