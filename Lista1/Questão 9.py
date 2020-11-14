# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 9 da Lista 1 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

import sys

def test(did_pass): # Printa o resultado do teste
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Teste na linha {0} deu certo.".format(linenum)
    else:
        msg = "Teste na linha {0} deu ERRADO.".format(linenum)
    print(msg)


def ehPalindromo(palavra):
    ler = len(palavra)/2
    ler = int(ler)

    a = palavra[0:ler]
    if len(palavra) % 2 ==0:
        b = palavra[ler:]
    else:
        b = palavra[ler+1:]
    if a == b[::-1]:
        return True
    else:
        return False


def test_suite():
    test(ehPalindromo("abba"))
    test(not ehPalindromo("abab"))
    test(ehPalindromo("tenet"))
    test(not ehPalindromo("banana"))
    test(ehPalindromo("straw warts"))
    test(ehPalindromo("a"))
    test(ehPalindromo("")) # A string vazia é palindromo :D


test_suite()