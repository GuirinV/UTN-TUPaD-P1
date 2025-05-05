# 1) Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga 
# “Es mayor de edad”.

# Solicitar la edad del usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Verificar si el usuario es mayor de 18 años
if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. 
# Si la nota es mayor o igual a 6, deberá por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.

# Solicitar la nota al usuario
nota = float(input("Por favor, ingresa tu nota: "))

# Verificar si la nota es mayor o igual a 6
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    
# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar 
# si un número es par o impar.

# Programa para verificar si un número es par
numero = int(input("Por favor, ingrese un número: "))

# Verificamos si el número es par
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

# Solicitar la edad al usuario
edad = int(input("Por favor, introduce tu edad: "))

# Determinar la categoría según la edad
if edad < 12:
    categoria = "Niño/a"
elif 12 <= edad < 18:
    categoria = "Adolescente"
elif 18 <= edad < 30:
    categoria = "Adulto/a joven"
else:
    categoria = "Adulto/a"

# Imprimir la categoría
print(f"Tu categoría es: {categoria}")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla 
# el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de 
# elementos que tiene un iterable tal como una lista o un string.

# Solicitar al usuario que ingrese una contraseña
contraseña = input("Por favor, ingrese una contraseña (entre 8 y 14 caracteres): ")

# Verificar la longitud de la contraseña
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana 
# y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. 
# Imprimir el resultado por pantalla

import random
from statistics import mode, median, mean

# Generar la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Imprimir los resultados
print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Comparar los valores para determinar el sesgo
if media > mediana:
    sesgo = "sesgo positivo"
elif media < mediana:
    sesgo = "sesgo negativo"
else:
    sesgo = "no hay sesgo"



#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
# Solicitar una frase o palabra al usuario
frase = input("Por favor, ingresa una frase o palabra: ")

# Verificar si la última letra es una vocal
if frase[-1].lower() in 'aeiou':
    frase += '!'
    
# Imprimir el resultado
print(frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Solicitar el nombre del usuario
nombre = input("Por favor, ingresa tu nombre: ")

# Solicitar la opción deseada
print("Elige una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra mayúscula")
opcion = input("Ingresa 1, 2 o 3: ")

# Transformar el nombre según la opción seleccionada
if opcion == '1':
    resultado = nombre.upper()
    print("Tu nombre en mayúsculas es:", resultado)
elif opcion == '2':
    resultado = nombre.lower()
    print("Tu nombre en minúsculas es:", resultado)
elif opcion == '3':
    resultado = nombre.title()
    print("Tu nombre con la primera letra mayúscula es:", resultado)
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).


# Solicitar al usuario la magnitud del terremoto
magnitud = float(input("Introduce la magnitud del terremoto: "))

# Clasificar la magnitud
if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:  # magnitud >= 7
    categoria = "Extremo (puede causar graves daños a gran escala)"

# Imprimir el resultado
print(f"La magnitud del terremoto es: {categoria}")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), 
# qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir 
# por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
# Preguntar al usuario en qué hemisferio se encuentra

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()

# Preguntar al usuario el mes y el día
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Determinar la estación según el hemisferio
if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha no válida"

elif hemisferio == 'S':
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha no válida"

else:
    estacion = "Hemisferio no válido"

# Imprimir la estación
print(f"Te encuentras en: {estacion}")