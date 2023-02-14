import math


class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def calcular_perimetro(self):
        base = abs(self.punto2.x - self.punto1.x)
        altura = abs(self.punto2.y - self.punto1.y)
        perimetro = 2 * (base + altura)
        return perimetro

    def calcular_area(self):
        base = abs(self.punto2.x - self.punto1.x)
        altura = abs(self.punto2.y - self.punto1.y)
        area = base * altura
        return area

    def es_cuadrado(self):
        base = abs(self.punto2.x - self.punto1.x)
        altura = abs(self.punto2.y - self.punto1.y)
        return base == altura