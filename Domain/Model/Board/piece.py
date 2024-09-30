from Domain.Model.player import Player


class InvalidStateError(Exception):
    pass


class Piece:
    def __init__(self):
        self.state = Player.NONE

    def place(self, state: Player) -> None:
        if self.state != Player.NONE:
            raise InvalidStateError("既にコマが置かれています")
        if state not in {Player.FIRST, Player.SECOND}:
            raise InvalidStateError("設定可能な値ではありません")

        self.state = state

    def flip(self) -> None:
        if self.state == Player.NONE:
            raise InvalidStateError("空のピースは反転できません")

        self.state = self.state.opponent()

    def is_empty(self) -> bool:
        return self.state.is_none()

    def is_piece_state(self, state: Player) -> bool:
        return self.state == state

    def get_state(self) -> Player:
        return self.state
