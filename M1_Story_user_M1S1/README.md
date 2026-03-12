# Historia de Usuario: M1S1 - Fundamentos y Operaciones Básicas de Inventario

## 🎯 Objetivo
Desarrollar un programa simple para el **registro de productos** que permita calcular unidades y costos, aplicando fundamentos de programación como gestión de variables, tipos de datos, operaciones matemáticas y salida por consola.

---

## 📝 Descripción de Tareas

### **TASK 1: Diseño del Flujo**
- **Actividad:** Diseñar un diagrama de flujo que represente el proceso de registro.
- **Flujo:** `Inicio` → `Leer nombre, precio y cantidad` → `Calcular costo total` → `Mostrar resultado` → `Fin`.
- **Entregable:** Imagen o PDF exportado desde **draw.io**.

### **TASK 2: Entrada de Datos (Variables)**
- **Archivo:** `inventario.py`
- **Requerimientos:**
  - Declarar variables: `nombre` (string), `precio` (float) y `cantidad` (int).
  - Implementar captura de datos con `input()`.
  - **Validación:** Si el usuario ingresa un valor inválido, el sistema debe mostrar un error y solicitar el dato nuevamente (bucle de validación).

### **TASK 3: Operación Matemática**
- **Cálculo:** Crear la variable `costo_total`.
- **Fórmula:** `precio * cantidad`.
- **Condición:** La operación solo debe ejecutarse tras validar correctamente las entradas.

### **TASK 4: Interfaz de Consola**
- **Salida:** Mostrar los datos procesados mediante `print()`.
- **Formato esperado:**  
  `Producto: [Nombre] | Precio: [Valor] | Cantidad: [Valor] | Total: [Valor]`

### **TASK 5: Documentación de Código**
- **Comentarios:** Usar `#` para explicar cada bloque de código.
- **Resumen:** Incluir un comentario general al final del archivo describiendo la funcionalidad global del script.

---

## ✅ Criterios de Aceptación

1.  **Integridad:** Solicitar obligatoriamente nombre, precio y cantidad.
2.  **Robustez:** Gestionar errores en la entrada de datos numéricos mediante re-solicitud.
3.  **Precisión:** El cálculo del costo total debe ser aritméticamente correcto.
4.  **Legibilidad:** Código estructurado, debidamente comentado y sin errores de sintaxis.
5.  **Coherencia:** El diagrama de flujo debe coincidir exactamente con la lógica del código (Entrada → Proceso → Salida).
