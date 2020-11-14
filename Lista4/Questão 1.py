# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 1 da Lista 4 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

# Classe Veiculo
class Veiculo:
    def __init__(self, motor):
        self.motor = motor

# Subclasses de Veiculo
class Caminhao(Veiculo):
    def __init__(self, motor):
        super(Caminhao,self).__init__(motor)


class Automovel(Veiculo):
    def __init__(self, motor):
        super(Automovel,self).__init__(motor)


class Motocicleta(Veiculo):
    def __init__(self, motor):
        super(Motocicleta,self).__init__(motor)


class Onibus(Veiculo):
    def __init__(self, motor):
        super(Onibus,self).__init__(motor)


# Classe Motor
class Motor:
    def __init__(self, tipo):
        self.__tipo = "Motor" + tipo

# Subclasses de Motor
class MotorEletrico(Motor):
    def __init__(self):
        super(MotorEletrico,self).__init__("Eletrico")

class MotorHibrido(Motor):
    def __init__(self):
        super(MotorHibrido,self).__init__("Hibrido")

class MotorCombustao(Motor):
    def __init__(self):
        super(MotorCombustao,self).__init__("Combustao")


# Testando a implementação
tesla = Automovel(MotorEletrico())
carreta = Caminhao(MotorCombustao())
busao = Onibus(MotorHibrido())