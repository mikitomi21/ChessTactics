from player import Player, Color
from data_manager.converter import Converter


class GameManager:
    def __init__(self):
        self.current_player = Color.WHITE
        self.players = [Player(Color.WHITE), Player(Color.BLACK)]

    def next_player(self):
        self.current_player = (
            Color.WHITE if self.current_player == Color.BLACK else Color.WHITE
        )

    def get_move(self, move: str):
        piece = Converter.get_piece(move)
        piece.make_move(self.current_player.)