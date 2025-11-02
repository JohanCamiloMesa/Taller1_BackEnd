"""
================================================================================
PARTE 2: EJERCICIOS PRÁCTICOS ADICIONALES
================================================================================
Este archivo contiene 4 ejercicios prácticos de análisis de datos:

1. La Aerolínea Más Puntual - Análisis de retrasos de vuelos
2. Validador y Formateador de URLs - Validación y formateo de URLs
3. Cambio de la Máquina Expendedora - Algoritmo greedy para cambio de monedas
4. Análisis Demográfico de Universidades - Análisis con DataFrames de pandas

Autor: [Tu nombre]
Fecha: Noviembre 2025
================================================================================
"""

import pandas as pd

print(f"La clase de este archivo es {__name__}")


# ============================================================================
# DEFINICIÓN DE FUNCIONES
# ============================================================================

# ----------------------------------------------------------------------------
# EJERCICIO 1: La Aerolínea Más Puntual
# ----------------------------------------------------------------------------

def aerolinea_mas_puntual(vuelos):
    """
    Determina la aerolínea con el menor retraso promedio.
    
    Parámetros:
    vuelos (dict): Diccionario de diccionarios donde la clave es el código del vuelo
                y el valor es otro diccionario con los detalles del vuelo:
                - aerolinea: nombre de la aerolínea
                - origen: aeropuerto de origen
                - destino: aeropuerto de destino
                - distancia: distancia en millas
                - retraso: retraso en minutos
                - duracion: duración del vuelo en minutos
                - salida: hora de salida
    
    Retorna:
    str: Nombre de la aerolínea con el menor retraso promedio
    """
    # Diccionario para almacenar los retrasos de cada aerolínea
    retrasos_por_aerolinea = {}
    
    # Recorrer todos los vuelos
    for codigo_vuelo, datos_vuelo in vuelos.items():
        aerolinea = datos_vuelo["aerolinea"]
        retraso = datos_vuelo["retraso"]
        
        # Si la aerolínea no está en el diccionario, agregarla con una lista vacía
        if aerolinea not in retrasos_por_aerolinea:
            retrasos_por_aerolinea[aerolinea] = []
        
        # Agregar el retraso a la lista de retrasos de la aerolínea
        retrasos_por_aerolinea[aerolinea].append(retraso)
    
    # Calcular el retraso promedio de cada aerolínea
    promedios_retraso = {}
    for aerolinea, retrasos in retrasos_por_aerolinea.items():
        promedio = sum(retrasos) / len(retrasos)
        promedios_retraso[aerolinea] = promedio
    
    # Encontrar la aerolínea con el menor retraso promedio
    aerolinea_puntual = min(promedios_retraso, key=promedios_retraso.get)
    
    return aerolinea_puntual


# ----------------------------------------------------------------------------
# EJERCICIO 2: Validador y Formateador de URLs
# ----------------------------------------------------------------------------

def validar_y_formatear_url(url):
    """
    Valida y formatea una URL según reglas específicas.
    
    Reglas de validación:
    1. La URL debe comenzar con "http://" o "https://"
    2. Debe contener una extensión de dominio válida: .com, .org, .net, .edu
    3. Si no cumple, devuelve "URL no válida"
    
    Reglas de formateo:
    1. Eliminar "www." si está presente
    2. Convertir todo a minúsculas
    3. Asegurar que use "https://"
    4. Eliminar la barra final ("/") si existe
    
    Parámetros:
    url (str): La URL a validar y formatear
    
    Retorna:
    str: URL formateada o "URL no válida"
    """
    # Convertir a minúsculas para facilitar la validación
    url_lower = url.lower()
    
    # Validación 1: Verificar que comience con http:// o https://
    if not (url_lower.startswith("http://") or url_lower.startswith("https://")):
        return "URL no válida"
    
    # Validación 2: Verificar que contenga una extensión válida
    extensiones_validas = [".com", ".org", ".net", ".edu"]
    tiene_extension_valida = False
    
    for extension in extensiones_validas:
        if extension in url_lower:
            tiene_extension_valida = True
            break
    
    if not tiene_extension_valida:
        return "URL no válida"
    
    # Si pasa las validaciones, proceder con el formateo
    url_formateada = url_lower
    
    # Formateo 1: Asegurar que use https://
    if url_formateada.startswith("http://"):
        url_formateada = url_formateada.replace("http://", "https://", 1)
    
    # Formateo 2: Eliminar "www." si está presente
    url_formateada = url_formateada.replace("https://www.", "https://")
    
    # Formateo 3: Eliminar la barra final "/" si existe
    if url_formateada.endswith("/"):
        url_formateada = url_formateada[:-1]
    
    return url_formateada


