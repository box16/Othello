from Domain.Model.Board.board import Board
from Domain.Model.position import Position
from Domain.Model.player import Player
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class BoardData:
    pieces: Tuple[Tuple[Player]]
    size: int

    def __init__(self, board: Board) -> None:
        board_size = board.get_size()
        pieces = self._create_pieces(board, board_size)
        object.__setattr__(self, "pieces", pieces)
        object.__setattr__(self, "size", board_size)

    def _create_pieces(self, board: Board, board_size: int) -> Tuple[Tuple[Player]]:
        return tuple(
            tuple(board.get_state(Position(i, j)) for j in range(board_size))
            for i in range(board_size)
        )

    def __eq__(self, other: "BoardData") -> bool:
        if not isinstance(other, BoardData):
            return False

        return (set(self.pieces) == set(other.pieces)) and (self.size == other.size)
