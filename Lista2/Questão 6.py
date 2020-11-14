# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 6 da Lista 2 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect_x(self):
        self.y = -self.y
        return (self.x, self.y)

    def slope_from_origin(self):
        return (self.y/self.x)

p = Point(-3,4)
print(p.slope_from_origin())