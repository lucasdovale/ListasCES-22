# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 10 da Lista 1 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

def somarComplexos (num1, num2): # Função que soma dois números complexos
    num3 = (num1[0]+num2[0],num1[1]+num2[1])
    return num3


# Representação
a = 3
b = 2
numComplexo = (a,b) # a + bi
print(numComplexo)

# Soma
print (somarComplexos ((1,2),(2,3)))