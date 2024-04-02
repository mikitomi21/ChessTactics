from enum import Enum
import numpy as np

from pieces.pawn import Pawn
from pieces.king import King
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight


class Color(Enum):
    WHITE = 0
    BLACK = 1


class Player:
    def __init__(self, color: Color):
        self.color = color
        self.pawns = self.set_pawns
        self.rooks = self.set_rooks
        self.knights = self.set_knights
        self.bishops = self.set_bishops
        self.queens = self.set_queens
        self.kings = self.set_kings

    @property
    def set_pawns(self) -> np.ndarray:
        position = np.zeros((8, 8))
        if self.color == Color.WHITE:
            position[1, :] = np.ones((1, 8))
        else:
            position[6, :] = np.ones((1, 8))
        return position

    @property
    def set_rooks(self) -> np.ndarray:
        position = np.zeros((8, 8))
        if self.color == Color.WHITE:
            position[0, 0] = 1
            position[0, 7] = 1
        else:
            position[7, 0] = 1
            position[7, 7] = 1
        return position

    @property
    def set_knights(self) -> np.ndarray:
        position = np.zeros((8, 8))
        if self.color == Color.WHITE:
            position[0, 1] = 1
            position[0, 6] = 1
        else:
            position[7, 1] = 1
            position[7, 6] = 1
        return position

    @property
    def set_bishops(self) -> np.ndarray:
        position = np.zeros((8, 8))
        if self.color == Color.WHITE:
            position[0, 2] = 1
            position[0, 5] = 1
        else:
            position[7, 2] = 1
            position[7, 5] = 1
        return position

    @property
    def set_queens(self) -> np.ndarray:
        position = np.zeros((8, 8))
        if self.color == Color.WHITE:
            position[0, 3] = 1
        else:
            position[7, 3] = 1
        return position

    @property
    def set_kings(self) -> np.ndarray:
        position = np.zeros((8, 8))
        if self.color == Color.WHITE:
            position[0, 4] = 1
        else:
            position[7, 4] = 1
        return position

    def get_all_positions(self) -> np.array:
        """
        Return ndarray vectors 6x8x8 in order for:
        pawns -> rooks -> knights -> bishops -> queens -> kings
        """
        return np.array(
            [
                self.pawns,
                self.rooks,
                self.knights,
                self.bishops,
                self.queens,
                self.kings,
            ]
        )

    def get_board(self, piece):
        if isinstance(piece, Pawn):
            return self.pawns
        elif isinstance(piece, Rook):
            return self.rooks
        elif isinstance(piece, Knight):
            return self.knights
        elif isinstance(piece, Bishop):
            return self.bishops
        elif isinstance(piece, Queen):
            return self.queens
        elif isinstance(piece, King):
            return self.kings
