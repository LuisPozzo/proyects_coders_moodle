# Funciones de validación para entradas de usuario

def validar_str(dato):
    #Validar que la cadena no esté vacía
    while True:
        #Se utiliza 'if dato' como logica boolelana para verificar si la cadena no está vacía. 
        # Si 'dato' es una cadena vacía, se evalúa como False, y el programa entra en el bloque else, mostrando un mensaje de error y solicitando al usuario que ingrese un nombre válido. Si dato contiene algún valor (es decir, no está vacía), se evalúa como True, y el programa retorna ese valor, permitiendo que el flujo continúe normalmente.
        if dato:
            return dato
        print ('Error 1: Entrada inválida. Por favor, inténtelo de nuevo.')
        dato = input("Ingrese un nombre válido: ").strip().title()

def validar_numerico(texto,tipo):
    while True:
        try:
            #Se solicita numero y se realiza la conversion, en caso de presentar error, saltará a la linea 25
            
            numero = tipo (input(f"Ingrese el {texto}: "))
            #Se valida que el numero sea positivo, si es negativo se muestra un mensaje de error y se solicita nuevamente el ingreso del número. Si el número es positivo, se retorna el valor, permitiendo que el flujo del programa continúe normalmente.
            if numero < 0:
                print("Error 2: El valor debe ser un número positivo.")
                continue
            return numero
        
        except ValueError:
            print ('Error 1: Entrada inválida. Por favor, inténtelo de nuevo.')
            continue

# PROGRAMA PRINCIPAL -------------------------------------------
# bucle que se ejecuta hasta que el usuario proporciona entradas válidas
while True:
    # TASK 2: declaración de variables que almacenan los datos
    try:
        nombre = validar_str(input("Name: ").strip().title())
        print('')
        precio = validar_numerico("precio",float)
        print('')
        cantidad = validar_numerico( "cantidad",int)

        # TASK 3: cálculo del costo total tras validar las entradas
        costo_total = precio * cantidad

        # TASK 4: salida de consola con formato solicitado
        print(30 * "--")
        print( f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")
        print(30 * "--")

        break

    except Exception as e:  # se utiliza de forma genérica para reintentar
        print(f"Error 3: {e} \nEntrada inválida. Por favor, inténtelo de nuevo. ")
        continue

# --------------------------------------------------------------
# Este script solicita el nombre, precio y cantidad de un producto,
# valida cada dato en bucles de repetición según la historia de usuario, 
# calcula el costo total y muestra en pantalla una línea.

