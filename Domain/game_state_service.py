from .Utility.player import Player
from .board_service import BoardService
from enum import Enum
from dataclasses import dataclass
from .Utility.position import Position
from .Utility.direction import Direction
from typing import Tuple


class GameState(Enum):
    IN_PROGRESS = 0
    END = 1


@dataclass(frozen=True)
class Move:
    player: Player
    position: Position

    def is_same_player(self, player: "Player") -> bool:
        return self.player == player


class InitializationFailed(Exception):
    pass


# possible_movesの管理は別クラスが良いかも
class GameStateService:
    def __init__(self, board_service: BoardService) -> None:
        self.game_state = GameState.IN_PROGRESS
        self.board_service = board_service

        if self._update(Player.FIRST):
            return
        if self._update(Player.SECOND):
            return
        raise InitializationFailed("ゲームの初期化に失敗しました")

    def update(self) -> None:
        now_player = self.next_player
        if self._update(now_player.opponent()):
            return
        if self._update(now_player):
            return

        self.next_player = Player.NONE
        self.game_state = GameState.END
        self.possible_moves = None

    def _update(self, player: Player) -> bool:
        possible_moves = self.board_service.get_possible_moves(player)
        if not possible_moves:
            return False

        self.next_player = player
        self.game_state = GameState.IN_PROGRESS
        self.possible_moves = possible_moves
        return True

    def can_continue(self) -> bool:
        return self.game_state == GameState.IN_PROGRESS

    def get_next_player(self) -> Player:
        return self.next_player

    def get_flippable_directions(self, move: Move) -> Tuple[Direction]:
        if not move.is_same_player(self.next_player):
            return ()
        if not (move.position in self.possible_moves):
            return ()
        return self.possible_moves.get_flippable_directions(move.position)
