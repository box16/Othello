from .piece import Piece
from ..Utility.player import Player
from ..Utility.position import Position
from dataclasses import dataclass
from ..Utility.direction import Direction
from typing import List


class InvalidPositionError(Exception):
    pass


@dataclass(frozen=True)
class BoardUpdateCommand:
    player: Player
    place_position: Position
    flippable_directions: List[Direction]


class Board:
    def __init__(self, size=8) -> None:
        self.size = size
        self.pieces = [[Piece() for j in range(self.size)] for i in range(self.size)]
        self.TOP_LEFT = Position(0, 0)
        self.BOTTOM_RIGHT = Position(self.size - 1, self.size - 1)
        self._set_initial_position()

    def _set_initial_position(self) -> None:
        half = int(self.size / 2)
        self._place_piece(Position(half - 1, half), Player.FIRST)
        self._place_piece(Position(half, half - 1), Player.FIRST)
        self._place_piece(Position(half, half), Player.SECOND)
        self._place_piece(Position(half - 1, half - 1), Player.SECOND)

    def _place_piece(self, pos: Position, state: Player) -> None:
        if not pos.is_inside(self.TOP_LEFT, self.BOTTOM_RIGHT):
            raise InvalidPositionError("ボードの範囲外です")

        self.pieces[pos.x][pos.y].place(state)

    def is_empty(self, pos: Position) -> bool:
        if not pos.is_inside(self.TOP_LEFT, self.BOTTOM_RIGHT):
            raise InvalidPositionError("ボードの範囲外です")

        return self.pieces[pos.x][pos.y].is_empty()

    def is_piece_state(self, pos: Position, state: Player) -> bool:
        if not pos.is_inside(self.TOP_LEFT, self.BOTTOM_RIGHT):
            raise InvalidPositionError("ボードの範囲外です")

        return self.pieces[pos.x][pos.y].is_piece_state(state)

    def get_size(self) -> int:
        return self.size

    def update(self, command: BoardUpdateCommand) -> None:
        pass
