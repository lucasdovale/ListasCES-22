# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 11 da Lista 2 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

# Argumentos
def idade(pessoa, *args):
    print(f'Pessoa: {pessoa}')
    print("Idade correta:")
    correct = 0
    for age in args:
        if age == 15:
            correct = age
            print(correct)
            break
    if correct != 15:
        print("Não foi encontrada a idade correta")

idade('Lucas',10,16,19)
idade('Clovis',13,15,18)

# Dicionário
def habitantes(inicial, **kwargs):
    morreu = kwargs.get('morreu')
    nasceu = kwargs.get('nasceu')
    habit = inicial
    if (morreu):
        habit -= morreu
    if (nasceu):
        habit += nasceu
    return habit

print(habitantes(1000, morreu=200, nasceu=300))
print(habitantes(2000, morreu=700, nasceu=500))