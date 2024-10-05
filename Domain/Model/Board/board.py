from functools import wraps
from Domain.Model.Board.piece import Piece
from Domain.Model.player import Player
from Domain.Model.position import Position
from Domain.Model.Board.board_update_command import BoardUpdateCommand


class InvalidPositionError(Exception):
    pass


class Board:
    def __init__(self, size=8) -> None:
        self.size = size
        self.pieces = [[Piece() for j in range(self.size)] for i in range(self.size)]
        self.TOP_LEFT = Position(0, 0)
        self.BOTTOM_RIGHT = Position(self.size - 1, self.size - 1)
        self._set_initial_position()

    def _set_initial_position(self) -> None:
        half = int(self.size / 2)
        self._place_piece(Position(half - 1, half), Player.FIRST)
        self._place_piece(Position(half, half - 1), Player.FIRST)
        self._place_piece(Position(half, half), Player.SECOND)
        self._place_piece(Position(half - 1, half - 1), Player.SECOND)

    def check_position(func):
        @wraps(func)
        def wrapper(self, pos: Position, *args, **kwargs):
            if not pos.is_inside(self.TOP_LEFT, self.BOTTOM_RIGHT):
                raise InvalidPositionError(f"ボードの範囲外です : {str(pos)}")
            return func(self, pos, *args, **kwargs)

        return wrapper

    @check_position
    def _place_piece(self, pos: Position, state: Player) -> None:
        self.pieces[pos.x][pos.y].place(state)

    @check_position
    def is_empty(self, pos: Position) -> bool:
        return self.pieces[pos.x][pos.y].is_empty()

    @check_position
    def is_piece_state(self, pos: Position, state: Player) -> bool:
        return self.pieces[pos.x][pos.y].is_piece_state(state)

    @check_position
    def get_state(self, pos: Position) -> Player:
        return self.pieces[pos.x][pos.y].get_state()

    @check_position
    def _flip(self, pos: Position) -> None:
        self.pieces[pos.x][pos.y].flip()

    def get_size(self) -> int:
        return self.size

    def update(self, command: BoardUpdateCommand) -> None:
        self._place_piece(command.place_position, command.player)
        for direction in command.flippable_directions:
            length = 1
            while True:
                target_position = command.place_position + (direction * length)
                if self.get_state(target_position) == command.player:
                    break
                self._flip(target_position)
                length += 1

    def get_player_more_pieces(self) -> Player:
        p1 = 0
        p2 = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.pieces[i][j].get_state() == Player.FIRST:
                    p1 += 1
                elif self.pieces[i][j].get_state() == Player.SECOND:
                    p2 += 1
                else:
                    continue

        if p2 < p1:
            return Player.FIRST
        elif p1 < p2:
            return Player.SECOND
        else:
            return Player.NONE
