from .Board.board import Board
from .Utility.player import Player
from .MoveCheck.move_checker import MoveChecker, PossibleMoves, BoardState, Move


class MoveService:
    def __init__(self, board: Board, move_checker: MoveChecker) -> None:
        self.board = board
        self.move_checker = move_checker
        self.possible_moves: PossibleMoves = None

    def update_possible_move(self, player: Player) -> None:
        self.possible_moves = self.move_checker.get_possible_moves(
            BoardState(self.board, player)
        )

    def has_possible_move(self, player: Player) -> bool:
        return (self.possible_moves.player == player) and (self.possible_moves)

    def is_valid_move(self, move: Move):
        return move in self.possible_moves

    def get_flippable_move(self, move: Move):
        return self.possible_moves.get_flippable_directions(move)
