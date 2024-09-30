from dataclasses import dataclass
from Domain.Service.move_service import MoveService
from Domain.Model.Turn.turn import Turn
from Domain.Model.Board.board import Board, BoardUpdateCommand
from Domain.Model.Move.move import Move
from Application.board_data import BoardData
from Application.game_data import GameData
from Application.move_data import MoveData


class InvalidMoveError(Exception):
    pass


class OthelloService:
    def __init__(self, board: Board, move_service: MoveService, turn: Turn) -> None:
        self.board = board
        self.move_service = move_service
        self.turn = turn

    def get_game_data(self) -> GameData:
        return GameData(self.turn.get_next_player(), BoardData(self.board))

    def update_game(self, move_data: MoveData) -> None:
        move = Move(move_data.player, move_data.position)
        if not self.move_service.is_valid_move(move):
            raise InvalidMoveError("無効な手です")

        command = BoardUpdateCommand(
            move.player, move.position, self.move_service.get_flippable_move(move)
        )
        self.board.update(command)
        self.turn.update()
