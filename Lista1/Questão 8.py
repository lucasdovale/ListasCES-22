# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 8 da Lista 1 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

print("\t  1   2   3   4   5   6   7   8   9  10  11  12")
print("  :-----------------------------------------------------")
for i in range(1,13):
    a = "{0:2d}:\t".format(i)
    for j in range(1,13):
        a+= "{0:3d} ".format(i*j)
    print(a,end="\n")