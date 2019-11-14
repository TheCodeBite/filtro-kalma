import numpy as np
from numpy import linalg as LA
import random

class Jugador():
    def __init__(self, xt, O, g):
        self.H = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ], float)
        
        self.W = np.random.normal(0,O)
        self.G = g
        self.Xt = xt
        self.Zt = self.H@self.Xt

        print(self.Zt)