# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for i in range(101):  # range(101) incluye el 0 y va hasta el 100
    print(i)  # Imprime el número actual


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene.

# Solicitar al usuario un número entero
numero = input("Por favor, introduce un número entero: ")

# Verificar si el número es negativo y contar los dígitos
if numero.startswith('-'):
    cantidad_digitos = len(numero) - 1  # Restamos 1 para no contar el signo negativo
else:
    cantidad_digitos = len(numero)

# Imprimir la cantidad de dígitos
print(f"El número {numero} tiene {cantidad_digitos} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores. 
# Solicitar al usuario que ingrese dos números
valor1 = int(input("Ingresa el primer número: "))
valor2 = int(input("Ingresa el segundo número: "))

# Asegurarse de que valor1 sea menor que valor2
if valor1 > valor2:
    valor1, valor2 = valor2, valor1  # Intercambiar los valores si es necesario

# Calcular la suma de los números entre valor1 y valor2, excluyéndolos
suma = sum(range(valor1 + 1, valor2))

# Mostrar el resultado
print(f"La suma de los números enteros entre {valor1} y {valor2} (excluyéndolos) es: {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 

# Inicializamos la variable para almacenar la suma total
total_acumulado = 0

# Iniciamos un bucle que continuará hasta que el usuario ingrese 0
while True:
    # Pedimos al usuario que ingrese un número entero
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    
    # Verificamos si el número ingresado es 0
    if numero == 0:
        break  # Salimos del bucle si el usuario ingresa 0
    
    # Sumamos el número ingresado al total acumulado
    total_acumulado += numero

# Mostramos el total acumulado al finalizar
print("El total acumulado es:", total_acumulado)


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos 
# intentos fueron necesarios para acertar el número. 
import random

# Generar un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)
intentos = 0
adivinado = False

print("¡Bienvenido al juego de adivinar el número!")
print("Tienes que adivinar un número entre 0 y 9.")

# Bucle para permitir múltiples intentos
while not adivinado:
    intento = int(input("Introduce tu número: "))
    intentos += 1
    
    if intento < 0 or intento > 9:
        print("Por favor, introduce un número válido entre 0 y 9.")
    elif intento < numero_aleatorio:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_aleatorio:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        adivinado = True
        print(f"¡Felicidades! Has adivinado el número {numero_aleatorio} en {intentos} intentos.")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for numero in range(100, -1, -1):  # Desde 100 hasta 0
    if numero % 2 == 0:  # Verifica si el número es par
        print(numero)  # Imprime el número par

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
# Solicitar al usuario un número entero positivo
numero = int(input("Introduce un número entero positivo: "))

# Verificar que el número sea positivo
if numero < 0:
    print("Por favor, introduce un número entero positivo.")
else:
    # Calcular la suma de los números desde 0 hasta el número indicado
    suma = sum(range(numero + 1))
    
    # Mostrar el resultado
    print(f"La suma de todos los números entre 0 y {numero} es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números 
# son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

# Inicializamos los contadores
pares = 0
impares = 0
negativos = 0
positivos = 0

# Pedimos al usuario que ingrese 100 números
for i in range(100):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    
    # Contamos si el número es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Contamos si el número es negativo o positivo
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

# Mostramos los resultados
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números negativos: {negativos}")
print(f"Números positivos: {positivos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

cantidad_numeros = 100

# Inicializamos una lista para almacenar los números
numeros = []

# Pedimos al usuario que ingrese los números
print(f"Ingrese {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
    while True:
        try:
            numero = int(input(f"Número {i + 1}: "))
            numeros.append(numero)
            break  # Salimos del bucle si la entrada es válida
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# Calculamos la media
media = sum(numeros) / cantidad_numeros

# Mostramos el resultado
print(f"La media de los {cantidad_numeros} números ingresados es: {media}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Solicitar al usuario que ingrese un número
numero = input("Por favor, ingresa un número: ")

# Invertir el orden de los dígitos
numero_invertido = numero[::-1]

# Mostrar el resultado
print("El número invertido es:", numero_invertido)
