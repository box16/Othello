import unittest
from .. import move_checker_factory
from ..board import Board
from ..board_service import BoardService
from ..move_checker import Move
from ..position import Position
from ..piece import PieceState

"""
初期配置
   0 1 2 3 4 5 6 7
0  . . . . . . . .
1  . . . . . . . .
2  . . . . . . . .
3  . . . ○ ● . . .
4  . . . ● ○ . . .
5  . . . . . . . .
6  . . . . . . . .
7  . . . . . . . .
"""


class TestBoardService(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.move_checker = move_checker_factory.create_common_checker()
        self.board_service = BoardService(self.board, self.move_checker)

    def test_first_valid_move(self):
        first_move = Move(Position(5, 4), PieceState.PLAYER1, self.board)
        result = self.board_service.is_valid_move(first_move)
        self.assertTrue(result)

    def test_first_invalid_move(self):
        first_move = Move(Position(5, 3), PieceState.PLAYER1, self.board)
        result = self.board_service.is_valid_move(first_move)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
