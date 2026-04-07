import json
import csv  
from pathlib import Path
from servicios import _buscar_producto, validar_str

def guardar_csv(inventario: list):
    """
    Guarda el inventario en un archivo CSV.
    Usa la librería csv para escribir filas.
    """
    if not inventario:
        print("Inventario vacío")
        return

    ruta = Path(__file__).resolve().parent / "inventario.csv"

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            # Escribir encabezado
            writer.writerow(["nombre", "precio", "cantidad"])

            # Escribir datos
            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print("Guardado correctamente.")

    except Exception as e:
        print("Error al guardar:", e)


def cargar_csv(inventario: list):
    """
    Carga productos desde un archivo CSV.

    - Valida encabezado
    - valida columnas
    - Omite filas inválidas
    - Permite sobrescribir o fusionar
    """
    ruta = Path(__file__).resolve().parent / "inventario.csv"
    nuevos = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)

            if header != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido")
                return

            for fila in reader:
                try:
                    if len(fila) != 3:
                        raise ValueError
                    
                    nombre, precio, cantidad = fila
                    
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        raise ValueError
                    
                    nuevos.append({
                        "nombre": nombre,
                        "precio": float(precio),
                        "cantidad": int(cantidad)
                    })

                except:
                    errores += 1

        op = validar_str("¿Sobrescribir? (Si/No):").lower()

        if op in ["s","si"]:
            inventario.clear()
            inventario.extend(nuevos)
            accion = "Sobrescritura"
        else:
            for n in nuevos:
                existente = _buscar_producto (inventario, n["nombre"])
                if existente:
                    existente["cantidad"] += n["cantidad"]
                    existente["precio"] = n["precio"]
                else:
                    inventario.append(n)
            accion = "Fusión"
        print("Carga completada...")
        print(f"Productos cargados: {len(nuevos)}")
        print(f"Filas inválidas: {errores}")
        print(f"Acción realizada: {accion}")

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print("Error al cargar:", e)
        


# Get the absolute path of the current file / Obtener la ruta absoluta del archivo actual (storage.py)
ruta = Path(__file__).resolve().parent
file_path = ruta / "inventario.json"

def guardar_datos(inventarios:list):
    """
    Guarda los datos en un archivo JSON en la misma carpeta.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(inventarios, file, indent=4)

def cargar_datos(inventarios:list):
    """
    Carga los datos desde un archivo JSON si existe.
    """
    try:
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

                if isinstance (data,list):
                    inventarios.clear()
                    inventarios.extend(data)
                else:
                    print("Invalid data format. Starting empty list.")
        else:
            print("(No hay datos previos encontrados.)\n")

    except FileNotFoundError:
        # If the file doesn't exist, it's no big deal / Si no existe el archivo, no pasa nada
        pass
