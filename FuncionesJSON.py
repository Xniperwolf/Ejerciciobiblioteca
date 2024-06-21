listalibros = []
import os
import time
import json

def menu():
    print("Bienvenido a la biblioteca.")
    print("-----------------------------")
    print("1. Agregar un libro")
    print("2. Mostrar libros disponibles")
    print("3. Buscar libro por título")
    print("4. Actualizar información de libro")
    print("5. Guardar libros en JSON")
    print("6. Salir")

    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if opc in (1,2,3,4,5,6):
                break
            else:
                print("ERROR, ingrese una opción correcta.")
        except:
            print("Ingrese un número entero.")

def agregar_libro():
    print("Agregar libro")
    print("---------------")
    titulolibro = input("Ingrese nombre de libro: ")
    fechapublicacion = int(input("Ingrese año de publicación: "))
    generolibro = input("Ingrese género al que pertenece el libro: ")

    libro = {"Nombre": titulolibro, "Fecha": fechapublicacion, "Genero": generolibro}
    listalibros.append(libro)
    print("Libro añadido con éxito.")
    time.sleep(2)
    os.system("cls")

def mostrar_libros():
    if len(listalibros) == 0:
        print("Lista vacía, ingrese un libro en la opción 1")
    else:
        print("Lista de libros: ")
        for x in listalibros:
            print(f"Nombre: {x['Nombre']}, Fecha: {x['Fecha']}, Género: {x['Genero']}")
            time.sleep(2)
    
def buscar_libro_especifico():
    if len(listalibros) == 0:
        print("No hay libros en la base de datos")
    else:
        titulolibro = input("Ingrese título del libro: ")
        for x in listalibros:
            print(f"Nombre: {x['Nombre']}, Fecha: {x['Fecha']}, Genero: {x['Genero']}")
            break

def modificar_info_libro():
    if len(listalibros) == 0:
            print("No hay libros para modificar información")
    else:
        titulolibro = input("Ingrese título del libro: ")
        for x in listalibros:
            print(f"Modificar libro: {x['Nombre']}, Fecha: {x['Fecha']}, Género: {x['Genero']}")
            nuevo_titulo = input("Ingrese nuevo nombre de libro (deje en blanco para no modificar): ")
            if nuevo_titulo:
                x['Nombre'] = nuevo_titulo
            nueva_fecha = input("Ingrese nuevo año de publicación (deje en blanco para no modificar): ")
            if nueva_fecha:
                x['Fecha'] = int(nueva_fecha)
            nuevo_genero = input("Ingrese nuevo género (deje en blanco para no modificar): ")
            if nuevo_genero:
                x['Genero'] = nuevo_genero
            print("Información del libro actualizada con éxito.")
            break

def importar_a_json():
    if len(listalibros) == 0:
            print("Lista vacía, nada que importar en JSON.")
    else:
        nombrearchivo = input("Ingrese nombre de archivo: ")+"json"
        with open(nombrearchivo,"x",newline="") as archivo:
            json.dump(listalibros,archivo)