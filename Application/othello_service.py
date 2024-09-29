from Domain.move_service import MoveService
from Domain.turn import Turn
from dataclasses import dataclass
from Domain.Utility.player import Player
from Domain.Utility.position import Position
from Domain.Board.board import Board, BoardUpdateCommand
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

    def update_game(self, _move: MoveData) -> None:
        move = Move(_move.player, _move.position)
        if not self.move_service.is_valid_move(move):
            raise InvalidMoveError("無効な手です")

        command = BoardUpdateCommand(
            move.player, move.position, self.move_service.get_flippable_move(move)
        )
        self.board.update(command)
        self.turn.update()
