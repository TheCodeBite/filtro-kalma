import numpy as np
from numpy import linalg as LA
import random


class Pelota():
    def __init__(self, x, y, vx, vy, time, sx, sy, svx, svy):
        self.F = np.array(
            [[x, 0, time, 0], 
            [0, y, 0, time],
            [0, 0, vx, 0],
            [0, 0, 0, vy]
            ], float)

        self.G = np.array([
            [1], [1], [1], [1]
            ], float)
        
        self.O = np.array([
            [sx], [sy], [svx], [svy]
            ], float) # O = [X, Y, Vx, Vy] SIGMA

        self.Xt = np.array([
            [x], [y], [vx], [vy]
            ],float) # xt = [X, Y , Vx, Vy]

        self.w = np.random.normal(0, self.O)

    def estado_get(self):
        self.w = np.random.normal(self.O)
        self.Xt = (self.F@self.Xt) + self.G + self.w
        
        return self.Xt