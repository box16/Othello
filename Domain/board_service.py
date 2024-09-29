from .Board.board import Board
from .Utility.position import Position
from .Utility.direction import Direction
from .Utility.player import Player
from .MoveCheck.move_checker import MoveChecker, PossibleMoves, BoardState
from typing import List
from dataclasses import dataclass


@dataclass(frozen=True)
class BoardUpdateCommand:
    player: Player
    place_position: Position
    flippable_directions: List[Direction]


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

    def update(self, command: BoardUpdateCommand) -> None:
        self.board.place_piece(command.place_position, command.player)
        for direction in command.flippable_directions:
            scalar = 1
            while True:
                target_position = command.place_position + (direction * scalar)
                if self.board.is_piece_state(target_position, command.player):
                    break
                self.board.flip(target_position)
                scalar += 1
