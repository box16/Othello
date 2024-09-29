from abc import ABC, abstractmethod
from typing import List, Tuple, Union
from dataclasses import dataclass
from ..Utility.position import Position
from ..Utility.player import Player
from ..Board.board import Board
from ..Utility.direction import Direction


@dataclass(frozen=True)
class Move:
    player: Player
    position: Position


@dataclass(frozen=True)
class PossibleMove:
    pos_can_place: Position
    flippable_directions: Tuple[Direction]

    def __post_init__(self):
        object.__setattr__(
            self, "flippable_directions", tuple(self.flippable_directions)
        )

    def __eq__(self, other: "PossibleMove"):
        if not isinstance(other, PossibleMove):
            return False
        return (self.pos_can_place == other.pos_can_place) and set(
            self.flippable_directions
        ) == set(other.flippable_directions)


@dataclass(frozen=True)
class PossibleMoves:
    player: Player
    moves: Union[Tuple[PossibleMove], List[PossibleMove]]

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

    def get_flippable_directions(self, pos: Position) -> Tuple[Direction]:
        for m in self.moves:
            if pos == m.pos_can_place:
                return m.flippable_directions
        return ()


@dataclass(frozen=True)
class BoardState:
    board: Board
    player: Player


class IRule(ABC):
    @abstractmethod
    def get_possible_moves(
        self, board_state: BoardState, possible_moves: PossibleMoves
    ) -> PossibleMoves:
        pass


class MoveChecker:
    def __init__(self, rules: List[IRule]) -> None:
        self.rules = rules

    def get_possible_moves(self, board_state: BoardState) -> PossibleMoves:
        possible_moves: PossibleMoves = PossibleMoves(Player.NONE, [])
        for rule in self.rules:
            possible_moves = rule.get_possible_moves(board_state, possible_moves)
            if not possible_moves:
                return PossibleMoves(Player.NONE, [])
        return possible_moves
