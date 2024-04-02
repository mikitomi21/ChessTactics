from abc import ABC, abstractmethod
import numpy as np

from game.player import Color
from data_manager.converter import Converter


class Piece(ABC):
    def __init__(self):
        print("piece")

    @abstractmethod
    def make_move(self, board: np.ndarray, pos: str, player: Color):
        pass
