# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 3 da Lista 1 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

def soma_ate(n): # Função que soma todos os inteiros menores ou iguais a n
    soma = 0
    for i in range(n+1):
        soma += i
    return soma


print(soma_ate(10))
