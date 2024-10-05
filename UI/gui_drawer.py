from .drawer import Drawer
import tkinter as tk
from Application.othello_service import OthelloService
from Application.move_data import MoveData
from Domain.Model.player import Player
from Domain.Model.position import Position


class GUIDrawer(Drawer):
    PLAYER_COLOR = {
        Player.FIRST: "Black",
        Player.SECOND: "White",
        Player.NONE: "Green",
    }

    def __init__(
        self,
        root: tk.Tk,
        othello_service: OthelloService,
        cell_size: int = 80,
        text_area_size: int = 100,
    ) -> None:
        self.root = root
        self.othello_service = othello_service
        self.CELL_SIZE = cell_size
        self.TEXT_AREA_SIZE = text_area_size

        board_data = self.othello_service.get_board_data()
        geometry_width = board_data.size * self.CELL_SIZE
        geometry_height = geometry_width + self.TEXT_AREA_SIZE
        self.root.geometry(f"{geometry_width}x{geometry_height}")

        self.label = tk.Label(self.root, text="Initialize", font=("Arial", 40))

        canvas_size = geometry_width
        self.canvas = tk.Canvas(
            self.root,
            width=canvas_size,
            height=canvas_size,
        )
        self.canvas.bind("<Button-1>", self._update)

        self.label.grid(row=0, column=0, sticky="nsew")
        self.canvas.grid(row=1, column=0, sticky="nsew")

        self.draw()
        self.root.mainloop()

    def _update(self, event: tk.Event) -> None:
        if not self._is_game_continuable():
            return

        self._perform_move(event)

        if not self._is_game_continuable():
            self._end_game()
        else:
            self.draw()

    def _is_game_continuable(self) -> bool:
        return self.othello_service.can_continue_game()

    def _perform_move(self, event: tk.Event) -> None:
        player = self.othello_service.get_next_player()
        position = self._convert_board_position(event)
        self.othello_service.update_game(MoveData(player, position))

    def _end_game(self) -> None:
        self.draw()
        winner = self.othello_service.get_player_more_pieces()
        if winner == Player.NONE:
            self.label.config(text=f"Draw")
        else:
            self.label.config(text=f"Winner : {self.PLAYER_COLOR[winner]}")

    def draw(self) -> None:
        self.canvas.delete("all")

        next_player = self.othello_service.get_next_player()
        board_data = self.othello_service.get_board_data()
        self.label.config(text=f"Next: {self.PLAYER_COLOR[next_player]}")

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
                self._draw_piece(x1, y1, self.PLAYER_COLOR[player])

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
