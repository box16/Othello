from abc import ABC, abstractmethod
from Domain.Model.Move.possible_move import PossibleMoves
from Domain.Model.Move.board_state import BoardState


class IMoveRule(ABC):
    @abstractmethod
    def get_possible_moves(
        self, board_state: BoardState, possible_moves: PossibleMoves
    ) -> PossibleMoves:
        pass
