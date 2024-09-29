from .drawer import Drawer
import tkinter as tk
from Application.board_data import BoardData
from Domain.Utility.player import Player


class GUIDrawer(Drawer):
    def __init__(self, root, board_data: BoardData) -> None:
        self.root = root
        self.cell_size = 80  # 各セルのサイズ
        self.board_size = board_data.size
        self.canvas = tk.Canvas(
            self.root,
            width=self.cell_size * self.board_size,
            height=self.cell_size * self.board_size,
        )
        self.canvas.pack()
        self.draw(board_data)

    def draw(self, board_data: BoardData) -> None:
        for i in range(self.board_size):
            for j in range(self.board_size):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")

                player = board_data.pieces[i][j]
                if player == Player.FIRST:
                    self.draw_piece(x1, y1, "black")
                elif player == Player.SECOND:
                    self.draw_piece(x1, y1, "white")

    def draw_piece(self, x, y, color):
        padding = 10
        self.canvas.create_oval(
            x + padding,
            y + padding,
            x + self.cell_size - padding,
            y + self.cell_size - padding,
            fill=color,
        )
