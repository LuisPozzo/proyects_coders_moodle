from servicios import *
from data import inventarios
from archivos import cargar_datos, guardar_datos,guardar_csv,cargar_csv

# PROGRAMA PRINCIPAL -------------------------------------------
# bucle que se ejecuta hasta que el usuario proporciona entradas válidas
#cargar_datos(inventarios)
cargar_csv(inventarios)
while True:
    # TASK 2: declaración de variables que almacenan los datos
    try:
        print("=== SISTEMA DE GESTION DE INVENTARIO ===")
        print("1. Agregar producto.")
        print("2. Mostrar inventario.")
        print("3. Buscar producto.")
        print("4. Actualizar producto.")
        print("5. Eliminar producto.")
        print("6. Estadisticas.")
        print("7. Salir del programa.")
        option = input("Selecciona una opción: ")

        if option == "1":
            agregar_producto(inventarios)
        elif option == "2":
            mostrar_inventario(inventarios)
        elif option == "3":
            buscar_producto(inventarios)
        elif option == "4":
            actualizar_producto(inventarios)
        elif option == "5":
            eliminar_producto (inventarios)        
        elif option == "6":
            calcular_estadisticas(inventarios)
        elif option == "7":
            print("Hasta Luego!")
            #guardar_datos(inventarios)
            guardar_csv (inventarios)
            
            
            break
        else:
            print("Opción invalida.\n")
        
    except Exception as e:  # se utiliza de forma genérica para reintentar
        print(f"Error 3: {e} \nEntrada inválida. Por favor, inténtelo de nuevo. ")
        option = input("Selecciona una opción: ") 
        continue