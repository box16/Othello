import unittest
from ..game_state_service import GameStateService, Move
from ..board import Board
from .. import factory
from ..player import Player
from ..position import Position

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


class TestGameStateService(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board_service = factory.create_common_board_service(self.board)
        self.game_state_service = GameStateService(self.board_service)

    def test_first_possible_moves(self):
        move = Move(Player.FIRST, Position(3, 2))
        self.assertTrue(self.game_state_service.is_valid_move(move))


if __name__ == "__main__":
    unittest.main()
