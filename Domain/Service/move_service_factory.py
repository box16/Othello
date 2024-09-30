from Domain.Model.Board.board import Board
from Domain.Model.Move.move_checker import MoveChecker
from Domain.Model.Move.move_check_rules import (
    Empty,
    OpponentPieceAround,
    OpponentPiecesAreFlanked,
)
from Domain.Service.move_service import MoveService


def create_common_move_service(board: Board):
    return MoveService(
        board, MoveChecker([Empty(), OpponentPieceAround(), OpponentPiecesAreFlanked()])
    )
