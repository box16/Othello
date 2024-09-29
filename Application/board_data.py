from Domain.Board.board import Board
from Domain.Utility.position import Position
from Domain.Utility.player import Player
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class BoardData:
    pieces: Tuple[Tuple[Player]]

    def __init__(self, board: Board) -> None:
        board_size = board.get_size()
        pieces = self._create_pieces(board, board_size)
        object.__setattr__(self, "pieces", pieces)

    def _create_pieces(self, board: Board, board_size: int) -> Tuple[Tuple[Player]]:
        return tuple(
            tuple(board.get_state(Position(i, j)) for j in range(board_size))
            for i in range(board_size)
        )