# ----------------------------------------------------------------------------
# EJERCICIO 3: Cambio de la Máquina Expendedora
# ----------------------------------------------------------------------------

def calcular_cambio(cantidad):
    """
    Calcula el cambio a retornar usando la menor cantidad de monedas posible.
    
    La máquina cuenta con monedas de 500, 200, 100 y 50 pesos.
    
    Parámetros:
    cantidad (int): Cantidad de dinero en pesos a dar como cambio
    
    Retorna:
    str: String en formato "A,B,C,D" donde A, B, C y D son la cantidad de monedas
        de 500, 200, 100 y 50 pesos respectivamente
    """
    # Denominaciones disponibles en orden descendente
    monedas_500 = 0
    monedas_200 = 0
    monedas_100 = 0
    monedas_50 = 0
    
    # Calcular monedas de 500
    monedas_500 = cantidad // 500
    cantidad = cantidad % 500
    
    # Calcular monedas de 200
    monedas_200 = cantidad // 200
    cantidad = cantidad % 200
    
    # Calcular monedas de 100
    monedas_100 = cantidad // 100
    cantidad = cantidad % 100
    
    # Calcular monedas de 50
    monedas_50 = cantidad // 50
    cantidad = cantidad % 50
    
    # Retornar en el formato especificado: "A,B,C,D" (sin espacios)
    return f"{monedas_500},{monedas_200},{monedas_100},{monedas_50}"


# ----------------------------------------------------------------------------
# EJERCICIO 4: Análisis Demográfico de Universidades
# ----------------------------------------------------------------------------

def calcular_habitantes_por_puesto(poblacion, universidades):
    """
    Calcula la proporción de habitantes por cada estudiante universitario en países
    con instituciones clasificadas en el ranking TIMES.
    
    Parámetros:
    poblacion (DataFrame): DataFrame con columnas 'Pais' y 'Poblacion'
    universidades (DataFrame): DataFrame con columnas 'country' y 'num_students'
    
    Retorna:
    DataFrame: DataFrame con columnas 'Pais' y 'habitantes_por_puesto', ordenado de forma ascendente por 'habitantes_por_puesto'
    """
    # Crear listas para almacenar los resultados
    paises = []
    habitantes_por_puesto_lista = []
    
    # Iterar sobre cada país en el DataFrame de población
    for idx, row in poblacion.iterrows():
        pais = row['Pais']
        poblacion_pais = row['Poblacion']
        
        # Buscar el número de estudiantes correspondiente
        # Asumiendo que los índices están alineados (mismo orden en ambos DataFrames)
        num_estudiantes = universidades.iloc[idx]['num_students']
        
        # Calcular habitantes por puesto
        hab_por_puesto = round(poblacion_pais / num_estudiantes, 1)
        
        # Agregar a las listas
        paises.append(pais)
        habitantes_por_puesto_lista.append(hab_por_puesto)
    
    # Crear DataFrame con los resultados
    resultado = pd.DataFrame({
        'Pais': paises,
        'habitantes_por_puesto': habitantes_por_puesto_lista
    })
    
    # Ordenar de forma ascendente por habitantes_por_puesto
    resultado = resultado.sort_values('habitantes_por_puesto', ascending=True)
    
    # Resetear el índice
    resultado = resultado.reset_index(drop=True)
    
    return resultado


