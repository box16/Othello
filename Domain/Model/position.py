from dataclasses import dataclass
from Domain.Model.direction import Direction


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other) -> "Position":
        if not isinstance(other, (Position, Direction)):
            raise TypeError("PositionかDirectionを入力してください")

        return Position(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar) -> "Position":
        if not isinstance(scalar, int):
            raise TypeError("intを入力してください")

        return Position(self.x * scalar, self.y * scalar)

    def is_inside(self, top_left, bottom_right) -> bool:
        if not isinstance(top_left, Position):
            raise TypeError("Positionを入力してください")
        if not isinstance(bottom_right, Position):
            raise TypeError("Positionを入力してください")

        x_is_inside = top_left.x <= self.x <= bottom_right.x
        y_is_inside = top_left.y <= self.y <= bottom_right.y
        return x_is_inside and y_is_inside
