import tkinter as tk
from typing import Callable
from Domain.Model.position import Position
from Application.board_data import BoardData
from UI.drawer import Drawer
from UI.draw_data import DrawData
from UI.GUI.player_color import PLAYER_COLOR


class GUIDrawer(Drawer):
    def __init__(
        self,
        root: tk.Tk,
        board_data: BoardData,
        cell_size: int = 80,
        text_area_size: int = 100,
    ) -> None:
        self.root = root
        self.CELL_SIZE = cell_size
        self.TEXT_AREA_SIZE = text_area_size

        self._set_geometry(board_data)
        self.label = tk.Label(self.root, text="Initialize", font=("Arial", 40))
        self._create_canvas(board_data)

        self.label.grid(row=0, column=0, sticky="nsew")
        self.canvas.grid(row=1, column=0, sticky="nsew")

    def _set_geometry(self, board_data: BoardData):
        geometry_width = board_data.size * self.CELL_SIZE
        geometry_height = geometry_width + self.TEXT_AREA_SIZE
        self.root.geometry(f"{geometry_width}x{geometry_height}")

    def _create_canvas(self, board_data: BoardData):
        canvas_size = board_data.size * self.CELL_SIZE
        self.canvas = tk.Canvas(
            self.root,
            width=canvas_size,
            height=canvas_size,
        )

    def start_loop(self) -> None:
        self.root.mainloop()

    def draw(self, draw_data: DrawData) -> None:
        self.canvas.delete("all")

        self.label.config(text=draw_data.text)
        for i in range(draw_data.board_data.size):
            for j in range(draw_data.board_data.size):
                x1 = i * self.CELL_SIZE
                y1 = j * self.CELL_SIZE
                x2 = x1 + self.CELL_SIZE
                y2 = y1 + self.CELL_SIZE

                self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")

                player = draw_data.board_data.pieces[i][j]
                if player.is_none():
                    continue
                self._draw_piece(x1, y1, PLAYER_COLOR[player])

    def _draw_piece(self, x, y, color):
        padding = 10
        self.canvas.create_oval(
            x + padding,
            y + padding,
            x + self.CELL_SIZE - padding,
            y + self.CELL_SIZE - padding,
            fill=color,
        )

    def bind(self, func: Callable):
        self.canvas.bind("<Button-1>", func)

    def convert_board_pos(self, event: tk.Event) -> Position:
        return Position(int(event.x / self.CELL_SIZE), int(event.y / self.CELL_SIZE))
