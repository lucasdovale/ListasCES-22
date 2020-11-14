# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 4 da Lista 2 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

import time
 
def rainha(col):
    if col < N:
        for lin in range(N):
            if linha[lin] or diagAsc[lin+col] or diagDesc[lin-col+N-1]:
                continue
            solucao[col] = lin
            linha[lin] = diagAsc[lin+col] = diagDesc[lin-col+N-1] = True
            rainha(col+1)
            linha[lin] = diagAsc[lin+col] = diagDesc[lin-col+N-1] = False
    else:
        global numSol
        numSol = numSol + 1
 
def resolver(n):
    global N
    N = n
    global linha
    linha = [False] * N
    global diagAsc
    diagAsc = [False] * (2 * N - 1)
    global diagDesc
    diagDesc = [False] * (2 * N - 1)
    global numSol
    numSol = 0
    global solucao
    solucao = [0] * N
    rainha(0)

#resolver(4)
#resolver(12)
#resolver(16)

def solvMinute():
    n = 0
    while(1):
        t0 = time.time()
        resolver(n)
        tf = time.time()
        tempo = tf - t0
        if tempo >= 60:
            print(f'(MAIOR QUE 1 MIN) N = {n}, Tempo = {tempo}')
        else:
            print(f'N = {n}, Tempo = {tempo}')
        n += 1

solvMinute()

# Acredito que o valor máximo do tamanho de tabuleiro que o algoritmo
# consegue resolver em menos de 1 minuto depende da máquina que está
# sendo utilizada, e também do algoritmo utilizado. No nosso caso,
# estamos utilizando um algoritmo recursivo, que tem alta complexidade
# de tempo. Com esse algoritmo, esse valor máximo é para N = 14, como
# mostrado pela simulação abaixo.

# N = 0, Tempo = 5.9604644775390625e-06
# N = 1, Tempo = 1.0251998901367188e-05
# N = 2, Tempo = 1.0013580322265625e-05
# N = 3, Tempo = 1.3113021850585938e-05
# N = 4, Tempo = 3.218650817871094e-05
# N = 5, Tempo = 9.775161743164062e-05
# N = 6, Tempo = 0.00021409988403320312
# N = 7, Tempo = 0.000997781753540039
# N = 8, Tempo = 0.003482818603515625
# N = 9, Tempo = 0.017789840698242188
# N = 10, Tempo = 0.056685686111450195
# N = 11, Tempo = 0.2700834274291992
# N = 12, Tempo = 1.380779504776001
# N = 13, Tempo = 7.849056243896484
# N = 14, Tempo = 48.52547311782837
# N = 15, Tempo = 302.6900453567505 (MAIOR QUE 1 MIN)
# N = 16, Tempo = 1893.4755654335022 (MAIOR QUE 1 MIN)
# .
# .
# .
# 
# Obs.: Tempos em segundos.