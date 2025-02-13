#Deve se utilizar uma Array quando existe um problema de peformace
#Similar a listas
#Melhor performance
# Arrays são coleções de elementos do mesmo tipo (ex.: todos inteiros ou todos floats).


from array import array

letras = ["a", "b", "c", "d"]
numeros_i = [10, 20, 30, 410]
numeros_f = [1.2, 2.2,3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array("u", ["a", "b", "c", "d"])
numeros_i = array("i", [10, 20, 30, 410])
numeros_f = array("f", [1.2, 2.2,3.2])

print(letras)
print(numeros_i)
print(numeros_f)
