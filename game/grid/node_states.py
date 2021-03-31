from enum import Enum

class State(Enum):
    EMPTY = (0,0,0)
    LINE = (255,255,255)
    RED_FILL = (255,0,0)
    GREEN_FILL = (0,255,0)
    BLUE_FILL = (0,0,255)
    