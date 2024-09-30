from typing import List
from Domain.Model.player import Player
from Domain.Model.Move.i_rule import IRule
from Domain.Model.Move.possible_move import PossibleMoves
from Domain.Model.Move.board_state import BoardState


class MoveChecker:
    def __init__(self, rules: List[IRule]) -> None:
        self.rules = rules

    def get_possible_moves(self, board_state: BoardState) -> PossibleMoves:
        possible_moves: PossibleMoves = PossibleMoves(Player.NONE, [])
        for rule in self.rules:
            possible_moves = rule.get_possible_moves(board_state, possible_moves)
            if not possible_moves:
                return PossibleMoves(Player.NONE, [])
        return possible_moves
