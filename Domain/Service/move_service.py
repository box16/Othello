from Domain.Model.Board.board import Board
from Domain.Model.player import Player
from Domain.Model.Move.move import Move
from Domain.Model.Move.possible_move import PossibleMoves
from Domain.Model.Move.i_move_rule import IMoveRule


class MoveService:
    def __init__(self, board: Board, move_rule: IMoveRule) -> None:
        self.board = board
        self.move_rule = move_rule
        self.possible_moves: PossibleMoves = None

    def update_possible_move(self, player: Player) -> None:
        self.possible_moves = self.move_rule.get_possible_moves(self.board, player)

    def has_possible_move(self, player: Player) -> bool:
        return (self.possible_moves.player == player) and (self.possible_moves)

    def is_valid_move(self, move: Move):
        return move in self.possible_moves

    def get_flippable_move(self, move: Move):
        return self.possible_moves.get_flippable_directions(move)
