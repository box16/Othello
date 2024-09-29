from .MoveCheck.move_check_rules import (
    Empty,
    OpponentPieceAround,
    OpponentPiecesAreFlanked,
)
from .MoveCheck.move_checker import MoveChecker
from .Board.board import Board
from .board_service import BoardService


def create_common_board_checker():
    rules = [Empty(), OpponentPieceAround(), OpponentPiecesAreFlanked()]
    common_checker = MoveChecker(rules)
    return common_checker


def create_common_board_service(board: Board):
    move_checker = create_common_board_checker()
    return BoardService(board, move_checker)
