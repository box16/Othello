from .MoveCheck.move_check_rules import (
    Empty,
    OpponentPieceAround,
    OpponentPiecesAreFlanked,
)
from .MoveCheck.move_checker import MoveChecker
from .Board.board import Board
from .move_service import MoveService


def create_common_board_checker():
    rules = [Empty(), OpponentPieceAround(), OpponentPiecesAreFlanked()]
    common_checker = MoveChecker(rules)
    return common_checker


def create_common_move_service(board: Board):
    move_checker = create_common_board_checker()
    return MoveService(board, move_checker)
