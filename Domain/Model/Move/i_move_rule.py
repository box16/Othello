from abc import ABC, abstractmethod
from Domain.Model.Move.possible_move import PossibleMoves
from Domain.Model.Board.board import Board
from Domain.Model.player import Player


class IMoveRule(ABC):
    @abstractmethod
    def get_possible_moves(self, board: Board, player: Player) -> PossibleMoves:
        pass
