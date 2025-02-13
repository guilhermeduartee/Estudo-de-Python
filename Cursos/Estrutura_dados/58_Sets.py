#Set (listas)
#Similar a listas
#Evita itens duplicados
#Não utiliza index
# Um set é uma coleção de elementos únicos e não ordenados. É útil quando você precisa garantir que não haja elementos duplicados.

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) #Union
print(num1 - num2) #Difference
print(num1 ^ num2) #Symmetric Difference
print(num1 & num2) #And

print(len(num1)) #Conta a quantidade de itens na lista
print("________________________________________________")
#____________________________________________________________________________

s1 = {1, 2, 3, 4, 5, 6}
s1.update([6, 7, 8, 9, 10]) #adiciona números
s1.remove(1)                #Remove o número, porém se o número não estiver na lista, da erro
s1.discard(90)              #Remove o número, se o número não estiver na lista, não da erro.

print(s1)
print("________________________________________________")
#____________________________________________________________________________

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set3)

print(set4)