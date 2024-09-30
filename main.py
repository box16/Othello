from UI.gui_drawer import GUIDrawer
from Domain.Model.Board.board import Board
import tkinter as tk
from Application.othello_service import OthelloService, GameState, MoveData
from Application.board_data import BoardData
from Domain.Service.move_service import MoveService
from Domain.Model.Turn.turn import Turn
from Domain.Service.move_service_factory import create_common_move_service


def click_event(event):
    position = gui.convert_board_position(event)
    othello_service.update_game(MoveData(turn.get_next_player(), position))
    game_state: GameState = othello_service.get_game_state()
    gui.draw(game_state.board_data)


board = Board()
move_service: MoveService = create_common_move_service(board)
turn = Turn(move_service)
othello_service = OthelloService(board, move_service, turn)

root = tk.Tk()
gui = GUIDrawer(root, BoardData(board), click_event)

root.mainloop()
