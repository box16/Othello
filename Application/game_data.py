from dataclasses import dataclass
from Domain.Model.player import Player
from Application.board_data import BoardData


@dataclass(frozen=True)
class GameData:
    next_player: Player
    board_data: BoardData
