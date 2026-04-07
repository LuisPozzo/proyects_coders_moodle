# Funciones de validación para entradas de usuario

def validar_str(dato:str)-> str:
    """ 
    Valida que la cadena no esté vacia.
    Si el dato recibido está vacío, solicita al usuario que ingrese
    un valor válido hasta que la entrada sea correcta.

    Args:
        dato (str): Entrada de texto.
    Returns:
        str: Cadena con texto validada, no vacía.
    Example :
        >>> validar_str(" ")
        Error 1: Entrada inválida. Por favor, inténtelo de nuevo.
        >>> validar_str("Luis")
        'Luis'
    """

    while True:
        # Evaluación booleana: cadena vacía es False, con contenido es True. 
        if dato:
            return dato
        print ('Error 1: Entrada inválida. Por favor, inténtelo de nuevo.')
        dato = input("Ingrese un nombre válido: ").strip().title()

def validar_numero(texto:str, tipo:type) ->int | float:
    """ 
    Valida que dato ingresado sea numerico y positivo. 

    Si el dato ingresado es negativo o es un texto,solicita al usuario que ingrese
    un valor válido hasta que la entrada sea correcta.

    Args:
        texto (str): Mensaje a mostrar al pedir entrada de dato al usuario.
        tipo (type): Tipo al que se convierte la entrada. Se pasa como callable: int para enteros, float para decimales. 
    Returns:
        int | float: Valor numérico positivo convertido según el tipo indicado.
    Example:
        >>> validar_numero ("Precio", float)
        Ingrese el precio: Hola
        Error 1: Entrada inválida. Por favor, inténtelo de nuevo.
        Ingrese el precio: 200.50
        200.5

        >>> validar_numero ("Precio", float)
        Ingrese tu edad:20
        20
        """

    while True:
        try:
            # Solicita el dato y lo convierte al tipo indicado (int o float)
            numero = tipo (input(f"Ingrese el {texto}: "))
            # Valida que el número sea positivo
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
        precio = validar_numero("precio",float)
        print('')
        cantidad = validar_numero( "cantidad",int)

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

