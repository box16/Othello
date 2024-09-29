from .move_checker import PossibleMove, PossibleMoves, IRule, BoardState
from ..Utility.position import Position
from ..Utility.direction import Direction
from ..Board.board import InvalidPositionError
from typing import List

"""
1. 置こうとしている場所が空である事
2. 置こうとしている場所の周辺に相手の駒がある事
3. 2で相手の駒のある所から伸ばした方向に空のマスが無く自分の駒がある事
"""


class Empty(IRule):
    def get_possible_moves(
        self, board_state: BoardState, possible_moves: PossibleMoves
    ) -> PossibleMoves:
        result: List[PossibleMove] = []
        size = board_state.board.get_size()
        all_pos = [Position(i, j) for i in range(size) for j in range(size)]
        for pos in all_pos:
            if board_state.board.is_empty(pos):
                result.append(PossibleMove(pos, ()))
        return PossibleMoves(board_state.player, result)


class OpponentPieceAround(IRule):
    DIRECTIONS = [
        Direction(-1, -1),
        Direction(0, -1),
        Direction(1, -1),
        Direction(-1, 0),
        Direction(1, 0),
        Direction(-1, 1),
        Direction(0, 1),
        Direction(1, 1),
    ]

    def get_possible_moves(
        self, board_state: BoardState, possible_moves: PossibleMoves
    ) -> PossibleMoves:
        result: List[PossibleMove] = []
        for move in possible_moves:
            valid_directions = self._check_direction(board_state, move)
            if not valid_directions:
                continue
            result.append(PossibleMove(move.pos_can_place, valid_directions))
        return PossibleMoves(board_state.player, result)

    def _check_direction(self, board_state: BoardState, move: PossibleMove):
        valid_directions = []
        for direction in self.DIRECTIONS:
            try:
                if board_state.board.is_piece_state(
                    move.pos_can_place + direction, board_state.player.opponent()
                ):
                    valid_directions.append(direction)
            except InvalidPositionError:
                continue
        return valid_directions


class OpponentPiecesAreFlanked(IRule):
    def get_possible_moves(
        self, board_state: BoardState, possible_moves: PossibleMoves
    ) -> PossibleMoves:

        result: List[PossibleMove] = []
        for move in possible_moves:
            valid_directions = []
            for direction in move.flippable_directions:
                if self._check_direction(board_state, move.pos_can_place, direction):
                    valid_directions.append(direction)
            if not valid_directions:
                continue
            result.append(PossibleMove(move.pos_can_place, valid_directions))
        return PossibleMoves(board_state.player, result)

    def _check_direction(
        self, board_state: BoardState, base_pos: Position, direction: Direction
    ):
        scalar = 1
        while True:
            try:
                check_pos = base_pos + (direction * scalar)
                if board_state.board.is_empty(check_pos):
                    return False
                if board_state.board.is_piece_state(check_pos, board_state.player):
                    return True
                scalar += 1
            except InvalidPositionError:
                return False
