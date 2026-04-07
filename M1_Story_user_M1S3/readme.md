# 📦 Sistema de Gestión de Inventario / Inventory Management System

---

## Descripción

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar un inventario de productos utilizando estructuras de datos (listas y diccionarios) y persistencia en archivos CSV.

El sistema implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar), cálculo de estadísticas y almacenamiento/carga de datos desde archivos.

---

## Cómo ejecutar el programa / How to run

1. Asegúrate de tener Python instalado (versión 3.10 o superior).
2. Clona este repositorio o descarga los archivos.
3. Ubícate en la carpeta del proyecto.
4. Ejecuta:

```bash
python app.py
```
---

##  Funcionalidades / Features

### Gestión de inventario
* Agregar productos
* Mostrar inventario
* Buscar productos
* Actualizar productos
* Eliminar productos

### Estadísticas
* Total de unidades
* Valor total del inventario
* Producto más caro
* Producto con mayor stock

### Persistencia
* Guardar inventario en archivo CSV
* Cargar inventario desde CSV
* Validación de datos
* Manejo de errores
* Fusión o sobrescritura de datos
---

## Estructura del proyecto / Project Structure

```bash
📁 proyecto/
│
├── app.py              # Menú principal
├── servicios.py        # Lógica del sistema (CRUD, validaciones)
├── archivos.py         # Manejo de archivos CSV
├── inventario.csv      # Archivo de datos (opcional)
└── README.md           # Documentación
```
---

## Ejemplo de uso / Example of use

```text
=== SISTEMA DE GESTION DE INVENTARIO ===

1. Agregar producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir
```
---

### Ejemplo:

```text
Nombre: Laptop
Precio: 2500
Cantidad: 3

Producto agregado correctamente.
```
---

## Validaciones implementadas / Validations

* No se permiten valores vacíos
* Precio y cantidad deben ser números positivos
* Validación de formato CSV
* Manejo de errores en lectura/escritura de archivos
* Omisión de filas inválidas en CSV
---

## Persistencia CSV
El sistema guarda los datos en formato:

```csv
nombre,precio,cantidad
Laptop,2500,3
Mouse,50,10
```

Al cargar datos:
* Se valida el archivo
* Se omiten filas incorrectas
* Se permite:

  * Sobrescribir inventario
  * Fusionar datos

---
