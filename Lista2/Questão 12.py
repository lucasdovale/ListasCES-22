# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 12 da Lista 2 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

class Humano:

    def peso(self):
        print("10kg")

    def altura(self):
        print("1.80m")

class Animal:

    def peso(self):
        print("50kg")

    def altura(self):
        print("5.20m")
        
def pesoAltura(Objeto):
    Objeto.peso()
    Objeto.altura()

Lucas = Humano()
Girafa = Animal()

pesoAltura(Lucas)
pesoAltura(Girafa)

# Nota-se que temos duas classes totalmente diferentes,
# mas que implementam funções com mesmo nome

# Dessa forma, podemos criar uma função que recebe um objeto genérico
# e chamar as funções peso e altura, independentemente do objeto que seja
# Isso resume o polimorfismo.

# A filosofia do Duck Typing é justamente essa, não importa o objeto 
# que seja passado, se ele tem peso e altura é o que importa.
# Analogia com o pato: se anda como um pato, nada como um pato e faz 
# quack feito um pato, entao deve ser um pato, e se não for, 
# não importa, porque faz tudo q um pato faz