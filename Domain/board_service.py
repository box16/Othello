from .board import Board
from .position import Position
from .piece import PieceState
from .move_checker import MoveChecker, Move


class BoardService:
    def __init__(self, board: Board, move_checker: MoveChecker) -> None:
        self.board = board
        self.move_checker = move_checker

    def set_initial_position(self) -> None:
        half = int(self.size / 2)
        self.board.place_piece(Position(half - 1, half), PieceState.PLAYER1)
        self.board.place_piece(Position(half, half - 1), PieceState.PLAYER1)
        self.board.place_piece(Position(half, half), PieceState.PLAYER2)
        self.board.place_piece(Position(half - 1, half - 1), PieceState.PLAYER2)

    def is_valid_move(self, move: Move) -> bool:
        return self.move_checker.is_valid(move)
