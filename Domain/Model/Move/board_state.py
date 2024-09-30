from dataclasses import dataclass
from Domain.Model.player import Player
from Domain.Model.Board.board import Board


@dataclass(frozen=True)
class BoardState:
    board: Board
    player: Player
