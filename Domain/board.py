from .piece import Piece, PieceState
from .position import Position


class InvalidPositionError(Exception):
    pass


class Board:
    def __init__(self, size=8) -> None:
        self.size = size
        self.pieces = [[Piece() for j in range(self.size)] for i in range(self.size)]
        self.TOP_LEFT = Position(0, 0)
        self.BOTTOM_RIGHT = Position(self.size - 1, self.size - 1)

    def place_piece(self, pos: Position, state: PieceState):
        if not pos.is_inside(self.TOP_LEFT, self.BOTTOM_RIGHT):
            raise InvalidPositionError("ボードの範囲外です")

        self.pieces[pos.x][pos.y].place(state)
