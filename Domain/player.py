from enum import Enum


class Player(Enum):
    NONE = "GREEN"
    FIRST = "BLACK"
    SECOND = "WHITE"

    def opponent(self):
        if self == Player.FIRST:
            return Player.SECOND
        elif self == Player.SECOND:
            return Player.FIRST
        else:
            return Player.NONE
