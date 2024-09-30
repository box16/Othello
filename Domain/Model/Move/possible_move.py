from typing import List, Tuple
from dataclasses import dataclass
from Domain.Model.position import Position
from Domain.Model.player import Player
from Domain.Model.direction import Direction
from Domain.Model.Move.move import Move


@dataclass(frozen=True)
class PossibleMove:
    pos_can_place: Position
    flippable_directions: List[Direction]

    def __post_init__(self):
        object.__setattr__(
            self, "flippable_directions", tuple(self.flippable_directions)
        )

    def __eq__(self, other: "PossibleMove"):
        if not isinstance(other, PossibleMove):
            return False

        is_same_pos = self.pos_can_place == other.pos_can_place
        is_sasme_directions = set(self.flippable_directions) == set(
            other.flippable_directions
        )
        return is_same_pos and is_sasme_directions


@dataclass(frozen=True)
class PossibleMoves:
    player: Player
    moves: List[PossibleMove]

    def __post_init__(self):
        object.__setattr__(self, "moves", tuple(self.moves))

    def __bool__(self):
        return (len(self.moves) != 0) and (self.player != Player.NONE)

    def __iter__(self):
        return iter(self.moves)

    def __eq__(self, other: "PossibleMoves"):
        if not isinstance(other, PossibleMoves):
            return False
        return (set(self.moves) == set(other.moves)) and (self.player == other.player)

    def __contains__(self, move: Move):
        if move.player != self.player:
            return False

        for m in self.moves:
            if move.position == m.pos_can_place:
                return True
        return False

    def get_flippable_directions(self, move: Move) -> Tuple[Direction]:
        if move.player != self.player:
            return ()

        for m in self.moves:
            if move.position == m.pos_can_place:
                return m.flippable_directions
        return ()
