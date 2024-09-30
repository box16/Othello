from typing import List
from Domain.Model.Move.i_move_rule import IMoveRule
from Domain.Model.Move.possible_move import PossibleMove, PossibleMoves
from Domain.Model.position import Position
from Domain.Model.direction import Direction
from Domain.Model.Board.board import InvalidPositionError
from Domain.Model.Board.board import Board
from Domain.Model.player import Player


class StandardRule(IMoveRule):
    """
    1. 置こうとしている場所が空である事
    2. 置こうとしている場所の周辺に相手の駒がある事
    3. 2で相手の駒のある所から伸ばした方向に空のマスが無く自分の駒がある事
    """

    AROUND = [
        Direction(-1, -1),
        Direction(0, -1),
        Direction(1, -1),
        Direction(-1, 0),
        Direction(1, 0),
        Direction(-1, 1),
        Direction(0, 1),
        Direction(1, 1),
    ]

    def get_possible_moves(self, board: Board, player: Player) -> PossibleMoves:
        result: List[PossibleMove] = []
        size = board.get_size()
        all_pos = [Position(i, j) for i in range(size) for j in range(size)]

        for pos in all_pos:
            if not board.is_empty(pos):
                continue

            opponent_directions = self._check_around(board, player, pos)
            if not opponent_directions:
                continue

            flippable_directions = self._check_direction(
                board, player, pos, opponent_directions
            )
            if not flippable_directions:
                continue

            result.append(PossibleMove(pos, flippable_directions))

        return PossibleMoves(player, result)

    def _check_around(
        self, board: Board, player: Player, pos: Position
    ) -> List[Direction]:
        result: List[Direction] = []
        for around in self.AROUND:
            try:
                if board.is_piece_state(pos + around, player.opponent()):
                    result.append(around)
            except InvalidPositionError:
                continue
        return result

    def _check_direction(
        self, board: Board, player: Player, pos: Position, directions: List[Direction]
    ):
        result: List[Direction] = []
        for direction in directions:
            length = 1
            while True:
                try:
                    check_pos = pos + (direction * length)
                    if board.is_empty(check_pos):
                        break
                    if board.is_piece_state(check_pos, player):
                        result.append(direction)
                    length += 1
                except InvalidPositionError:
                    break
        return result
