# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 1 da Lista 1 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

import turtle # Permite que usemos turtles

def desenhar_quadrado(t, sz): # Função que desenha um quadrado
    for i in range(4):
        t.forward(sz)
        t.left(90)


tela = turtle.Screen() # Criando playground para turtles
tela.bgcolor("lightgreen") # Cor do playground 
tela.title("Questão 1") # Título do playground
werneck = turtle.Turtle() # Criando turtle
werneck.color("#ee89aa") # Cor do turtle
werneck.pensize(4) # Tamanho da caneta

for i in range(6):
    desenhar_quadrado(werneck,20*i) # Chamando função
    werneck.pu() # Levanta a caneta (não desenha)
    werneck.setpos(-10*i,-10*i) # Mudança no cursor
    werneck.pd() # Abaixa a caneta (desenha)

tela.mainloop() # Espera usuário fechar a janela