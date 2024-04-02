from player import Player, Color
from data_manager.converter import Converter


class GameManager:
    def __init__(self):
        self.current_player = Color.WHITE
        self.players = [Player(Color.WHITE), Player(Color.BLACK)]

    def next_player(self):
        self.current_player = (
            Color.WHITE if self.current_player == Color.BLACK else Color.BLACK
        )

    def make_move(self, pos: str):
        piece = Converter.get_piece(pos)
        board = self.players[self.current_player.value].get_board(piece)
        (y_new, x_new), (y_old, x_old) = piece.make_move(board, pos, self.current_player)
