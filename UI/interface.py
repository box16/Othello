from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def start_game() -> None:
        pass

    @abstractmethod
    def update_game() -> None:
        pass

    @abstractmethod
    def end_game() -> None:
        pass
