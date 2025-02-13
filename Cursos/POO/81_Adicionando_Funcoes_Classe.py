# Criando a Classe
class Funcionarios:

    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento 
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

#Criando o objeto
usuario1 = Funcionarios('Guilherme', 'Duarte', '11/09/2001')
usuario2 = Funcionarios('Gui', 'Azevedo', '12/10/2024')
usuario3 = Funcionarios('Miguel', 'Duarte', '13/02/2011')

print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario3))
