# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 5 da Lista 4 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

import abc

# Classe contexto (interface)
class Context:
    def __init__(self, estado):
        self._estado = estado

    def request(self):
        self._estado.handle()

# Classe base Estado
class Estado(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self):
        pass

# Possíveis estados

# Estado Draft
class Draft(Estado):
    def handle(self):
        pass

    def __init__(self):
        print("Draft")

# Estado Moderation
class Moderation(Estado):
    def handle(self):
        pass

    def __init__(self):
        print("Moderation")

# Estado Published
class Published(Estado):
    def handle(self):
        pass

    def __init__(self):
        print("Published")


# Main
def main():

    draft = Draft()
    moderation = Moderation()
    published = Published()

    context = Context(draft)
    context.request()
    
    context = Context(moderation)
    context.request()

    context = Context(published)
    context.request()



if __name__ == "__main__":
    main()