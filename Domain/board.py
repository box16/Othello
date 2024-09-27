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
        self._set_initial_position()

    def _set_initial_position(self) -> None:
        half = int(self.size / 2)
        self.place_piece(Position(half - 1, half), PieceState.PLAYER1)
        self.place_piece(Position(half, half - 1), PieceState.PLAYER1)
        self.place_piece(Position(half, half), PieceState.PLAYER2)
        self.place_piece(Position(half - 1, half - 1), PieceState.PLAYER2)

    def place_piece(self, pos: Position, state: PieceState) -> None:
        if not pos.is_inside(self.TOP_LEFT, self.BOTTOM_RIGHT):
            raise InvalidPositionError("ボードの範囲外です")

        self.pieces[pos.x][pos.y].place(state)

    def is_empty(self, pos: Position) -> bool:
        if not pos.is_inside(self.TOP_LEFT, self.BOTTOM_RIGHT):
            raise InvalidPositionError("ボードの範囲外です")

        return self.pieces[pos.x][pos.y].is_empty()

    def is_piece_state(self, pos: Position, state: PieceState) -> bool:
        if not pos.is_inside(self.TOP_LEFT, self.BOTTOM_RIGHT):
            raise InvalidPositionError("ボードの範囲外です")

        return self.pieces[pos.x][pos.y].is_piece_state(state)
