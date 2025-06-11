# # # # # # # # # # # # # # # # # # #  EJERCICIO 1 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 1) Dado el diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

# Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

# Resultado
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Mostrar el diccionario actualizado
print(precios_frutas)

# # # # # # # # # # # # # # # # # # #  EJERCICIO 2 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

# Resultado

# Asumiendo que precios_frutas ya contiene las frutas añadidas anteriormente
precios_frutas = {
    'Banana': 1200,
    'Anand': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

# Actualizar los precios de las frutas indicadas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostrar el diccionario actualizado
print(precios_frutas)

# # # # # # # # # # # # # # # # # # #  EJERCICIO 3 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# crear una lista que contenga únicamente las frutas sin los precios

# Resultado
# Asumiendo que precios_frutas está actualizado como en el punto anterior
precios_frutas = {
    'Banana': 1330,
    'Anand': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

# Crear una lista con solo los nombres de las frutas (claves del diccionario)
lista_frutas = list(precios_frutas.keys())

# Mostrar la lista resultante
print(lista_frutas)

# # # # # # # # # # # # # # # # # # #  EJERCICIO 4 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe

# Resultado
# Programa para almacenar y consultar números telefónicos

# Paso 1: Cargar 5 contactos
contactos = {}
print("Por favor ingresa 5 contactos:")

for i in range(5):
    nombre = input(f"Ingresa el nombre del contacto {i+1}: ")
    telefono = input(f"Ingresa el número de teléfono de {nombre}: ")
    contactos[nombre] = telefono

# Paso 2: Consultar contactos
print("\n--- Consulta de contactos ---")
while True:
    consulta = input("\nIngresa un nombre para buscar (o 'salir' para terminar): ")
    
    if consulta.lower() == 'salir':
        break
    
    if consulta in contactos:
        print(f"El número de {consulta} es: {contactos[consulta]}")
    else:
        print(f"Lo siento, no existe un contacto llamado '{consulta}'.")

print("\nPrograma terminado. Estos son todos tus contactos:")
print(contactos)

# # # # # # # # # # # # # # # # # # #  EJERCICIO 5 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

# Resultado
# Solicitar frase al usuario
frase = input("Ingresa una frase: ")

# Dividir la frase en palabras
palabras = frase.split()

# 1. Obtener palabras únicas usando un set
palabras_unicas = set(palabras)

# 2. Contar la frecuencia de cada palabra
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

# Mostrar resultados
print("\nPalabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# # # # # # # # # # # # # # # # # # #  EJERCICIO 6 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

# Resultado
# Diccionario para almacenar los alumnos y sus notas
alumnos = {}

# Ingresar datos de 3 alumnos
for i in range(3):
    nombre = input(f"\nIngrese el nombre del alumno {i+1}: ")
    
    # Ingresar las 3 notas para cada alumno
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    
    # Almacenar como tupla en el diccionario
    alumnos[nombre] = tuple(notas)

# Calcular y mostrar promedios
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {notas} -> Promedio: {promedio:.2f}")

# # # # # # # # # # # # # # # # # # #  EJERCICIO 7 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Resultado
# Sets de estudiantes que aprobaron cada parcial
parcial1 = {"Juan", "María", "Carlos", "Ana", "Luis"}
parcial2 = {"Ana", "Pedro", "Carlos", "Sofía", "Luis"}

# a) Estudiantes que aprobaron ambos parciales
ambos_parciales = parcial1 & parcial2  # Intersección
print("Aprobaron ambos parciales:", ambos_parciales)

# b) Estudiantes que aprobaron solo uno de los dos
solo_parcial1 = parcial1 - parcial2  # Diferencia
solo_parcial2 = parcial2 - parcial1  # Diferencia
solo_uno = solo_parcial1 | solo_parcial2  # Unión
print("Aprobaron solo un parcial:", solo_uno)

# c) Lista total de aprobados (al menos uno)
total_aprobados = parcial1 | parcial2  # Unión
print("Total de aprobados (al menos un parcial):", total_aprobados)

# # # # # # # # # # # # # # # # # # #  EJERCICIO 8 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

# Resultado
# Diccionario inicial de productos y su stock
stock = {
    "manzanas": 50,
    "naranjas": 30,
    "plátanos": 20
}

def consultar_stock(producto):
    """Consulta el stock de un producto."""
    return stock.get(producto, "El producto no existe.")

def agregar_unidades(producto, unidades):
    """Agrega unidades al stock de un producto existente."""
    if producto in stock:
        stock[producto] += unidades
        return f"Se han agregado {unidades} unidades a {producto}. Nuevo stock: {stock[producto]}"
    else:
        return "El producto no existe."

def agregar_producto(producto, unidades):
    """Agrega un nuevo producto al stock."""
    if producto not in stock:
        stock[producto] = unidades
        return f"Se ha agregado el producto {producto} con {unidades} unidades."
    else:
        return "El producto ya existe."

# Menú de opciones para el usuario
while True:
    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    
    opcion = input("Selecciona una opción (1-4): ")
    
    if opcion == "1":
        producto = input("Ingresa el nombre del producto: ")
        print(consultar_stock(producto))
    
    elif opcion == "2":
        producto = input("Ingresa el nombre del producto: ")
        unidades = int(input("Ingresa la cantidad de unidades a agregar: "))
        print(agregar_unidades(producto, unidades))
    
    elif opcion == "3":
        producto = input("Ingresa el nombre del nuevo producto: ")
        unidades = int(input("Ingresa la cantidad de unidades: "))
        print(agregar_producto(producto, unidades))
    
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

# # # # # # # # # # # # # # # # # # #  EJERCICIO 9 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Permití consultar qué actividad hay en cierto día y hora.

# Resultado
# Definimos la agenda como un diccionario
agenda = {}

def agregar_evento(dia, hora, evento):
    # Usamos una tupla (día, hora) como clave
    clave = (dia, hora)
    agenda[clave] = evento
    print(f"Evento '{evento}' agregado para el {dia} a las {hora}.")

def consultar_evento(dia, hora):
    # Usamos la tupla (día, hora) para consultar
    clave = (dia, hora)
    evento = agenda.get(clave, "No hay eventos programados.")
    return evento

# Ejemplo de uso
agregar_evento("2023-10-15", "10:00", "Reunión con el equipo")
agregar_evento("2023-10-15", "14:00", "Cita médica")

# Consultar eventos
print(consultar_evento("2023-10-15", "10:00"))  # Debería mostrar el evento de la reunión
print(consultar_evento("2023-10-15", "14:00"))  # Debería mostrar la cita médica
print(consultar_evento("2023-10-15", "16:00"))  # Debería indicar que no hay eventos

# # # # # # # # # # # # # # # # # # #  EJERCICIO 10 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

# Resultado
paises_capitales = {
    'España': 'Madrid',
    'Francia': 'París',
    'Italia': 'Roma',
    'Alemania': 'Berlín'
}
# nuevo diccionario, capitales_paises contendrá:

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

{
    'Madrid': 'España',
    'París': 'Francia',
    'Roma': 'Italia',
    'Berlín': 'Alemania'
}