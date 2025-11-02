# ============================================================================
# TALLER 1 - SISTEMA DE GESTIÓN DE ADOPCIÓN DE MASCOTAS
# ============================================================================
# Este archivo contiene 4 ejercicios que cubren diferentes módulos:
# - Módulo 1: Variables, listas y diccionarios
# - Módulo 3: Funciones y estructuras de control
# - Módulo 4: Programación Orientada a Objetos (POO)
# - Módulo 5: Manejo de errores
# ============================================================================

# ----------------------------------------------------------------------------
# EJERCICIO 3: Sistema de Adopción de Mascotas con POO (Módulo 4)
# ----------------------------------------------------------------------------

# 1. Crear la Clase Mascota
class Mascota:
    """Clase que representa una mascota en el sistema de adopción."""
    
    def __init__(self, nombre, especie, edad, adoptado=False):
        """
        Inicializa una mascota.
        
        Parámetros:
        nombre (str): Nombre de la mascota
        especie (str): Especie de la mascota (perro, gato, etc.)
        edad (int): Edad de la mascota en años
        adoptado (bool): Estado de adopción (por defecto False)
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.adoptado = adoptado
    
    def __str__(self):
        """Retorna una representación en string de la mascota."""
        estado = "Adoptado" if self.adoptado else "Disponible"
        return f"{self.nombre} ({self.especie}, {self.edad} años) - Estado: {estado}"


# 2. Crear las Clases Persona y Adoptante
class Persona:
    """Clase base que representa una persona."""
    
    def __init__(self, nombre, edad):
        """
        Inicializa una persona.
        
        Parámetros:
        nombre (str): Nombre de la persona
        edad (int): Edad de la persona
        """
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        """Retorna una representación en string de la persona."""
        return f"{self.nombre} ({self.edad} años)"


class Adoptante(Persona):
    """Clase que representa un adoptante, hereda de Persona."""
    
    def __init__(self, nombre, edad):
        """
        Inicializa un adoptante.
        
        Parámetros:
        nombre (str): Nombre del adoptante
        edad (int): Edad del adoptante
        """
        super().__init__(nombre, edad)
        self.mascotas_adoptadas = []
    
    def adoptar(self, mascota):
        """
        Adopta una mascota si está disponible.
        
        Parámetros:
        mascota (Mascota): La mascota a adoptar
        
        Retorna:
        bool: True si la adopción fue exitosa, False si la mascota ya estaba adoptada
        """
        if not mascota.adoptado:
            mascota.adoptado = True
            self.mascotas_adoptadas.append(mascota)
            print(f"✓ {self.nombre} ha adoptado a {mascota.nombre}")
            return True
        else:
            print(f"✗ {mascota.nombre} ya ha sido adoptado")
            return False
    
    def __str__(self):
        """Retorna una representación en string del adoptante y sus mascotas."""
        info = f"{self.nombre} ({self.edad} años)"
        if self.mascotas_adoptadas:
            info += f" - Mascotas adoptadas: {len(self.mascotas_adoptadas)}"
            for mascota in self.mascotas_adoptadas:
                info += f"\n  • {mascota.nombre} ({mascota.especie})"
        else:
            info += " - Sin mascotas adoptadas"
        return info


# ----------------------------------------------------------------------------
# EJERCICIO 4: Adopción Segura con Manejo de Errores (Módulo 5)
# ----------------------------------------------------------------------------

# 1. Crear una función asignar_adopcion que reciba un adoptante y una mascota
def asignar_adopcion(adoptante, mascota):
    """
    Asigna una adopción de forma segura con manejo de errores.
    
    Parámetros:
    adoptante (Adoptante): El adoptante que desea adoptar
    mascota (Mascota): La mascota a adoptar
    
    Raises:
    Exception: Si la mascota ya está adoptada
    """
    # 2. Utilizar bloque try-except con sentencia if para verificar si la mascota ya está adoptada
    try:
        # 3. Si la mascota ya fue adoptada, lanzar un mensaje de error personalizado
        if mascota.adoptado:
            raise Exception(f"Error: Esta mascota no está disponible. {mascota.nombre} ya ha sido adoptado.")
        
        # Si la mascota está disponible, proceder con la adopción
        adoptante.adoptar(mascota)
        print(f"✓ Adopción exitosa: {adoptante.nombre} es ahora el dueño de {mascota.nombre}")
        
    except Exception as e:
        print(f"✗ {e}")


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

print(f"La clase de este archivo es {__name__}")

if __name__ == "__main__":
    print("\n" + "="*80)
    print(" TALLER 1 - SISTEMA DE GESTIÓN DE ADOPCIÓN DE MASCOTAS ".center(80))
    print("="*80 + "\n")
    
    # ------------------------------------------------------------------------
    # EJERCICIO 1: Perfil de la Mascota (Módulo 1)
    # ------------------------------------------------------------------------
    
    # 1. Crear variables para el nombre de una mascota, su edad y una lista de sus premios favoritos
    nombre_mascota = "Max"
    edad_mascota = 3
    premios_favoritos = ["Hueso de juguete", "Pelota de tenis", "Cuerda para jalar"]

    # 2. Crear un diccionario llamado perfil_mascota que almacene esta información
    perfil_mascota = {
        "nombre": nombre_mascota,
        "edad": edad_mascota,
        "premios_favoritos": premios_favoritos,
        "adoptado": False
    }

    print("=== Perfil de la Mascota ===")
    print(f"Perfil completo: {perfil_mascota}")
    print()

    # 3. Acceder e imprimir el nombre de la mascota y su segundo premio favorito
    print("=== Información Inicial ===")
    print(f"Nombre de la mascota: {perfil_mascota['nombre']}")
    print(f"Segundo premio favorito: {perfil_mascota['premios_favoritos'][1]}")
    print()

    # 4. Actualizar la edad de la mascota y añadir un nuevo premio a su lista
    perfil_mascota["edad"] = 4
    perfil_mascota["premios_favoritos"].append("Snack de pollo")

    print("=== Información Actualizada ===")
    print(f"Nueva edad: {perfil_mascota['edad']}")
    print(f"Lista actualizada de premios: {perfil_mascota['premios_favoritos']}")
    print(f"Perfil completo actualizado: {perfil_mascota}")
    print()

    # ------------------------------------------------------------------------
    # EJERCICIO 2: Verificación del Estado de la Mascota (Módulo 3)
    # ------------------------------------------------------------------------
    
    # 1 y 2. Definir función verificar_estado_mascota
    def verificar_estado_mascota(edad):
        """
        Verifica el estado de una mascota según su edad.
        
        Parámetros:
        edad (int): La edad de la mascota en años
        
        Retorna:
        str: "Cachorro" (< 2 años), "Adulto" (2-7 años), o "Senior" (> 7 años)
        """
        if edad < 2:
            return "Cachorro"
        elif edad <= 7:
            return "Adulto"
        else:
            return "Senior"
    
    # 3. Crear lista de edades y usar bucle for para llamar a la función
    print("=== Verificación del Estado de la Mascota ===")
    edades_mascotas = [1, 2, 4, 7, 8, 10, 0, 5, 9, 3]
    
    for edad in edades_mascotas:
        estado = verificar_estado_mascota(edad)
        print(f"Mascota de {edad} año(s): {estado}")
    print()

    # ------------------------------------------------------------------------
    # EJERCICIO 3: Integrar y Probar el Sistema de Adopción (Módulo 4)
    # ------------------------------------------------------------------------
    
    print("=== Sistema de Adopción de Mascotas con POO ===")
    
    # 3. Crear instancias de Mascota
    mascota1 = Mascota("Luna", "Perro", 3)
    mascota2 = Mascota("Michi", "Gato", 2)
    mascota3 = Mascota("Rocky", "Perro", 5)
    mascota4 = Mascota("Nala", "Gato", 1)
    
    print("\nMascotas disponibles:")
    print(f"  • {mascota1}")
    print(f"  • {mascota2}")
    print(f"  • {mascota3}")
    print(f"  • {mascota4}")
    
    # Crear instancias de Adoptante
    adoptante1 = Adoptante("Carlos Pérez", 28)
    adoptante2 = Adoptante("Ana García", 35)
    
    print(f"\nAdoptantes registrados:")
    print(f"  • {adoptante1}")
    print(f"  • {adoptante2}")
    
    # Usar el método adoptar
    print("\nProceso de adopción:")
    adoptante1.adoptar(mascota1)
    adoptante1.adoptar(mascota3)
    adoptante2.adoptar(mascota2)
    adoptante2.adoptar(mascota1)  # Intentar adoptar una mascota ya adoptada
    
    print("\nEstado final de las mascotas:")
    print(f"  • {mascota1}")
    print(f"  • {mascota2}")
    print(f"  • {mascota3}")
    print(f"  • {mascota4}")
    
    print("\nInformación de los adoptantes:")
    print(adoptante1)
    print()
    print(adoptante2)
    print()

    # ------------------------------------------------------------------------
    # EJERCICIO 4: Prueba de Adopción Segura con Manejo de Errores (Módulo 5)
    # ------------------------------------------------------------------------
    
    print("=== Adopción Segura con Manejo de Errores ===")
    
    # Crear nuevas mascotas para las pruebas
    mascota_test1 = Mascota("Toby", "Perro", 4)
    mascota_test2 = Mascota("Pelusa", "Gato", 2)
    
    # Crear un nuevo adoptante
    adoptante_test = Adoptante("Laura Martínez", 30)
    
    print(f"\nAdoptante: {adoptante_test}")
    print(f"Mascota de prueba 1: {mascota_test1}")
    print(f"Mascota de prueba 2: {mascota_test2}")
    
    # 4. Probar la lógica intentando adoptar la misma mascota dos veces
    print("\n--- Prueba 1: Primera adopción (debe ser exitosa) ---")
    asignar_adopcion(adoptante_test, mascota_test1)
    
    print("\n--- Prueba 2: Intentar adoptar la misma mascota (debe generar error) ---")
    asignar_adopcion(adoptante_test, mascota_test1)
    
    print("\n--- Prueba 3: Adoptar una mascota diferente (debe ser exitosa) ---")
    asignar_adopcion(adoptante_test, mascota_test2)
    
    print("\n--- Prueba 4: Intentar adoptar la segunda mascota nuevamente (debe generar error) ---")
    asignar_adopcion(adoptante_test, mascota_test2)
    
    print("\nEstado final:")
    print(f"  • {mascota_test1}")
    print(f"  • {mascota_test2}")
    print(f"\n{adoptante_test}")
    
    # ------------------------------------------------------------------------
    # FIN DEL PROGRAMA
    # ------------------------------------------------------------------------
    print("\n" + "="*80)
    print(" FIN DEL TALLER 1 ".center(80))
    print("="*80)
