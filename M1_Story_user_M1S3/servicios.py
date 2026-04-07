# Funciones de validación para entradas de usuario

def validar_str(texto:str)-> str:
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
        dato = input(f"{texto} ").strip().title()
        if dato:
            return dato
        print ('Error 1: Entrada inválida. Por favor, inténtelo de nuevo.')
        print("")
    

def validar_numero(texto:str, tipo:type) ->int | float:
    """ 
    Valida que dato ingresado sea numerico y positivo. 
    En caso de que no, solicita al usuario que ingrese
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
             """
    while True:
        try:
            # Solicita el dato y lo convierte al tipo indicado (int o float)
            numero = tipo (input(f"{texto} "))
            # Valida que el número sea positivo
            if numero < 0:
                print("Error 2: El valor debe ser un número positivo.")
                print("")
                continue
            return numero
        
        except ValueError:
            print ('Error 1: Entrada inválida. Por favor, inténtelo de nuevo.')
            print("")
            continue

def agregar_producto(inventario:list):
    """
    Aagrega un producto nuevo y permite que el usuario dese continuar agregando mas productos o regresar al menu.
    Cada producto debe tener:
    - nombre.
    - precio.
    - cantidad.

    Args:
        inventario (list): Lista de productos.
    """

    while True:
        print(f"\n{'='*5} REGISTRO DE PRODUCTO {'='*5}")
        nombre = validar_str("Nombre del producto: ")
        precio = validar_numero("Precio:",float)
        cantidad = validar_numero( "Cantidad:",int)

        producto = {
            "nombre" : nombre,
            "precio" : precio,
            "cantidad": cantidad
        } 
        inventario.append (producto)
        print (f"Producto registrado correctamente.")

        op = validar_numero ("""Seleccione una opción:
    1.Registrar nuevo producto.
    2. Volver al menu.\n>>> """,int)
        if op !=1:
            break
        
def mostrar_inventario(inventario:list):
    """Muestra el listado de los productos.
    Args: 
        inventario : Lista de productos.
    """
    print(f"\n{'='*10} INVENTARIO {'='*10}")

    if not inventario:
        print ("No hay productos en el inventario.")
        print("-"*50)
        return
    
    for idx, producto in enumerate(inventario):
        print (f"{idx+1}. {producto['nombre']} | ${producto['precio']} | Cantidad: {producto['cantidad']}")
    print("-"*50)

def _buscar_producto(inventario:list,nombre:str):
    """
    Busca un producto por nombre y lo retorna.
    Returns:
        dict | None
    """
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def buscar_producto(inventario:list):
    """Busca un prodcuto por su nombre y muestra el resultado.
    Args:
        inventario (list) : Lista de productos.
    """
    print(f"\n{'='*5} BUSQUEDA DE PRODUCTO {'='*5}")
    
    if not inventario:
        print ("No hay productos en el inventario.")
        print("-"*50)
        return
    
    nombre = validar_str("Ingrese el producto a buscar: ")
    producto =_buscar_producto(inventario,nombre)

    if producto:
        print(f"\nProducto encontrado:")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Cantidad: {producto['cantidad']}")
    else:
        print("Producto no encontrado\n")
    
def actualizar_producto(inventario:list):
    """Actualiza precio y cantidad de un producto."""

    print(f"\n{'='*5} ACTUALIZAR PRODUCTO {'='*5}")

    if not inventario:
        print ("No hay productos en el inventario.")
        print("-"*50)
        return
    
    nombre = validar_str("Ingrese el producto a actualizar: ")
    producto = _buscar_producto (inventario,nombre)

    if not producto:
        print("Producto no encontrado.")
        return
    
    nuevo_precio = validar_numero("Nuevo precio:", float)
    nueva_cantidad = validar_numero("Nueva cantidad:", int)

    producto["precio"] = nuevo_precio
    producto["cantidad"] = nueva_cantidad

    print("Producto actualizado correctamente.")

def eliminar_producto(inventario):
    """Elimina un producto del inventario."""

    print(f"\n{'='*5} ELIMINAR PRODUCTO {'='*5}")

    if not inventario:
        print ("No hay productos en el inventario.")
        print("-"*50)
        return
    
    nombre = validar_str("Ingrese producto a eliminar:")
    producto = _buscar_producto(inventario,nombre)

    if producto:
        inventario.remove(producto)
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def calcular_estadisticas(inventario:list):
    """Calcula estadisticas del inventario:
    - Unidades totales.
    - Valor total del inventario.
    - Producto mas caro.
    - Producto de mayor stock."""

    print(f"\n{'='*10} ESTADISTICAS DE INVENTARIO {'='*10}")

    if not inventario:
        print ("No hay productos en el inventario.")
        print("-"*50)
        return
    
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total: ${valor_total:.2f}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f"Mayor stock: {mayor_stock['nombre']} ({mayor_stock['cantidad']})")
    print("-"*50)
    