from dataclasses import dataclass
from typing import List
from Domain.Model.player import Player
from Domain.Model.position import Position
from Domain.Model.direction import Direction


@dataclass(frozen=True)
class BoardUpdateCommand:
    player: Player
    place_position: Position
    flippable_directions: List[Direction]
