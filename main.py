from UI.gui_drawer import GUIDrawer
from Domain.Model.Board.board import Board
import tkinter as tk
from Application.othello_service import OthelloService
from Application.game_data import GameData
from Application.move_data import MoveData
from Application.board_data import BoardData
from Domain.Service.move_service import MoveService
from Domain.Model.Turn.turn import Turn
from Domain.Model.Move.standard_rule import StandardRule


def click_event(event):
    position = gui.convert_board_position(event)
    othello_service.update_game(MoveData(turn.get_next_player(), position))
    game_state: GameData = othello_service.get_game_data()
    gui.draw(game_state.board_data)


board = Board()
move_service = MoveService(board, StandardRule())
turn = Turn(move_service)
othello_service = OthelloService(board, move_service, turn)

root = tk.Tk()
gui = GUIDrawer(root, BoardData(board), click_event)

root.mainloop()
