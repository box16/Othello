from .board import Board
from .position import Position
from .piece import PieceState


class BoardService:
    def __init__(self, board: Board) -> None:
        self.board = board

    def set_initial_position(self) -> None:
        half = int(self.size / 2)
        self.board.place_piece(Position(half - 1, half), PieceState.PLAYER1)
        self.board.place_piece(Position(half, half - 1), PieceState.PLAYER1)
        self.board.place_piece(Position(half, half), PieceState.PLAYER2)
        self.board.place_piece(Position(half - 1, half - 1), PieceState.PLAYER2)
