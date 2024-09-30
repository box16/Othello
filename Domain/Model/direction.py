from dataclasses import dataclass


@dataclass(frozen=True)
class Direction:
    x: int
    y: int

    def __mul__(self, scalar) -> "Direction":
        if not isinstance(scalar, int):
            raise TypeError("intを入力してください")

        return Direction(self.x * scalar, self.y * scalar)
