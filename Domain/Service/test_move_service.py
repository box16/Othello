import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import unittest
from Domain.Service.move_service_factory import create_common_move_service
from Domain.Model.Board.board import Board
from Domain.Model.Move.possible_move import PossibleMove, PossibleMoves
from Domain.Model.position import Position
from Domain.Model.player import Player
from Domain.Model.direction import Direction

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


class TestMoveService(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.move_service = create_common_move_service(self.board)

    def test_first_possible_moves(self):
        self.move_service.update_possible_move(Player.FIRST)
        e = (
            PossibleMove(Position(3, 2), [Direction(0, 1)]),
            PossibleMove(Position(2, 3), [Direction(1, 0)]),
            PossibleMove(Position(5, 4), [Direction(-1, 0)]),
            PossibleMove(Position(4, 5), [Direction(0, -1)]),
        )
        expect = PossibleMoves(Player.FIRST, e)
        actually = self.move_service.possible_moves
        self.assertEqual(expect, actually)
        self.assertTrue(self.move_service.has_possible_move(Player.FIRST))


if __name__ == "__main__":
    unittest.main()
