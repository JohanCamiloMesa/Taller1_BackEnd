# Taller 1 - Backend con Python

## 📋 Descripción

Este repositorio contiene la solución completa del Taller 1, un proyecto educativo que abarca conceptos fundamentales y avanzados de programación en Python, incluyendo manejo de estructuras de datos, funciones, Programación Orientada a Objetos (POO), manejo de errores y análisis de datos con pandas.

## 🗂️ Estructura del Proyecto

```
Talle1_BackEnd/
│
├── Parte1.py          # Sistema de Gestión de Adopción de Mascotas
├── Parte2.py          # Ejercicios Prácticos Adicionales
├── venv/              # Entorno virtual de Python
└── README.md          # Este archivo
```

## 📚 Contenido

### Parte 1: Sistema de Gestión de Adopción de Mascotas

Implementa un sistema completo de adopción de mascotas cubriendo los siguientes módulos:

#### **Ejercicio 1: Perfil de la Mascota (Módulo 1)**
- Variables, listas y diccionarios
- Creación de perfil de mascota
- Actualización de datos

#### **Ejercicio 2: Verificación del Estado de la Mascota (Módulo 3)**
- Funciones y estructuras de control
- Clasificación de mascotas por edad: Cachorro, Adulto, Senior

#### **Ejercicio 3: Sistema de Adopción con POO (Módulo 4)**
- Clase `Mascota`: Representa una mascota con nombre, especie, edad y estado
- Clase `Persona`: Clase base para personas
- Clase `Adoptante`: Hereda de Persona, gestiona adopciones
- Método `adoptar()`: Permite adoptar mascotas disponibles

#### **Ejercicio 4: Manejo de Errores (Módulo 5)**
- Función `asignar_adopcion()`: Adopción segura con try-except
- Validación de disponibilidad de mascotas
- Mensajes de error personalizados

### Parte 2: Ejercicios Prácticos Adicionales

Cinco ejercicios que aplican conceptos avanzados de programación y análisis de datos:

#### **Ejercicio 1: La Aerolínea Más Puntual**
- Análisis de datos de vuelos
- Cálculo de retrasos promedio por aerolínea
- Identificación de la aerolínea más puntual

#### **Ejercicio 2: Validador y Formateador de URLs**
- Validación de formato de URLs
- Reglas de validación: protocolo y extensión de dominio
- Formateo automático: minúsculas, https://, eliminación de www. y /

#### **Ejercicio 3: Cambio de la Máquina Expendedora**
- Algoritmo greedy para calcular cambio
- Denominaciones: 500, 200, 100, 50 pesos
- Retorna formato: "A,B,C,D" (cantidad de cada moneda)

#### **Ejercicio 4: Análisis Demográfico de Universidades**
- Uso de pandas DataFrame
- Cálculo de habitantes por puesto universitario
- Ordenamiento y análisis de datos
- Operaciones de iteración sobre DataFrames

#### **Ejercicio 5: Conteo de Vecinos en una Matriz**
- Recorrido de matriz bidimensional (lista de listas)
- Búsqueda en 8 direcciones (cardinales y diagonales)
- Conteo de vecinos con valor cero
- Validación de límites de matriz

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.13 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio** (si aplica):
```bash
git clone <https://github.com/JohanCamiloMesa/Taller1_BackEnd.git>
cd Talle1_BackEnd
```

2. **Crear entorno virtual**:
```bash
python -m venv venv
```

3. **Activar el entorno virtual**:
- En Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```
- En Windows (CMD):
```cmd
venv\Scripts\activate.bat
```
- En Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instalar dependencias**:
```bash
pip install pandas
```

## 💻 Uso

### Ejecución Individual

Para ejecutar cada parte de forma independiente:

```bash
# Ejecutar Parte 1 (Sistema de Adopción de Mascotas)
python Parte1.py

# Ejecutar Parte 2 (Ejercicios Prácticos Adicionales)
python Parte2.py
```

Cada archivo ejecuta automáticamente todos los ejercicios incluidos y muestra los resultados en la consola.

## 📊 Ejemplos de Salida

### Parte 1: Sistema de Adopción
```
=== Sistema de Adopción de Mascotas con POO ===

Mascotas disponibles:
  • Luna (Perro, 3 años) - Estado: Disponible
  • Michi (Gato, 2 años) - Estado: Disponible

Proceso de adopción:
✓ Carlos Pérez ha adoptado a Luna
✓ Adopción exitosa: Carlos Pérez es ahora el dueño de Luna
```

### Parte 2: Ejercicio 1 - Análisis de Aerolíneas
```
🏆 La aerolínea más puntual es: Delta Airlines
```

### Parte 2: Ejercicio 2 - Validador de URLs
```
URL Original:   HTTP://WWW.GOOGLE.COM/
URL Formateada: https://google.com
Estado:         ✅ Válida y formateada
```

### Parte 2: Ejercicio 3 - Cambio de Máquina Expendedora
```
Cantidad a cambiar: $1850
  Resultado: 3,1,1,1
  Desglose:
    • 3 moneda(s) de $500
    • 1 moneda(s) de $200
    • 1 moneda(s) de $100
    • 1 moneda(s) de $50
```

### Parte 2: Ejercicio 5 - Conteo de Vecinos
```
Análisis de casilla (2, 2):
Valor de la casilla: 0
Vecinos con valor cero: 3
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.13**: Lenguaje de programación principal
- **pandas**: Biblioteca para análisis y manipulación de datos
- **POO**: Programación Orientada a Objetos
- **Manejo de Errores**: try-except para código robusto

## 📝 Conceptos Aprendidos

### Fundamentos de Python
- Variables y tipos de datos
- Listas y diccionarios
- Estructuras de control (if, for)
- Funciones

### Programación Orientada a Objetos
- Clases y objetos
- Herencia
- Métodos especiales (`__init__`, `__str__`)
- Encapsulamiento

### Algoritmos y Estructuras de Datos
- Algoritmo greedy (cambio de monedas)
- Recorrido de matrices
- Búsqueda en múltiples direcciones

### Manejo de Datos
- DataFrames de pandas
- Operaciones de agregación
- Ordenamiento y filtrado
- Análisis estadístico

## 👨‍💻 Autor

Desarrollo del Taller 1 - Backend con Python  
Fecha: Noviembre 2025

## 📄 Licencia

Este proyecto es con fines educativos.

## 🤝 Contribuciones

Este es un proyecto de taller educativo. Si deseas sugerir mejoras:
1. Reporta issues
2. Propón cambios
3. Mejora la documentación

## 📞 Contacto

Para preguntas o comentarios sobre este proyecto, consulta con tu instructor o revisa la documentación del curso.

---

**¡Gracias por revisar este proyecto! 🐾**
