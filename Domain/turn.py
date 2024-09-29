from .Utility.player import Player
from .move_service import MoveService


class GameIsOver(Exception):
    pass


class Turn:
    def __init__(self, move_service: MoveService) -> None:
        self.move_service = move_service
        self.next_player = Player.FIRST

    def update(self) -> None:
        if self.next_player == Player.NONE:
            raise GameIsOver("両プレイヤーとも打ち手がありません")

        now_player = self.next_player
        if self.move_service.has_possible_move(now_player.opponent()):
            self.next_player = now_player.opponent()
        elif self.move_service.has_possible_move(now_player):
            self.next_player = now_player
        else:
            self.next_player = Player.NONE

    def get_next_player(self) -> Player:
        return self.next_player
