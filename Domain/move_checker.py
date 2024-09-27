from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass
from .position import Position
from .piece import PieceState


@dataclass(frozen=True)
class Move:
    position: Position
    piece_state: PieceState


class IRule(ABC):
    @abstractmethod
    def is_valid(self, move: Move) -> bool:
        pass


class MoveChecker:
    def __init__(self, rules: List[IRule]) -> None:
        self.rules = rules

    def is_valid(self, move: Move) -> bool:
        for rule in self.rules:
            if not rule.is_valid(move):
                return False
        return True
