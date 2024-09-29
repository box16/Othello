from .Board.board import Board
from .Utility.position import Position
from .Utility.player import Player
from .MoveCheck.move_checker import MoveChecker, PossibleMoves, BoardState


class BoardService:
    def __init__(self, board: Board, move_checker: MoveChecker) -> None:
        self.board = board
        self.move_checker = move_checker
        self._set_initial_position()

    def _set_initial_position(self) -> None:
        half = int(self.board.get_size() / 2)
        self.board.place_piece(Position(half - 1, half), Player.FIRST)
        self.board.place_piece(Position(half, half - 1), Player.FIRST)
        self.board.place_piece(Position(half, half), Player.SECOND)
        self.board.place_piece(Position(half - 1, half - 1), Player.SECOND)

    def get_possible_moves(self, player: Player) -> PossibleMoves:
        return self.move_checker.get_possible_moves(BoardState(self.board, player))
