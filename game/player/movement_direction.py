from enum import Enum

class MovementDirection(Enum):
    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)