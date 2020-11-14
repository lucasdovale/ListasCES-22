# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 8 da Lista 2 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 10 da Lista 2 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

# Estudo dos Decoradores

class Aluno:

    def __init__(self, nome, anoMatricula, curso):
        self.nome = nome
        self.anoMatricula = anoMatricula
        self.curso = curso

    def cursoAluno(self):
        return self.curso

    # Método abstrato
    def get_idade(self): # 
        raise NotImplementedError
    # Com o método abstrato, conseguimos ter diversas implementações
    # diferentes para diferentes tipos de plataforma. Pode-se fazer
    # uma analogia ao TAD (Tipo Abstrato de Dados).

    # Método estático
    def formacao(anoMatricula): 
        return anoMatricula + 4
    # Aqui conseguimos manter um agrupamento lógico das funções
    # tudo dentro da classe, e sem permitir que a função acesse 
    # atributos da classe.

    # Método de classe
    def alunoPorAnoFormacao(cls, nome, curso, formacao):
        return cls(nome, curso, formacao - 4)
    # Já aqui conseguimos ter acesso aos atributos da classe,
    # podendo instanciar objetos da classe e usar o Construtor
    # de diversas formas.

Lucas = Aluno('Werneck',2018,'COMP')
Italo = Aluno('Leitinho',2017,'MEC')

print(Lucas.cursoAluno())
print(Lucas.formacao(Lucas.anoMatricula))
novoAluno = Aluno.alunoPorAnoFormacao('Tulio','ELE',2020)
print(novoAluno.curso)
print(novoAluno.nome)
print(novoAluno.anoMatricula)