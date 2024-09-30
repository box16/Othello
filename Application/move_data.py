from dataclasses import dataclass
from Domain.Model.player import Player
from Domain.Model.position import Position


@dataclass(frozen=True)
class MoveData:
    player: Player
    position: Position
