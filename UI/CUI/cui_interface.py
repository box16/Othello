from Domain.Model.position import Position
from Domain.Model.player import Player
from Application.othello_service import OthelloService
from Application.move_data import MoveData
from Application.othello_service import InvalidMoveError
from UI.CUI.cui_drawer import CUIDrawer
from UI.draw_data import DrawData
from UI.CUI.player_mark import PLAYER_MARK
from UI.interface import Interface


class CUIInterface(Interface):
    def __init__(self, othello_service: OthelloService, drawer: CUIDrawer) -> None:
        self.othello_service = othello_service
        self.drawer = drawer

    def start_game(self) -> None:
        board_data = self.othello_service.get_board_data()
        next_player = self.othello_service.get_next_player()
        text = f"Next: {PLAYER_MARK[next_player]}"

        self.drawer.draw(DrawData(board_data, text))
        self._input_ready()

    def _input_ready(self) -> None:
        try:
            user_input = input("Enter two integers separated by a space: ")
            x, y = user_input.split()
            self.update_game(Position(int(x), int(y)))
        except InvalidMoveError as e:
            print(e)
            self._input_ready()

    def update_game(self, position: Position) -> None:
        if not self.othello_service.can_continue_game():
            return

        player = self.othello_service.get_next_player()
        self.othello_service.update_game(MoveData(player, position))

        if not self.othello_service.can_continue_game():
            self.end_game()
            return

        board_data = self.othello_service.get_board_data()
        next_player = self.othello_service.get_next_player()
        text = f"Next: {PLAYER_MARK[next_player]}"
        self.drawer.draw(DrawData(board_data, text))

        self._input_ready()

    def end_game(self) -> None:
        board_data = self.othello_service.get_board_data()
        winner = self.othello_service.get_player_more_pieces()
        if winner == Player.NONE:
            text = f"Draw"
        else:
            text = f"Winner: {PLAYER_MARK[winner]}"
        self.drawer.draw(DrawData(board_data, text))
