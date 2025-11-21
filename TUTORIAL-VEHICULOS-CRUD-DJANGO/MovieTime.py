import csv
import os


FUNCIONES_FILE = "Funciones.csv"
VENTAS_FILE = "Ventas.csv"
LIMITE_BOLETOS = 200
PRECIO_BOLETO = 10000
PELICULAS = ["The walking dead", "Rapido y furioso", "Avengers", "Titanic", "El senor de los anillos"]
ID_NOMBRE_PELICULAS = {1: "The walking dead", 2: "Rapido y furioso", 3: "Avengers", 4: "Titanic", 5: "El senor de los anillos"}


def catalogo_peliculas():
    print("\nCATÁLOGO DE PELICULAS:")
    print("-" * 50)
    for i, pelicula in enumerate(PELICULAS, start=1):
        print(f"{i}. {pelicula}")
    print("-" * 50)

def cargar_datos(archivo):
    if not os.path.exists(archivo):
        return []
    with open(archivo, "r", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
    
def guardar_datos(archivo, datos, campos):
    with open(archivo, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(datos)

def registrar_funcion():
    funciones = cargar_datos(FUNCIONES_FILE)
    if not funciones:
        funciones = []

    catalogo_peliculas()
    try:
        opcion = int(input("Seleccione el número de la pelicula: "))
        if opcion < 1 or opcion > len(PELICULAS):
            print("Opción inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    pelicula = ID_NOMBRE_PELICULAS[opcion]
    hora = input("Ingrese la hora (M:T:N): ")
    nombre = f"{pelicula} - {hora}"

    # Validar si ya existe una función con ese nombre y hora
    for f in funciones:
        if f["nombre"].lower() == nombre.lower() and f["hora"] == hora:
            print("Esa función ya está registrada.")
            return

    nueva = {
        "nombre": nombre,
        "hora": hora,
        "precio": PRECIO_BOLETO,
        "boletos_vendidos": 0
    }
    funciones.append(nueva)
    guardar_datos(FUNCIONES_FILE, funciones, ["nombre", "hora", "precio", "boletos_vendidos"])
    print("Función registrada exitosamente.")


def listar_funciones():
    funciones = cargar_datos(FUNCIONES_FILE)
    if not funciones:
        print("No hay funciones disponibles.")
        return

    print("\nFUNCIONES DISPONIBLES:")
    print("-" * 50)
    for i, f in enumerate(funciones, start=1):
        print(f"{i}. {f['nombre']} - {f['hora']} | Boletos vendidos: {f['boletos_vendidos']}")
    print("-" * 50)


def gestionar_venta():
    funciones = cargar_datos(FUNCIONES_FILE)
    if not funciones:
        print("No hay funciones disponibles.")
        return

    listar_funciones()
    try:
        opcion = int(input("Seleccione el número de la función: "))
        if opcion < 1 or opcion > len(funciones):
            print("Opción inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    funcion = funciones[opcion - 1]
    cantidad = int(input("Ingrese la cantidad de boletos a vender: "))
    total = str(int(cantidad) * PRECIO_BOLETO)

    # Validar si hay suficientes boletos disponibles
    if int(funcion["boletos_vendidos"]) + cantidad > LIMITE_BOLETOS:
        print("No hay suficientes boletos disponibles.")
        return

    # Actualizar ventas
    ventas = cargar_datos(VENTAS_FILE)
    if not ventas:
        ventas = []
    venta = {
        "pelicula": funcion["nombre"],
        "hora": funcion["hora"],
        "cantidad": cantidad,
        "total": total
    }
    ventas.append(venta)
    guardar_datos(VENTAS_FILE, ventas, ["pelicula", "hora", "cantidad", "total"])

    # Actualizar boletos vendidos
    funcion["boletos_vendidos"] = int(funcion["boletos_vendidos"]) + cantidad
    guardar_datos(FUNCIONES_FILE, funciones, ["nombre", "hora", "precio", "boletos_vendidos"])

    print("Venta realizada exitosamente.")


def resumen_ventas():
    ventas = cargar_datos(VENTAS_FILE)
    if not ventas:
        print("No hay ventas registradas.")
        return

    print("\nRESUMEN DE VENTAS DEL DÍA:")
    print("-" * 50)
    total_dia = 0
    for v in ventas:
        print(f"{v['pelicula']} - {v['hora']} | {v['cantidad']} boletos | Total: ${v['total']}")
        total_dia += int(v["total"])
    print("-" * 50)
    print(f"TOTAL DEL DÍA: ${total_dia}")

# Funciones disponibles 
def funciones_disponibles():
    funciones = cargar_datos(FUNCIONES_FILE)
    if not funciones:
        print("No hay funciones disponibles.")
        return

    print("\nFUNCIONES DISPONIBLES:")
    print("-" * 50)
    for i, f in enumerate(funciones, start=1):
        print(f"{i}. {f['nombre']} - {f['hora']} | Boletos vendidos: {f['boletos_vendidos']}")
    print("-" * 50)


def menu():
    while True:
        print("\nSISTEMA DE GESTIÓN DE CINE - MovieTime")
        print("1. Registrar función")
        print("2. Listar funciones disponibles")
        print("3. Vender boletos")
        print("4. Mostrar resumen de ventas")
        print("5. Catalogo de peliculas")
        print("6. salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_funcion()
        elif opcion == "2":
            listar_funciones()
        elif opcion == "3":
            gestionar_venta()
        elif opcion == "4":
            resumen_ventas()
        elif opcion == "5":
            catalogo_peliculas()
        elif opcion == "6":
            print("Gracias por usar MovieTime. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()
    print("\nGracias por usar MovieTime. ¡Hasta pronto!")