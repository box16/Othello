import tkinter as tk
from Domain.Service.move_service import MoveService
from Domain.Model.Turn.turn import Turn
from Domain.Model.Move.standard_rule import StandardRule
from Domain.Model.Board.board import Board
from Application.othello_service import OthelloService
from UI.CUI.cui_drawer import CUIDrawer
from UI.CUI.cui_interface import CUIInterface


def create_othello_service() -> OthelloService:
    board = Board()
    move_service = MoveService(board, StandardRule())
    turn = Turn(move_service)
    OthelloService(board, move_service, turn)
    return OthelloService(board, move_service, turn)


othello_service = create_othello_service()
board_data = othello_service.get_board_data()
drawer = CUIDrawer()
user_interface = CUIInterface(othello_service, drawer)

user_interface.start_game()
