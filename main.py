from UI.gui_drawer import GUIDrawer
from Domain.Model.Board.board import Board
import tkinter as tk
from Application.othello_service import OthelloService
from Application.move_data import MoveData
from Domain.Service.move_service import MoveService
from Domain.Model.Turn.turn import Turn
from Domain.Model.Move.standard_rule import StandardRule


def create_othello_service() -> OthelloService:
    board = Board()
    move_service = MoveService(board, StandardRule())
    turn = Turn(move_service)
    OthelloService(board, move_service, turn)
    return OthelloService(board, move_service, turn)


othello_service = create_othello_service()
user_interface = GUIDrawer(tk.Tk(), othello_service)
