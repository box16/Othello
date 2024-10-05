import tkinter as tk
from Domain.Service.move_service import MoveService
from Domain.Model.Turn.turn import Turn
from Domain.Model.Move.standard_rule import StandardRule
from Domain.Model.Board.board import Board
from Application.othello_service import OthelloService
from UI.GUI.user_interface import UserInterface
from UI.GUI.gui_drawer import GUIDrawer


def create_othello_service() -> OthelloService:
    board = Board()
    move_service = MoveService(board, StandardRule())
    turn = Turn(move_service)
    OthelloService(board, move_service, turn)
    return OthelloService(board, move_service, turn)


othello_service = create_othello_service()
board_data = othello_service.get_board_data()
drawer = GUIDrawer(tk.Tk(), board_data)
user_interface = UserInterface(othello_service, drawer)

user_interface.start_game()
