from Pelota import *
from Jugador import *
import random

pelota = Pelota(random.random(), random.random(), random.randint(0,8,), random.randint(0,4), 1, random.uniform(0.9, 0.1), random.uniform(0.9, 0.1), random.uniform(0.9, 0.1), random.uniform(0.9, 0.1))

vector_x = pelota.estado_get()
print(vector_x)
print("-----")
prediccion = Jugador(pelota.Xt, pelota.O, pelota.G)
