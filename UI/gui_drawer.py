from .drawer import Drawer
import tkinter as tk
from Application.othello_service import OthelloService
from Application.move_data import MoveData
from Domain.Model.player import Player
from Domain.Model.position import Position


class GUIDrawer(Drawer):
    CELL_SIZE = 80
    TEXT_AREA_SIZE = 100

    def __init__(self, root: tk.Tk, othello_service: OthelloService) -> None:
        self.root = root
        self.othello_service = othello_service

        board_data = self.othello_service.get_board_data()
        geometry_width = board_data.size * self.CELL_SIZE
        geometry_height = geometry_width + self.TEXT_AREA_SIZE
        self.root.geometry(f"{geometry_width}x{geometry_height}")

        self.label = tk.Label(self.root, text="Initialize", font=("Arial", 40))
        self.label.pack()

        canvas_size = geometry_width
        self.canvas = tk.Canvas(
            self.root,
            width=canvas_size,
            height=canvas_size,
        )
        self.canvas.bind("<Button-1>", lambda event: self._update(event))
        self.canvas.pack()

        self.draw()
        self.root.mainloop()

    def _get_player_color(self, player: Player) -> str:
        if player == Player.FIRST:
            return "Black"
        elif player == Player.SECOND:
            return "White"
        else:
            return "Green"

    def _update(self, event: tk.Event) -> None:
        if not self.othello_service.can_continue_game():
            return

        player = self.othello_service.get_next_player()
        position = self._convert_board_position(event)
        self.othello_service.update_game(MoveData(player, position))

        if not self.othello_service.can_continue_game():
            self.draw()
            self.label.config(text=f"Game is end.")
        else:
            self.draw()

    def draw(self) -> None:
        next_player = self.othello_service.get_next_player()
        board_data = self.othello_service.get_board_data()
        self.label.config(text=f"Next: {self._get_player_color(next_player)}")

        for i in range(board_data.size):
            for j in range(board_data.size):
                x1 = i * self.CELL_SIZE
                y1 = j * self.CELL_SIZE
                x2 = x1 + self.CELL_SIZE
                y2 = y1 + self.CELL_SIZE

                self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")

                player = board_data.pieces[i][j]
                if player.is_none():
                    continue
                self._draw_piece(x1, y1, self._get_player_color(player))

    def _draw_piece(self, x, y, color):
        padding = 10
        self.canvas.create_oval(
            x + padding,
            y + padding,
            x + self.CELL_SIZE - padding,
            y + self.CELL_SIZE - padding,
            fill=color,
        )

    def _convert_board_position(self, event: tk.Event) -> Position:
        return Position(int(event.x / self.CELL_SIZE), int(event.y / self.CELL_SIZE))
