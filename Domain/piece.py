from enum import Enum


class Player(Enum):
    EMPTY = "GREEN"
    FIRST = "BLACK"
    SECOND = "WHITE"

    def opponent(self):
        if self == Player.FIRST:
            return Player.SECOND
        elif self == Player.SECOND:
            return Player.FIRST
        else:
            return Player.EMPTY


class InvalidStateError(Exception):
    pass


class Piece:
    def __init__(self):
        self.state = Player.EMPTY

    def place(self, state: Player) -> None:
        if self.state != Player.EMPTY:
            raise InvalidStateError("既にコマが置かれています")
        if state not in {Player.FIRST, Player.SECOND}:
            raise InvalidStateError("設定可能な値ではありません")

        self.state = state

    def flip(self) -> None:
        if self.state == Player.EMPTY:
            raise InvalidStateError("空のピースは反転できません")

        self.state = Player.SECOND if self.state == Player.FIRST else Player.FIRST

    def is_empty(self) -> bool:
        return self.state == Player.EMPTY

    def is_piece_state(self, state: Player) -> bool:
        return self.state == state
