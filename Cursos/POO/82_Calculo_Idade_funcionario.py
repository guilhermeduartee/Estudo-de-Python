# Criando a Classe

from datetime import datetime

class Funcionarios:

    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = int(ano_nascimento)
    
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

#Criando o objeto
usuario1 = Funcionarios('Guilherme', 'Duarte', '2001')
usuario2 = Funcionarios('Gui', 'Azevedo', '2005')
usuario3 = Funcionarios('Miguel', 'Duarte', '2011')

#Print
print(Funcionarios.idade_funcionario(usuario1))
