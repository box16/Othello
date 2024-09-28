import unittest
from .. import move_checker_factory
from ..board import Board
from ..board_service import BoardService
from ..move_checker import Move, PossibleMoves
from ..position import Position
from ..piece import Player
from ..direction import Direction

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

    def test_first_possible_moves(self):
        e1 = Move(Position(5, 4), [Direction(-1, 0)])
        e2 = Move(Position(3, 2), [Direction(0, 1)])
        e3 = Move(Position(4, 5), [Direction(0, -1)])
        e4 = Move(Position(2, 3), [Direction(1, 0)])
        expect = PossibleMoves([e1, e2, e3, e4])
        result = self.board_service.get_possible_moves(Player.FIRST)
        self.assertEqual(result, expect)


if __name__ == "__main__":
    unittest.main()
