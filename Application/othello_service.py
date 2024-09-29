from Domain.move_service import MoveService
from Domain.turn import Turn
from dataclasses import dataclass
from Domain.Utility.player import Player
from Domain.Utility.position import Position
from Domain.Board.board import Board
from board_data import BoardData
from Domain.MoveCheck.move_checker import Move


@dataclass(frozen=True)
class GameState:
    next_player: Player
    board_data: BoardData


@dataclass(frozen=True)
class MoveData:
    player: Player
    position: Position


class InvalidMoveError(Exception):
    pass


class OthelloService:
    def __init__(self, board: Board, move_service: MoveService, turn: Turn) -> None:
        self.board = board
        self.move_service = move_service
        self.turn = turn

    def get_game_state(self) -> GameState:
        return GameState(self.turn.get_next_player(), BoardData(self.board))

    def update_game(self, move: MoveData) -> None:
        if not self.move_service.is_valid_move(Move(move.player, move.position)):
            raise InvalidMoveError("無効な手です")
