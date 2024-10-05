from tkinter import Event
from Domain.Model.player import Player
from Application.othello_service import OthelloService
from Application.move_data import MoveData
from UI.draw_data import DrawData
from UI.GUI.gui_drawer import GUIDrawer
from UI.GUI.player_color import PLAYER_COLOR


class UserInterface:

    def __init__(self, othello_service: OthelloService, drawer: GUIDrawer) -> None:
        self.othello_service = othello_service
        self.drawer = drawer
        self.drawer.bind(self.update_game)

    def start_game(self) -> None:
        board_data = self.othello_service.get_board_data()
        next_player = self.othello_service.get_next_player()
        text = f"Next: {PLAYER_COLOR[next_player]}"

        self.drawer.draw(DrawData(board_data, text))
        self.drawer.start_loop()

    def update_game(self, event: Event) -> None:
        if not self.othello_service.can_continue_game():
            return

        player = self.othello_service.get_next_player()
        position = self.drawer.convert_board_pos(event)
        self.othello_service.update_game(MoveData(player, position))

        if not self.othello_service.can_continue_game():
            self.end_game()
            return

        board_data = self.othello_service.get_board_data()
        next_player = self.othello_service.get_next_player()
        text = f"Next: {PLAYER_COLOR[next_player]}"
        self.drawer.draw(DrawData(board_data, text))

    def end_game(self) -> None:
        board_data = self.othello_service.get_board_data()
        winner = self.othello_service.get_player_more_pieces()
        if winner == Player.NONE:
            text = f"Draw"
        else:
            text = f"Winner: {PLAYER_COLOR[winner]}"
        self.drawer.draw(DrawData(board_data, text))
