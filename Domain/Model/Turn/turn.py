from Domain.Model.player import Player
from Domain.Service.move_service import MoveService


class GameIsOver(Exception):
    pass


class Turn:
    def __init__(self, move_service: MoveService) -> None:
        self.move_service = move_service
        self.next_player = Player.FIRST
        self.move_service.update_possible_move(self.next_player)

    def update(self) -> None:
        if self.next_player == Player.NONE:
            raise GameIsOver("両プレイヤーとも打ち手がありません")

        now_player = self.next_player
        if self._update(now_player.opponent()):
            return

        if self._update(now_player):
            return

        self.next_player = Player.NONE

    def _update(self, player: Player) -> bool:
        self.move_service.update_possible_move(player)
        if self.move_service.has_possible_move(player):
            self.next_player = player
            return True
        return False

    def get_next_player(self) -> Player:
        return self.next_player
