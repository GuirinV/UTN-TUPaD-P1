#1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. 
# Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamar a la función desde el programa principal
if __name__ == "__main__":
    imprimir_hola_mundo()

#2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
# Llamar a esta función desde el programa principal solicitando el nombre al usuario

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
if __name__ == "__main__":
    nombre = input("Por favor, introduce tu nombre: ")
    saludo = saludar_usuario(nombre)
    print(saludo)


#3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

# Llamar a la función con los valores ingresados
informacion_personal(nombre, apellido, edad, residencia)


#4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.


import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Solicitar el radio al usuario
radio = float(input("Ingrese el radio del círculo: "))

# Calcular y mostrar resultados
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"\nPara un círculo con radio {radio}:")
print(f"Área: {area:.2f}")  # Mostrar con 2 decimales
print(f"Perímetro: {perimetro:.2f}")



#5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad 
# de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.


def segundos_a_horas(segundos):
    return segundos / 3600  # 1 hora = 3600 segundos

# Solicitar segundos al usuario
segundos_ingresados = float(input("Ingrese la cantidad de segundos: "))

# Calcular y mostrar resultado
horas = segundos_a_horas(segundos_ingresados)
print(f"{segundos_ingresados} segundos equivalen a {horas:.2f} horas")


# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. 
# Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar número al usuario
numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))

# Llamar a la función
tabla_multiplicar(numero)


#7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con 
# el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

# Solicitar números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Obtener resultados
resultados = operaciones_basicas(num1, num2)

# Mostrar resultados de forma clara
print("\nResultados de las operaciones básicas:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")


#8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC)
    :param peso: Peso en kilogramos (float)
    :param altura: Altura en metros (float)
    :return: Valor del IMC redondeado a 2 decimales
    """
    imc = peso / (altura ** 2)
    return round(imc, 2)

# Solicitar datos al usuario con validación
while True:
    try:
        peso = float(input("Ingrese su peso en kilogramos (ej. 68.5): "))
        altura = float(input("Ingrese su altura en metros (ej. 1.75): "))
        if peso > 0 and altura > 0:
            break
        else:
            print("Error: El peso y altura deben ser valores positivos.")
    except ValueError:
        print("Error: Por favor ingrese números válidos.")

# Calcular y mostrar resultado
imc = calcular_imc(peso, altura)
print(f"\nSu Índice de Masa Corporal (IMC) es: {imc}")

# Mostrar clasificación según OMS
if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 25:
    categoria = "Peso normal"
elif 25 <= imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"Clasificación OMS: {categoria}")



#9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva 
# su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.


def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

# Solicitar temperatura al usuario con validación
while True:
    try:
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        break
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

# Convertir y mostrar resultado
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"\n{celsius}°C equivalen a {fahrenheit:.1f}°F")  # Mostrar con 1 decimal


#10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    """Calcula el promedio de tres números"""
    return (a + b + c) / 3

# Solicitar números al usuario con validación
numeros = []
for i in range(3):
    while True:
        try:
            num = float(input(f"Ingrese el número {i+1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Calcular y mostrar resultado
promedio = calcular_promedio(*numeros)  # Usamos unpacking de la lista
print(f"\nEl promedio de {numeros} es: {promedio:.2f}")  # Mostrar con 2 decimales
