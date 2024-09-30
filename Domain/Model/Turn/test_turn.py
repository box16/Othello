import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)


import unittest
from Domain.Model.Turn.turn import Turn
from Domain.Model.Board.board import Board
from Domain.Model.player import Player
from Domain.Model.Move.move_rule import StandardRule
from Domain.Service.move_service import MoveService

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
        self.move_service = MoveService(self.board, StandardRule())
        self.turn = Turn(self.move_service)

    def test_first_turn(self):
        self.assertEqual(self.turn.get_next_player(), Player.FIRST)

    def test_second_turn(self):
        self.turn.update()
        self.assertEqual(self.turn.get_next_player(), Player.SECOND)


if __name__ == "__main__":
    unittest.main()
