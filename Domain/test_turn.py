import unittest
from .turn import Turn
from .Board.board import Board
from . import factory
from .Utility.player import Player

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


class TestTurn(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.move_service = factory.create_common_move_service(self.board)
        self.turn = Turn(self.move_service)

    def test_first_turn(self):
        self.assertEqual(self.turn.get_next_player(), Player.FIRST)

    def test_second_turn(self):
        self.turn.update()
        self.assertEqual(self.turn.get_next_player(), Player.SECOND)


if __name__ == "__main__":
    unittest.main()
