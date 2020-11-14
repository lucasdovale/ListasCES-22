# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 10 da Lista 2 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

# Estudo dos Decoradores

def limpar_palavras(função):
    def cleanword():
        a = ""
        for caractere in função():
           if caractere.isalpha():
             a += caractere
        return a
    return cleanword

@limpar_palavras  # Decorador que vai ser executado antes da função a seguir
def palavra():
    return 'w@h#o??'


palavra = palavra()
print(palavra)