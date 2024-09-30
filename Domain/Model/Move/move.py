from dataclasses import dataclass
from Domain.Model.position import Position
from Domain.Model.player import Player


@dataclass(frozen=True)
class Move:
    player: Player
    position: Position
