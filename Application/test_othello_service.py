import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import unittest
from Application.othello_service import OthelloService, InvalidMoveError
from Application.game_data import GameData
from Application.move_data import MoveData
from Domain.Model.Turn.turn import Turn
from Domain.Model.player import Player
from Domain.Model.position import Position
from Domain.Model.Board.board import Board
from Application.board_data import BoardData
from Domain.Model.Move.standard_rule import StandardRule
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


class OthelloServiceTest(unittest.TestCase):
    def setUp(self):
        board = Board()
        move_service = MoveService(board, StandardRule())
        turn = Turn(move_service)
        self.othello_service = OthelloService(board, move_service, turn)

    def test_invalid_move_update(self):
        with self.assertRaises(InvalidMoveError):
            self.othello_service.update_game(MoveData(Player.FIRST, Position(0, 0)))

    def test_valid_move_update(self):
        self.othello_service.update_game(MoveData(Player.FIRST, Position(3, 2)))

        dummy_board = Board()
        dummy_board._place_piece(Position(3, 2), Player.FIRST)
        dummy_board._flip(Position(3, 3))
        expect = GameData(Player.SECOND, BoardData(dummy_board))
        actually = self.othello_service.get_game_data()
        self.assertEqual(str(expect), str(actually))


if __name__ == "__main__":
    unittest.main()
