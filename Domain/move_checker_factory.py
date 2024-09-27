from .move_checker import Move, IRule, MoveChecker
from .position import Position
from .piece import PieceState

"""
1. 置こうとしている場所が空である事
2. 置こうとしている場所の周辺に相手の駒がある事
3. 2で相手の駒のある所から伸ばした方向に空のマスが無く自分の駒がある事
"""


class Empty(IRule):
    def is_valid(self, move: Move) -> bool:
        board = move.board
        position = move.position
        return board.is_empty(position)


class OpponentPieceAround(IRule):
    AROUND = [
        Position(-1, -1),
        Position(0, -1),
        Position(1, -1),
        Position(-1, 0),
        Position(1, 0),
        Position(-1, 1),
        Position(0, 1),
        Position(1, 1),
    ]

    def is_valid(self, move: Move) -> bool:
        board = move.board
        position = move.position
        opponent = move.piece_state.opponent()
        for around in self.AROUND:
            if board.is_piece_state(position + around, opponent):
                return True
        return False


class OpponentPiecesAreFlanked(IRule):
    AROUND = [
        Position(-1, -1),
        Position(0, -1),
        Position(1, -1),
        Position(-1, 0),
        Position(1, 0),
        Position(-1, 1),
        Position(0, 1),
        Position(1, 1),
    ]

    def is_valid(self, move: Move) -> bool:
        board = move.board
        position = move.position
        for around in self.AROUND:
            if board.is_empty(position + around):
                continue
            if board.is_piece_state(position + around, move.piece_state):
                continue
            return self._check_direction(around, move)

    def _check_direction(self, direction: Position, move: Move) -> bool:
        length = 1
        board = move.board
        position = move.position
        while True:
            check_pos = position + (direction * length)
            if board.is_empty(check_pos):
                return False
            if board.is_piece_state(check_pos, move.piece_state):
                return True
            length += 1


def create_common_checker():
    rules = [Empty(), OpponentPieceAround(), OpponentPiecesAreFlanked()]
    common_checker = MoveChecker(rules)
    return common_checker
