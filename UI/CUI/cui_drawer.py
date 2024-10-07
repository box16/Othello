from UI.drawer import Drawer
from UI.draw_data import DrawData
from UI.CUI.player_mark import PLAYER_MARK


class CUIDrawer(Drawer):

    def draw(self, draw_data: DrawData) -> None:
        print()
        print(draw_data.text)

        column_header = " "
        for i in range(draw_data.board_data.size):
            column_header += f" {i}"
        print(column_header)

        for i in range(draw_data.board_data.size):
            row = f"{i}"
            for j in range(draw_data.board_data.size):
                player = draw_data.board_data.pieces[j][i]
                row += f" {PLAYER_MARK[player]}"
            print(row)
