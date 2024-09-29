from Domain.board_service import BoardService, BoardUpdateCommand
from Domain.game_state_service import GameStateService
from dataclasses import dataclass
from Domain.Utility.player import Player
from Domain.Utility.position import Position
from Domain.game_state_service import Move


@dataclass(frozen=True)
class NextInfo:
    next_player: Player
    can_continue: bool

    def __eq__(self, other: "NextInfo") -> bool:
        if not isinstance(other, NextInfo):
            return False
        return (self.next_player == other.next_player) and (
            self.can_continue == other.can_continue
        )


@dataclass(frozen=True)
class MoveData:
    player: Player
    position: Position


class InvalidMoveError(Exception):
    pass


class OthelloService:
    def __init__(
        self, board_service: BoardService, game_state_service: GameStateService
    ) -> None:
        self.board_service = board_service
        self.game_state_service = game_state_service

    def prepare(self) -> NextInfo:
        return NextInfo(
            self.game_state_service.get_next_player(),
            self.game_state_service.can_continue(),
        )

    def process(self, move: MoveData) -> None:
        flippable_directions = self.game_state_service.get_flippable_directions(
            Move(move.player, move.position)
        )
        if not flippable_directions:
            raise InvalidMoveError("有効な手ではありません")

        update_command = BoardUpdateCommand(
            move.player, move.position, flippable_directions
        )
        self.board_service.update(update_command)
        self.game_state_service.update()
