#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
multiples_de_4 = list(range(4, 101, 4))
print(multiples_de_4)



#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 

# Crear una lista con cinco elementos
mi_lista = ["manzana", "banana", "naranja", "fresa", "kiwi"]

# Mostrar el penúltimo elemento
penultimo_elemento = mi_lista[-2]
print(penultimo_elemento)



#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
# Crear una lista vacía
mi_lista = []

# Agregar tres palabras
mi_lista.append("hola")
mi_lista.append("mundo")
mi_lista.append("Python")

# Imprimir la lista resultante
print(mi_lista)



#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla. 

# Lista original
animales = ["perro", "gato", "conejo", "tortuga"]

# Reemplazar el segundo valor (índice 1) con "loro"
animales[1] = "loro"

# Reemplazar el último valor (índice -1) con "oso"
animales[-1] = "oso"

# Imprimir la lista resultante
print(animales)



#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros =  [ 8,15,3,22,7]
numeros.remove (max(numeros))
print(numeros)
#)  el método remove() se usa para eliminar ese valor máximo de la lista. Así, al ejecutar
numeros.remove(max(numeros))
#) el número 22 se elimina de la lista.



# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

# Crear la lista con números del 10 al 30, saltando de 5 en 5
numeros = list(range(10, 31, 5))

# Mostrar los dos primeros números
print(numeros[:2])


#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

# Lista original
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazar los valores en los índices 1 y 2
autos[1] = "ford"    # Reemplaza "polo" por "ford"
autos[2] = "toyota"  # Reemplaza "suran" por "toyota"

# Mostrar la lista actualizada
print(autos)
# La salida sería:
['sedan', 'ford', 'toyota', 'gol']



#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.

# Crear una lista vacía
dobles = []

# Agregar el doble de 5, 10 y 15
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Imprimir la lista resultante
print(dobles)
# la salida será:
[10, 20, 30]


#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

# Lista original de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print(compras)
# la lista compras quedará así:

[['leche'], ['arroz', 'tallarines', 'salsa'], ['agua', 'jugo']]



#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

# Crear la lista anidada
lista_anidada = [
    15,                     # Posición lista_anidada[0]
    True,                   # Posición lista_anidada[1]
    [25.5, 57.9, 30.6],    # Posición lista_anidada[2]
    False                   # Posición lista_anidada[3]
]

# Imprimir la lista resultante
print(lista_anidada)
#la salida será:
[15, True, [25.5, 57.9, 30.6], False]
