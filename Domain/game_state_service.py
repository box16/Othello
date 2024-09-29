from .Utility.player import Player
from .board_service import BoardService
from enum import Enum
from dataclasses import dataclass
from .Utility.position import Position


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
        if self._update(self.player.opponent()):
            return
        if self._update(self.player):
            return

        self.player = Player.NONE
        self.game_state = GameState.END
        self.possible_moves = None

    def _update(self, player: Player) -> bool:
        possible_moves = self.board_service.get_possible_moves(player)
        if not possible_moves:
            return False

        self.player = player
        self.game_state = GameState.IN_PROGRESS
        self.possible_moves = possible_moves
        return True

    def can_continue(self) -> bool:
        return self.game_state == GameState.IN_PROGRESS

    def get_next_turn(self) -> Player:
        return self.player

    def is_valid_move(self, move: Move) -> bool:
        if not move.is_same_player(self.player):
            return False
        if not (move.position in self.possible_moves):
            return False
        return True
