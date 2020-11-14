# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 7 da Lista 1 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

import sys

def test(did_pass): # Printa o resultado do teste
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Teste na linha {0} deu certo.".format(linenum)
    else:
        msg = "Teste na linha {0} deu ERRADO.".format(linenum)
    print(msg)


def somaDeQuadrados(xs): 
# Função que calcula a soma dos quadrados dos elementos de uma lista
    soma = 0
    for [idx, val] in enumerate(xs):
        soma += val * val
    return soma


def test_suite():
    test(somaDeQuadrados([2,3,4]) == 29)
    test(somaDeQuadrados([ ]) == 0)
    test(somaDeQuadrados([2,-3,4]) == 29)

test_suite()