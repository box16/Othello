import unittest
from . import factory
from .Board.board import Board
from .MoveCheck.move_checker import PossibleMove, PossibleMoves
from .Utility.position import Position
from .Utility.player import Player
from .Utility.direction import Direction

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
        self.board_service = factory.create_common_board_service(self.board)

    def test_first_possible_moves(self):
        e = [
            PossibleMove(Position(5, 4), [Direction(-1, 0)]),
            PossibleMove(Position(3, 2), [Direction(0, 1)]),
            PossibleMove(Position(4, 5), [Direction(0, -1)]),
            PossibleMove(Position(2, 3), [Direction(1, 0)]),
        ]
        expect = PossibleMoves(Player.FIRST, e)
        result = self.board_service.get_possible_moves(Player.FIRST)
        self.assertEqual(result, expect)


if __name__ == "__main__":
    unittest.main()
