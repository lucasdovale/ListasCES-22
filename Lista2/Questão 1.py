# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 1 da Lista 2 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

import turtle   # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
size_pen = 3


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:  # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

def red_on():
    tess.fillcolor("red")
    state_num = 2
        
def green_on():
    tess.fillcolor("green")
    state_num = 0

def blue_on():
    tess.fillcolor("blue")

def increase():
    global size_pen
    if size_pen == 20:
        print("O tamanho máximo da caneta é 20")
    else:
        size_pen += 1
        tess.shapesize(outline=size_pen)


def decrease():
    global size_pen
    if size_pen == 1:
        print("O tamanho mínimo da caneta é 1")
    else:
        size_pen -= 1
        tess.shapesize(outline=size_pen)

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

# Chamando funções para as cores vermelho, verde e azul
wn.onkey(red_on, "r")
wn.onkey(green_on, "g")
wn.onkey(blue_on, "b")

# Chamando funções para aumentar ou diminuir a espessura da caneta
wn.onkey(increase, "plus")
wn.onkey(decrease, "minus")

wn.listen()
wn.mainloop()