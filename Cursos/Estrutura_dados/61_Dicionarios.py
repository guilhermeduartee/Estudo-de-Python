#Dicionários
#Utiliza index no formato de keys e Values
#Aceita string, integer, float boolean...

aluno ={'nome': 'Guilherme', 'idade':23, 'nome_final': 'D', 'aprovação': True}

print(aluno)

aluno.update({'nome': 'Duarte', 'nota_final':'B'})
print(aluno)

aluno.update({'endereco': 'Rua A'})
print(aluno)

print(aluno['nome'])

print("________________________________________________")
#____________________________________________________________________________

aluno ={'nome': 'Guilherme', 'idade':23, 'nome_final': 'D', 'aprovação': True}

for x in aluno.values():
    print(x)

for keys, values in aluno.items():
    print(keys, values)