from enum import Enum


class PieceState(Enum):
    EMPTY = "GREEN"
    PLAYER1 = "BLACK"
    PLAYER2 = "WHITE"

    def opponent(self):
        if self == PieceState.PLAYER1:
            return PieceState.PLAYER2
        elif self == PieceState.PLAYER2:
            return PieceState.PLAYER1
        else:
            return PieceState.EMPTY


class InvalidStateError(Exception):
    pass


class Piece:
    def __init__(self):
        self.state = PieceState.EMPTY

    def place(self, state: PieceState) -> None:
        if self.state != PieceState.EMPTY:
            raise InvalidStateError("既にコマが置かれています")
        if state not in {PieceState.PLAYER1, PieceState.PLAYER2}:
            raise InvalidStateError("設定可能な値ではありません")

        self.state = state

    def flip(self) -> None:
        if self.state == PieceState.EMPTY:
            raise InvalidStateError("空のピースは反転できません")

        self.state = (
            PieceState.PLAYER2
            if self.state == PieceState.PLAYER1
            else PieceState.PLAYER1
        )

    def is_empty(self) -> bool:
        return self.state == PieceState.EMPTY

    def is_piece_state(self, state: PieceState) -> bool:
        return self.state == state
