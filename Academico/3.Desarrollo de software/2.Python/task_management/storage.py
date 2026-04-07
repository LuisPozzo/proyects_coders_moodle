import json
from data import tasks
from pathlib import Path

# Get the absolute path of the current file / Obtener la ruta absoluta del archivo actual (storage.py)
ruta = Path(__file__).resolve().parent
file_path = ruta / "task.json"

def save_data():
    """
    Save the data to a JSON file in the same folder./
    Guarda los datos en un archivo JSON en la misma carpeta.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

def load_data():
    """
    Load the data from a JSON file if one exists /
    Carga los datos desde un archivo JSON si existe.
    """
    try:
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

                if isinstance (data,list):
                    tasks.clear()
                    tasks.extend(data)
                else:
                    print("Invalid data format. Starting empty list.")
        else:
            print("No previous data found.")

    except FileNotFoundError:
        # If the file doesn't exist, it's no big deal / Si no existe el archivo, no pasa nada
        pass
