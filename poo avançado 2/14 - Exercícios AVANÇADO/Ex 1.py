'''
Gerenciador de Formas Geométricas
Desenvolva um programa que permita ao usuário criar e gerenciar diferentes formas geométricas, como retângulos, triângulos e círculos. 
O usuário deve poder adicionar novas formas, calcular áreas e perímetros, e exibir informações sobre as formas existentes.
'''

import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Exemplo de uso:
rectangle = Rectangle(5, 4)
triangle = Triangle(3, 4, 5)
circle = Circle(3)
print("Área do retângulo:", rectangle.area())
print("Perímetro do triângulo:", triangle.perimeter())
print("Área do círculo:", circle.area())
