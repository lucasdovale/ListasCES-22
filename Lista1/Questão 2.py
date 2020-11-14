# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 2 da Lista 1 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

import turtle # Permite que usemos turtles

def desenhar_poligono(t, n, sz): # Função que desenha um poligono regular
    ang = 360/n
    for i in range(n):
        t.forward(sz)
        t.left(ang)


tela = turtle.Screen() # Criando playground para turtles
tela.bgcolor("lightgreen") # Cor do playground 
tela.title("Questão 1") # Título do playground
werneck = turtle.Turtle() # Criando turtle
werneck.color("#ee89aa") # Cor do turtle
werneck.pensize(4) # Tamanho da caneta

desenhar_poligono(werneck,8,50) # Chamando função para caso teste

tela.mainloop() # Espera usuário fechar a janela