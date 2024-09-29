from .Board.board import Board
from .Utility.position import Position
from .Utility.direction import Direction
from .Utility.player import Player
from .MoveCheck.move_checker import MoveChecker, PossibleMoves, BoardState
from typing import List


class MoveService:
    def __init__(self, board: Board, move_checker: MoveChecker) -> None:
        self.board = board
        self.move_checker = move_checker
        self.possible_moves: PossibleMoves = None

    def has_possible_move(self, player: Player) -> bool:
        self.possible_moves = self.move_checker.get_possible_moves(
            BoardState(self.board, player)
        )
        return self.possible_moves
