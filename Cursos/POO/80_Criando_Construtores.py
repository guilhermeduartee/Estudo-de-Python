# Criando a Classe
class Funcionarios:

    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento 

#Criando o objeto
usuario1 = Funcionarios('Guilherme', 'Duarte', '11/09/2001')
usuario2 = Funcionarios('Gui', 'Azevedo', '12/10/2024')


print(usuario1)
print(usuario2)


#Criando parametros
#usuario1.nome = 'Guilherme'
#usuario1.sobrenome = 'Duarte'
#usuario1.data_nascimento = '11/09/2001'

#usuario2.nome = 'Gui'
#usuario2.sbrenome = 'Azevedo'
#usuario2.data_nascimento = '12/10/2022'