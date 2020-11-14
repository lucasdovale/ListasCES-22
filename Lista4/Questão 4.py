# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 4 da Lista 4 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

from tkinter import *
from abc import ABCMeta, abstractstaticmethod
import time

# Classe abstrata
class ICommand(metaclass=ABCMeta):
    @abstractstaticmethod
    def executar():
        "Executar"

# Alavanca
class Switch:
    def __init__(self):
        self._comandos = {}
        self._historico = []

    @property
    def historico(self):
        return self._historico

    def registro(self, nome_do_comando, command):
        self._comandos[nome_do_comando] = command

    def executar(self, nome_do_comando):
        if nome_do_comando in self._comandos.keys():
            self._historico.append((time.time(), nome_do_comando))
            self._comandos[nome_do_comando].executar()
        else:
            print(f"Comando [{nome_do_comando}] não reconhecido")

# Cliente
class Cliente:
    def __init__(self):
        self.dinheiro = 0

    def depositar(self):
        self.dinheiro = self.dinheiro + 400
        print(self.dinheiro)

    def sacar(self):
        self.dinheiro = self.dinheiro - 150
        print(self.dinheiro)

# Possíveis comandos do cliente
class depositar(ICommand):

    def __init__(self, cliente):
        self._cliente = cliente

    def executar(self):
        self._cliente.depositar()

class sacar(ICommand):

    def __init__(self, cliente):
        self._cliente = cliente

    def executar(self):
        self._cliente.sacar()

# A função main
if __name__ == "__main__":
    # The Client is the main python app

    # The Cliente is the Reciever
    CLIENTE = Cliente()
    SWITCH = Switch()

    # Create Commands
    SWITCH_ON = depositar(CLIENTE)
    SWITCH_OFF = sacar(CLIENTE)

def saldo():
    print("Saldo:", CLIENTE.dinheiro)

def depositar():
    SWITCH.registro("Deposito", SWITCH_ON)
    SWITCH.executar("Deposito")
    print("Saldo:", CLIENTE.dinheiro)

def saque():
    SWITCH.registro("Saque", SWITCH_OFF)
    SWITCH.executar("Saque")
    print("Saldo:", CLIENTE.dinheiro)

def historico():
    print("Horario e comando feito: ")
    print(SWITCH.historico)

# GUI

tela = Tk()
tela.title("Banco")
tela.geometry('400x200')
botao = Button(tela, text="Saldo", command=saldo)
botao.grid(column=0, row=0)
botao = Button(tela, text="Depositar (400)", command=depositar)
botao.grid(column=1, row=0)
botao = Button(tela, text="Saque (150)", command=saque)
botao.grid(column=2, row=0)
botao = Button(tela, text="Historico", command=historico)
botao.grid(column=3, row=0)
tela.mainloop()