# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 6 da Lista 1 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

import sys

def test(did_pass): # Printa o resultado do teste
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Teste na linha {0} deu certo.".format(linenum)
    else:
        msg = "Teste na linha {0} deu ERRADO.".format(linenum)
    print(msg)


def ehPrimo(num): # Função que verifica se o número é primo
    if num < 2:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True


def test_suite():
    test(ehPrimo(11))
    test(not ehPrimo(35))
    test(ehPrimo(19911121))
    test(not ehPrimo(15101999))

test_suite()

# Nasci em 15/10/1999. Pelo teste, 15101999 não é primo.
# Em uma turma de 100 pessoas, temos 100 números de 8 algarismos,
# o que torna bastante improvável que tenha muitos primos, mas acredito
# que tenha pelo menos 5.