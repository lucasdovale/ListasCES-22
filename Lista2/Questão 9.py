# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 9 da Lista 2 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

class Shape:

    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Plotter:

    def plot(self, ratio, topleft):
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))

class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'

class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self,side):
        self.side = side

class RegularHexagon(RegularPolygon):
    geometric_type = 'RegularHexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)

class Square(RegularPolygon):
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side

hexagon = RegularHexagon(10)
print(hexagon.area()) # 259.8076211
print(hexagon.get_geometric_type())
hexagon.plot(0.8,(75,77)) # Plotting at (75,77), ratio 0.8

square = Square(12)
print(square.area()) # 144
print(square.get_geometric_type()) # Square
square.plot(0.93,(74,75))

print(square.__class__.__mro__)
# prints:
# (<class '__main__.Square'>, <class '__main___.RegularPolygon'>,
# <class '__main__.Polygon'>, <class '__main__.Shape'>, <class '__main__.Plotter'>, <class 'object'>)

# Nota-se acima que o MRO faz uma busca em DFS na árvore de herança
# das classes, de acordo com o diagrama previsto no slide, agora,
# criaremos mais uma classe de polígonos irregulares

class IrregularPolygon(Polygon):
    geometric_type = 'Irregular Polygon'

    def __init__(self,*args):
        pass

class IrregularTriangle(IrregularPolygon):
    geometric_type = 'Irregular Triangle'

    def __init__(self,base,altura):
            self.base = base
            self.altura = altura

class IsoscelesTriangle(IrregularTriangle):
    geometric_type = 'Isosceles Triangle'

    def area(self):
        return self.base * self.altura/2

class ScaleneTriangle(IrregularTriangle):
    geometric_type = 'Scalene Triangle'

    def area(self):
        return self.base * self.altura/2

# Aqui, temos uma nova árvore de herança, sendo a classe IrregularPolygon
# herdada da classe Polygon e a classe IrregularTriangle herdada
# da classe IrregularPolygon. Além disso, as classes de triangulo 
# Isosceles e Escaleno herdadas de IrregularTriangle.
# Vejamos agora a nova MRO:

trianguloIso = IsoscelesTriangle(6,8)
print(trianguloIso.area()) # 24
print(trianguloIso.get_geometric_type()) # Isosceles Triangle
print(trianguloIso.__class__.__mro__)

# prints:
# (<class '__main__.IsoscelesTriangle'>, <class '__main__.IrregularTriangle'>,
# <class '__main__.IrregularPolygon'>, <class '__main__.Polygon'>, 
# <class '__main__.Shape'>, <class '__main__.Plotter'>, <class 'object'>)

# Note que já temos uma árvore diferente de MRO, mas que obedece a lógica da
# herança múltipla.