from abc import ABC, abstractmethod


class Drawer(ABC):
    @abstractmethod
    def draw() -> None:
        pass
