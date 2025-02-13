#Listas
#Adicionando itens a lista

# Lista original -> frutas = ['Maçã', 'banana', 'manga', 'uva']

frutas = ['Maçã', 'banana', 'manga', 'uva']

frutas[1:3] = ['abacaxi', 'abacate'] #[x:y] Substitui do intervalo X ao Y, porém sem substituir o Y.
frutas[1]= 'morango' #Substitui itens
frutas.append ('abacaxi') #Adiciona itens ao final da fila
frutas.insert(2, 'abacate') #Adiciona o item que você escolher no local que você escolher.
print(frutas)
