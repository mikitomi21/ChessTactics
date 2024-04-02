test_data = "1.e4 c5 2.Nf3 e6 3.d3 Nc6 4.g3 d5 5.Nbd2 Nf6 6.Bg2 Be7 60.Kf4 Rb5 61.Ke4 Rb1 62.d5 Re1+ 63.Kf4 Re2 64.f3 Re1 65.Nd4 Rd1 66.Nc6 Kf7 67.Ke5 Re1+ 68.Kf5 Rd1 69.Ne5+ Ke7 70.g6 Rxd5 71.g7 Rxe5+ 72.Kxe5 Kf7 73.g8=Q+ Kxg8 74.Kf6 1-0"
from pieces.piece import Piece
from pieces.king import King
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight


class Converter:
    KINDS_OF_PAWNS = 6

    @staticmethod
    def get_piece(move: str) -> Piece:
        if move[0] == 'K':
            return King()
        elif move[0] == 'Q':
            return Queen()
        elif move[0] == 'R':
            return Rook()
        elif move[0] == 'B':
            return Bishop()
        elif move[0] == 'N':
            return Knight()