# ----------------------------------------------------------------------------
# EJERCICIO 5: Conteo de Vecinos en una Matriz
# ----------------------------------------------------------------------------

def contar_vecinos_cero(matriz, fila, columna):
    """
    Cuenta cuántos vecinos de una casilla tienen valor cero (0).
    
    Se consideran vecinos todas las celdas adyacentes en las 8 direcciones posibles:
    - Arriba, abajo, izquierda, derecha (4 direcciones cardinales)
    - Las 4 diagonales
    
    Una celda en un borde o esquina tendrá menos de 8 vecinos.
    
    Parámetros:
    matriz (list): Matriz de números enteros (lista de listas)
    fila (int): Índice de la fila de la casilla (0-indexed)
    columna (int): Índice de la columna de la casilla (0-indexed)
    
    Retorna:
    int: Cantidad de vecinos con valor cero
    """
    # Obtener dimensiones de la matriz
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    
    # Contador de vecinos con valor cero
    contador = 0
    
    # Definir las 8 direcciones posibles (fila, columna)
    # Arriba, abajo, izquierda, derecha, y las 4 diagonales
    direcciones = [
        (-1, -1),  # Diagonal superior izquierda
        (-1,  0),  # Arriba
        (-1,  1),  # Diagonal superior derecha
        ( 0, -1),  # Izquierda
        ( 0,  1),  # Derecha
        ( 1, -1),  # Diagonal inferior izquierda
        ( 1,  0),  # Abajo
        ( 1,  1)   # Diagonal inferior derecha
    ]
    
    # Revisar cada dirección
    for dir_fila, dir_col in direcciones:
        nueva_fila = fila + dir_fila
        nueva_columna = columna + dir_col
        
        # Verificar que la posición esté dentro de los límites de la matriz
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            # Si el vecino tiene valor 0, incrementar el contador
            if matriz[nueva_fila][nueva_columna] == 0:
                contador += 1
    
    return contador


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print(" PARTE 2 - EJERCICIOS PRÁCTICOS ADICIONALES ".center(80))
    print("="*80 + "\n")
    
    # ========================================================================
    # EJERCICIO 1: La Aerolínea Más Puntual
    # ========================================================================
    
    print("=== Ejercicio 1: La Aerolínea Más Puntual ===\n")
    
    # Datos de vuelos
    vuelos = {
        "AA101": {"aerolinea": "American Airlines", "origen": "JFK", "destino": "LAX", "distancia": 3983, "retraso": 15, "duracion": 360, "salida": "08:00"},
        "AA102": {"aerolinea": "American Airlines", "origen": "LAX", "destino": "ORD", "distancia": 2800, "retraso": 25, "duracion": 270, "salida": "09:45"},
        "DL201": {"aerolinea": "Delta Airlines", "origen": "ATL", "destino": "ORD", "distancia": 950, "retraso": 5, "duracion": 120, "salida": "09:30"},
        "DL202": {"aerolinea": "Delta Airlines", "origen": "ORD", "destino": "ATL", "distancia": 950, "retraso": 0, "duracion": 125, "salida": "13:20"},
        "UA301": {"aerolinea": "United Airlines", "origen": "SFO", "destino": "DEN", "distancia": 1550, "retraso": 10, "duracion": 180, "salida": "11:00"},
        "UA302": {"aerolinea": "United Airlines", "origen": "DEN", "destino": "SFO", "distancia": 1550, "retraso": 20, "duracion": 175, "salida": "15:00"},
        "SW401": {"aerolinea": "Southwest Airlines", "origen": "LAX", "destino": "LAS", "distancia": 380, "retraso": 0, "duracion": 60, "salida": "07:45"},
        "SW402": {"aerolinea": "Southwest Airlines", "origen": "LAS", "destino": "LAX", "distancia": 380, "retraso": 5, "duracion": 55, "salida": "10:30"},
        "JB501": {"aerolinea": "JetBlue", "origen": "BOS", "destino": "MCO", "distancia": 1790, "retraso": 12, "duracion": 200, "salida": "06:40"},
        "JB502": {"aerolinea": "JetBlue", "origen": "MCO", "destino": "BOS", "distancia": 1790, "retraso": 30, "duracion": 190, "salida": "13:10"}
    }
    
    print("Datos de vuelos registrados:")
    print(f"Total de vuelos: {len(vuelos)}\n")
    
    # Mostrar información de cada vuelo
    for codigo, datos in vuelos.items():
        print(f"Vuelo {codigo}:")
        print(f"  Aerolínea: {datos['aerolinea']}")
        print(f"  Ruta: {datos['origen']} → {datos['destino']}")
        print(f"  Retraso: {datos['retraso']} minutos")
        print()
    
    # Calcular retrasos promedio por aerolínea para mostrar
    retrasos_por_aerolinea = {}
    for codigo_vuelo, datos_vuelo in vuelos.items():
        aerolinea = datos_vuelo["aerolinea"]
        retraso = datos_vuelo["retraso"]
        
        if aerolinea not in retrasos_por_aerolinea:
            retrasos_por_aerolinea[aerolinea] = []
        
        retrasos_por_aerolinea[aerolinea].append(retraso)
    
    print("Análisis de retrasos por aerolínea:")
    print("-" * 60)
    for aerolinea, retrasos in retrasos_por_aerolinea.items():
        promedio = sum(retrasos) / len(retrasos)
        print(f"{aerolinea}:")
        print(f"  Número de vuelos: {len(retrasos)}")
        print(f"  Retrasos: {retrasos}")
        print(f"  Retraso promedio: {promedio:.2f} minutos")
        print()
    
    # Llamar a la función para obtener la aerolínea más puntual
    print("="*60)
    aerolinea_puntual = aerolinea_mas_puntual(vuelos)
    print(f"🏆 La aerolínea más puntual es: {aerolinea_puntual}")
    print("="*60)
    print("\n")
    
    # ========================================================================
    # EJERCICIO 2: Validador y Formateador de URLs
    # ========================================================================
    
    print("=== Ejercicio 2: Validador y Formateador de URLs ===\n")
    
    # Lista de URLs de prueba
    urls_prueba = [
        "HTTP://WWW.GOOGLE.COM/",
        "https://www.example.org",
        "http://marketing.net/campaigns/",
        "www.invalid.com",
        "https://university.edu/",
        "http://site.info",
        "https://WWW.AMAZON.COM",
        "ftp://files.com",
        "http://www.github.com/user/repo/",
        "https://learning.edu"
    ]
    
    print("Procesando URLs:\n")
    print("-" * 80)
    
    for i, url in enumerate(urls_prueba, 1):
        resultado = validar_y_formatear_url(url)
        print(f"URL {i}:")
        print(f"  Original:   {url}")
        print(f"  Resultado:  {resultado}")
        
        # Mostrar si es válida o no
        if resultado == "URL no válida":
            print(f"  Estado:     ❌ No válida")
        else:
            print(f"  Estado:     ✅ Válida y formateada")
        print()
    
    # Resumen de validaciones
    print("-" * 80)
    urls_validas = [url for url in urls_prueba if validar_y_formatear_url(url) != "URL no válida"]
    urls_invalidas = [url for url in urls_prueba if validar_y_formatear_url(url) == "URL no válida"]
    
    print(f"\nResumen:")
    print(f"  Total de URLs procesadas: {len(urls_prueba)}")
    print(f"  URLs válidas: {len(urls_validas)}")
    print(f"  URLs inválidas: {len(urls_invalidas)}")
    
    print("\nReglas aplicadas:")
    print("  ✓ Validación: http:// o https:// requerido")
    print("  ✓ Validación: Extensión .com, .org, .net o .edu requerida")
    print("  ✓ Formateo: Conversión a minúsculas")
    print("  ✓ Formateo: Cambio a https://")
    print("  ✓ Formateo: Eliminación de 'www.'")
    print("  ✓ Formateo: Eliminación de barra final '/'")
    print("\n")
    
    # ========================================================================
    # EJERCICIO 3: Cambio de la Máquina Expendedora
    # ========================================================================
    
    print("=== Ejercicio 3: Cambio de la Máquina Expendedora ===\n")
    
    # Casos de prueba
    cantidades_prueba = [1850, 500, 950, 1500, 750, 350, 100, 50, 2000, 1250]
    
    print("Cálculo de cambio con menor cantidad de monedas:")
    print("Denominaciones disponibles: 500, 200, 100, 50 pesos\n")
    print("-" * 80)
    
    for cantidad in cantidades_prueba:
        resultado = calcular_cambio(cantidad)
        monedas = resultado.split(',')
        
        print(f"Cantidad a cambiar: ${cantidad}")
        print(f"  Resultado: {resultado}")
        print(f"  Desglose:")
        print(f"    • {monedas[0]} moneda(s) de $500")
        print(f"    • {monedas[1]} moneda(s) de $200")
        print(f"    • {monedas[2]} moneda(s) de $100")
        print(f"    • {monedas[3]} moneda(s) de $50")
        
        # Verificar total
        total_monedas = int(monedas[0]) + int(monedas[1]) + int(monedas[2]) + int(monedas[3])
        total_valor = (int(monedas[0]) * 500 + int(monedas[1]) * 200 + 
                      int(monedas[2]) * 100 + int(monedas[3]) * 50)
        print(f"  Total de monedas: {total_monedas}")
        print(f"  Verificación: ${total_valor}")
        print()
    
    print("-" * 80)
    print("\n💡 La función retorna el formato: 'A,B,C,D' (sin espacios)")
    print("   donde A=monedas de 500, B=monedas de 200, C=monedas de 100, D=monedas de 50")
    print("\n")
    
    # ========================================================================
    # EJERCICIO 4: Análisis Demográfico de Universidades
    # ========================================================================
    
    print("=== Ejercicio 4: Análisis Demográfico de Universidades ===\n")
    
    # Crear DataFrame de población
    poblacion = pd.DataFrame({
        "Pais": ["Estados Unidos", "Reino Unido", "Canadá", "Australia", "Alemania", 
                "Japón", "Francia", "España", "Italia", "Brasil"],
        "Poblacion": [331000000, 68000000, 38000000, 25600000, 83000000, 
                    125800000, 67000000, 47000000, 60000000, 213000000]
    })
    
    # Crear DataFrame de universidades
    universidades = pd.DataFrame({
        "country": ["United States", "United Kingdom", "Canada", "Australia", "Germany", 
                    "Japan", "France", "Spain", "Italy", "Brazil"],
        "num_students": [2000000, 500000, 300000, 250000, 600000, 
                        800000, 550000, 400000, 450000, 700000]
    })
    
    print("Datos de entrada:\n")
    
    print("DataFrame de Población:")
    print(poblacion.to_string(index=False))
    print()
    
    print("DataFrame de Universidades:")
    print(universidades.to_string(index=False))
    print()
    
    # Llamar a la función
    resultado = calcular_habitantes_por_puesto(poblacion, universidades)
    
    print("-" * 80)
    print("\nResultado: Habitantes por Puesto Universitario")
    print("(Ordenado de forma ascendente)\n")
    print(resultado.to_string(index=False))
    print()
    
    # Análisis detallado
    print("-" * 80)
    print("\nAnálisis detallado:\n")
    
    for idx, row in resultado.iterrows():
        pais = row['Pais']
        hab_por_puesto = row['habitantes_por_puesto']
        
        # Obtener datos originales
        pob = poblacion[poblacion['Pais'] == pais]['Poblacion'].values[0]
        
        print(f"{idx + 1}. {pais}:")
        print(f"   • Población: {pob:,} habitantes")
        print(f"   • Habitantes por puesto: {hab_por_puesto}")
        print(f"   • Interpretación: Hay {hab_por_puesto} habitantes por cada estudiante universitario")
        print()
    
    # Conclusión
    mejor_pais = resultado.iloc[0]['Pais']
    mejor_ratio = resultado.iloc[0]['habitantes_por_puesto']
    
    print("="*80)
    print(f"📊 Conclusión:")
    print(f"   {mejor_pais} tiene la mejor proporción de acceso a educación universitaria")
    print(f"   con {mejor_ratio} habitantes por puesto universitario.")
    print("="*80)
    print("\n")
    
    # ========================================================================
    # EJERCICIO 5: Conteo de Vecinos en una Matriz
    # ========================================================================
    
    print("=== Ejercicio 5: Conteo de Vecinos en una Matriz ===\n")
    
    # Crear matriz de prueba
    matriz = [
        [0, 1, 0, 2, 0],
        [2, 0, 1, 0, 3],
        [1, 2, 0, 1, 0],
        [0, 0, 3, 0, 2],
        [2, 1, 0, 0, 1]
    ]
    
    print("Matriz de prueba:")
    print("-" * 40)
    for i, fila in enumerate(matriz):
        print(f"Fila {i}: {fila}")
    print("-" * 40)
    print()
    
    # Función auxiliar para visualizar la matriz con una casilla marcada
    def visualizar_matriz_con_marca(matriz, fila_marca, col_marca):
        print(f"Casilla marcada: [{fila_marca}, {col_marca}] = {matriz[fila_marca][col_marca]}")
        print()
        for i, fila in enumerate(matriz):
            fila_str = ""
            for j, valor in enumerate(fila):
                if i == fila_marca and j == col_marca:
                    fila_str += f"[{valor}] "
                else:
                    fila_str += f" {valor}  "
            print(fila_str)
        print()
    
    # Casos de prueba
    casos_prueba = [
        (0, 0),  # Esquina superior izquierda
        (0, 2),  # Borde superior
        (2, 2),  # Centro de la matriz
        (4, 4),  # Esquina inferior derecha
        (1, 1),  # Posición con varios ceros alrededor
        (3, 1),  # Otra posición
        (2, 0),  # Borde izquierdo
        (4, 2),  # Borde inferior
    ]
    
    print("Análisis de vecinos con valor cero:\n")
    print("="*80)
    
    for idx, (fila, col) in enumerate(casos_prueba, 1):
        print(f"\nCaso {idx}: Casilla [{fila}, {col}]")
        print("-" * 80)
        
        visualizar_matriz_con_marca(matriz, fila, col)
        
        # Contar vecinos con valor cero
        resultado = contar_vecinos_cero(matriz, fila, col)
        
        # Determinar tipo de posición
        filas_total = len(matriz)
        cols_total = len(matriz[0])
        
        if (fila == 0 or fila == filas_total - 1) and (col == 0 or col == cols_total - 1):
            tipo_posicion = "Esquina (3 vecinos posibles)"
        elif fila == 0 or fila == filas_total - 1 or col == 0 or col == cols_total - 1:
            tipo_posicion = "Borde (5 vecinos posibles)"
        else:
            tipo_posicion = "Centro (8 vecinos posibles)"
        
        print(f"Tipo de posición: {tipo_posicion}")
        print(f"Valor de la casilla: {matriz[fila][col]}")
        print(f"Vecinos con valor cero: {resultado}")
        print()
    
    # Resumen final
    print("="*80)
    print("\n📊 Resumen del Ejercicio 5:")
    print("   • La función considera las 8 direcciones posibles (arriba, abajo, izq, der, y diagonales)")
    print("   • Las casillas en esquinas tienen máximo 3 vecinos")
    print("   • Las casillas en bordes tienen máximo 5 vecinos")
    print("   • Las casillas en el centro tienen 8 vecinos")
    print("   • Solo se cuentan los vecinos con valor 0")
    print("="*80)
    
    # ========================================================================
    # FIN DEL PROGRAMA
    # ========================================================================
    print("\n" + "="*80)
    print(" FIN DE LA PARTE 2 - TODOS LOS EJERCICIOS COMPLETADOS ".center(80))
    print("="*80)
