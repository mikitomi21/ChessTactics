from .piece import *


class Pawn(Piece):
    def __init__(self):
        super().__init__()
        print("Pawn")

    def make_move(self, board: np.ndarray, pos: str, player: Color):
        y, x = Converter.position_to_int(pos)
