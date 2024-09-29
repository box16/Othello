import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from othello_service import OthelloService, InvalidMoveError, MoveData
from Domain import factory
from Domain.turn import Turn
from Domain.Utility.player import Player
from Domain.Utility.position import Position
from Domain.Board.board import Board

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
        board_service = factory.create_common_move_service(board)
        turn = Turn(board_service)
        self.othello_service = OthelloService(board_service, turn)


if __name__ == "__main__":
    unittest.main()
