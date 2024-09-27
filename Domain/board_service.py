from .board import Board
from .position import Position
from .piece import PieceState
from .move_checker import MoveChecker, Move


class BoardService:
    def __init__(self, board: Board, move_checker: MoveChecker) -> None:
        self.board = board
        self.move_checker = move_checker

    def is_valid_move(self, move: Move) -> bool:
        return self.move_checker.is_valid(move)
