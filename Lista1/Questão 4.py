# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 4 da Lista 1 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

import sys

def test(did_pass): # Printa o resultado do teste
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Teste na linha {0} deu certo.".format(linenum)
    else:
        msg = "Teste na linha {0} deu ERRADO.".format(linenum)
    print(msg)


def somarElementos(xs): 
# Função que calcula a soma dos elementos de uma lista, 
# sem incluir o primeiro número par
    soma = 0
    primeiroPar = False
    for [idx, val] in enumerate(xs):
        soma += val
        if (val % 2 == 0) and (primeiroPar == False):
            primeiroPar = True
            soma -= val   
    return soma


def test_suite():
    test(somarElementos([2,3,4]) == 7)
    test(somarElementos([1,2,3,4]) == 8)
    test(somarElementos([2,-3,8]) == 5)
    test(somarElementos([1,-3,5]) == 3)


test_suite()