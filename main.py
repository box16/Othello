from UI.gui_drawer import GUIDrawer
from Application.board_data import BoardData
from Domain.Board.board import Board
import tkinter as tk

root = tk.Tk()
board = Board()
board_data = BoardData(board)
gui = GUIDrawer(root, board_data)
root.mainloop()
