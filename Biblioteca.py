import os
import time
import csv
import json
from FuncionesJSON import *
os.system("cls")

listalibros = []
libro = []

while True:
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

    os.system("cls")
    if opc == 1:
        agregar_libro()
        
    
    elif opc == 2:
            mostrar_libros()
                    
    
    elif opc == 3:
        buscar_libro_especifico()


    elif opc == 4:
        modificar_info_libro()
                

    elif opc == 5:
        importar_a_json()
        
    else:
        print("Muchas gracias por ocupar la app. Vuelva pronto!")
        break


        

