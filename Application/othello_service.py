from Domain.move_service import MoveService
from Domain.turn import Turn
from dataclasses import dataclass
from Domain.Utility.player import Player
from Domain.Utility.position import Position


@dataclass(frozen=True)
class MoveData:
    player: Player
    position: Position


class InvalidMoveError(Exception):
    pass


class OthelloService:
    def __init__(self, move_service: MoveService, turn: Turn) -> None:
        self.move_service = move_service
        self.turn = turn

    def process(self, move: MoveData) -> None:
        self.turn
