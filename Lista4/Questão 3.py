# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 3 da Lista 4 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

# Classe Fabrica
class Fabrica:
  def fabricar(self, veiculo):
    if veiculo == "caminhao":
         return Caminhao(Motor(""))
    elif veiculo == "automovel":
         return Automovel(Motor(""))
    elif veiculo == "motocicleta":
         return Motocicleta(Motor(""))
    elif veiculo == "onibus":
         return Onibus(Motor(""))
    elif veiculo == "automovel com motor eletrico":
         return Automovel(MotorEletrico())
    elif veiculo == "onibus com motor hibrido":
         return Onibus(MotorHibrido())
    elif veiculo == "caminhao com motor a combustao":
         return Caminhao(MotorCombustao())

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

# Testando implementação
fabrica_de_carros = Fabrica()
carreta = fabrica_de_carros.fabricar("caminhao")
tesla = fabrica_de_carros.fabricar("automovel")
busao = fabrica_de_carros.fabricar("onibus")
carretaComb = fabrica_de_carros.fabricar("caminhao com motor a combustao")
teslaEle = fabrica_de_carros.fabricar("automovel com motor eletrico")
busaoHib = fabrica_de_carros.fabricar("onibus com motor hibrido")