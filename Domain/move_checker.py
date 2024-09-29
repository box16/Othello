from abc import ABC, abstractmethod
from typing import List, Tuple
from dataclasses import dataclass
from .position import Position
from .player import Player
from .board import Board
from .direction import Direction


@dataclass(frozen=True)
class Move:
    pos_can_place: Position
    flippable_directions: Tuple[Direction]

    def __post_init__(self):
        object.__setattr__(
            self, "flippable_directions", tuple(self.flippable_directions)
        )

    def __eq__(self, other: "Move"):
        if not isinstance(other, Move):
            return False
        return (self.pos_can_place == other.pos_can_place) and set(
            self.flippable_directions
        ) == set(other.flippable_directions)


@dataclass(frozen=True)
class PossibleMoves:
    player: Player
    moves: Tuple[Move]

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

    def __contains__(self, position: Position):
        for m in self.moves:
            if position == m.pos_can_place:
                return True
        return False


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
