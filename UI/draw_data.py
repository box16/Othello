from Application.board_data import BoardData
from dataclasses import dataclass


@dataclass(frozen=True)
class DrawData:
    board_data: BoardData
    text: str
