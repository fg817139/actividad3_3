import math
from ejercicio2 import Punto

class Punto:
    def mostrar(self):
        print(f"({self.x}, {self.y})")

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def calcular_distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return distancia