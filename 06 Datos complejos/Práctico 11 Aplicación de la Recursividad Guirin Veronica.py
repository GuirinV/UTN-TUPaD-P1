##) Práctico 11: Aplicación de la Recursividad

#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar 
# en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    numero = int(input("Ingrese un número entero positivo: "))
    if numero < 1:
        print("Por favor, ingrese un número entero positivo mayor o igual a 1.")
    else:
        print(f"Factoriales de los números entre 1 y {numero}:")
        for i in range(1, numero + 1):
            print(f"{i}! = {factorial(i)}")
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")


#2)Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.  

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    posicion = int(input("Ingrese la posición hasta la cual desea generar la serie de Fibonacci: "))
    if posicion < 0:
        print("Por favor, ingrese un número entero no negativo.")
    else:
        print(f"Serie de Fibonacci hasta la posición {posicion}:")
        for i in range(posicion + 1):
            print(f"Posición {i}: {fibonacci(i)}")
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")

    
#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). 
# Prueba esta función en un algoritmo general

def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: n^m = n * n^(m-1)
    else:
        return base * potencia(base, exponente - 1)


#4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación
# en binario como una cadena de texto. 
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. 
# Para convertir un número decimal a binario, se puede seguir este procedimiento: 
#1. Dividir el número por 2. 
#2. Guardar el resto (0 o 1). 
#3. Repetir el proceso con el cociente hasta que llegue a 0. 
#4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario. 

def decimal_a_binario(n):
    if n == 0:
        return "0"  # Caso base: 0 en decimal es 0 en binario
    elif n == 1:
        return "1"  # Caso base: 1 en decimal es 1 en binario
    else:
        # Llamada recursiva: dividir n entre 2 y concatenar los restos en orden inverso
        return decimal_a_binario(n // 2) + str(n % 2)

# PROBAR: 
# Pedir al usuario un número decimal
try:
    numero = int(input("Ingrese un número entero positivo: "))
    if numero < 0:
        print("Error: El número debe ser positivo.")
    else:
        binario = decimal_a_binario(numero)
        print(f"El número {numero} en binario es: {binario}")
except ValueError:
    print("Error: Ingrese un número entero válido.")


#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True 
# si es un palíndromo o False si no lo es. 
# Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    # Caso base: si la longitud es 0 o 1, es palíndromo
    if len(palabra) <= 1:
        return True
    # Verificar si el primer y último carácter son iguales
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con la palabra sin el primer y último carácter
    return es_palindromo(palabra[1:-1])


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos 
# sus dígitos. 
# Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 
# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5) 

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
    
#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
# y así sucesivamente hasta llegar al último nivel con un solo bloque. 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques 
# que necesita para construir toda la pirámide. 
# Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) 
# y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número. 
# Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4 
# contar_digito(123456, 7)     → 0   


def contar_digito(numero, digito):
    # Caso base: número de un solo dígito
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        # Verificar el último dígito y llamar recursivamente con el resto del número
        ultimo_digito = numero % 10
        resto_numero = numero // 10
        return (1 if ultimo_digito == digito else 0) + contar_digito(resto_numero, digito)


