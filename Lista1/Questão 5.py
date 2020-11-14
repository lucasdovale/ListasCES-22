# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 5 da Lista 1 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

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


def contarPalavras(xs): 
# Função que conta quantas palavras tem numa lista e
# conta, também, quantas vezes apareceu a palavara "sam" 
    cont1 = len(xs)
    cont2 = 0
    for [idx, pal] in enumerate(xs): 
        if pal.lower() == "sam":
            cont2 += 1
    cont = (cont1,cont2)
    return cont


def test_suite():
    test(contarPalavras(["werneck", "Leticia", "igor","sam"]) == (4,1))
    test(contarPalavras(["Sam", "leticia","sam"]) == (3,2))
    test(contarPalavras(["Werneck", "SAM"]) == (2,1))
    test(contarPalavras(["Werneck", "leticia", "igor","Lurdes"]) == (4,0))


test_suite()