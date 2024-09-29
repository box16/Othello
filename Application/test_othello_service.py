import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import unittest
from .othello_service import OthelloService
from Domain import factory
from Domain.game_state_service import GameStateService
from .othello_service import NextInfo
from Domain.Utility.player import Player
from Domain.Board.board import Board
from Domain.game_state_service import Move
from Domain.Utility.position import Position
from .othello_service import InvalidMoveError

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


class OthelloServiceTest(unittest.TestCase):
    def setUp(self):
        board = Board()
        board_service = factory.create_common_board_service(board)
        game_state_service = GameStateService(board_service)
        self.othello_service = OthelloService(board_service, game_state_service)

    def test_initial_state(self):
        expect = NextInfo(Player.FIRST, True)
        actually = self.othello_service.prepare()
        self.assertEqual(expect, actually)

    def test_valid_move(self):
        move = Move(Player.FIRST, Position(3, 2))
        self.othello_service.process(move)

        expect = NextInfo(Player.SECOND, True)
        actually = self.othello_service.prepare()

        self.assertEqual(expect, actually)

    def test_invalid_move(self):
        move = Move(Player.FIRST, Position(0, 0))
        with self.assertRaises(InvalidMoveError):
            self.othello_service.process(move)


if __name__ == "__main__":
    unittest.main()
