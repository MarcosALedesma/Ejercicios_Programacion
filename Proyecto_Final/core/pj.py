import sys
import os

# Agregar el directorio raíz al path para importar desde api
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from api.dnd_api import get_races, get_classes, get_race_details

class Personaje:
    def __init__(self, nombre, raza, clase, stats, nivel=1):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.stats = stats
        self.nivel = nivel
        self.puntos_golpe_maximos = self.calcular_puntos_golpe()
        self.puntos_golpe_actuales = self.puntos_golpe_maximos
        self.clase_armadura = 10 + self.mod_stat('dexterity')
        self.bono_competencia = 2  # Bono base por competencia

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Raza: {self.raza}\n"
                f"Clase: {self.clase}\n"
                f"Nivel: {self.nivel}\n"
                f"Puntos de Golpe: {self.puntos_golpe_actuales}/{self.puntos_golpe_maximos}\n"
                f"Clase de Armadura: {self.clase_armadura}\n"
                f"Stats: {self.stats}\n"
                f"Modificadores: FUE:{self.mod_stat('strength')}, DES:{self.mod_stat('dexterity')}, "
                f"CON:{self.mod_stat('constitution')}, INT:{self.mod_stat('intelligence')}, "
                f"SAB:{self.mod_stat('wisdom')}, CAR:{self.mod_stat('charisma')}")

    def mod_stat(self, stat):
        """Calcula el modificador de una estadística"""
        valor_stat = self.stats[stat]
        modificador = (valor_stat - 10) // 2
        return modificador

    def calcular_puntos_golpe(self):
        """Calcula los puntos de golpe basados en la clase y constitución"""
        # Dados de golpe por clase (simplificado)
        dados_golpe = {
            'barbarian': 12,
            'fighter': 10,
            'paladin': 10,
            'ranger': 10,
            'rogue': 8,
            'bard': 8,
            'cleric': 8,
            'druid': 8,
            'monk': 8,
            'warlock': 8,
            'wizard': 6,
            'sorcerer': 6
        }
        
        # Tomamos el dado de golpe base de la clase (o 8 por defecto)
        dado_golpe = dados_golpe.get(self.clase.lower(), 8)
        
        # Puntos de golpe = dado de golpe + modificador de constitución
        puntos_golpe = dado_golpe + self.mod_stat('constitution')
        
        # Aseguramos un mínimo de 1 punto de golpe por nivel
        return max(puntos_golpe, 1)

    def atacar(self):
        """Calcula el daño de un ataque básico"""
        # Determinamos qué estadística usar para atacar basado en la clase
        if self.clase.lower() in ['wizard', 'sorcerer', 'warlock']:
            stat_ataque = 'intelligence'
        elif self.clase.lower() in ['cleric', 'druid', 'ranger']:
            stat_ataque = 'wisdom'
        elif self.clase.lower() in ['paladin', 'bard']:
            stat_ataque = 'charisma'
        else:
            stat_ataque = 'strength'  # Para guerreros, bárbaros, etc.
        
        # Daño base (simplificado)
        daño_base = {
            'barbarian': 8,
            'fighter': 6,
            'paladin': 6,
            'ranger': 6,
            'rogue': 4,
            'bard': 4,
            'cleric': 4,
            'druid': 4,
            'monk': 4,
            'warlock': 4,
            'wizard': 4,
            'sorcerer': 4
        }
        
        daño = daño_base.get(self.clase.lower(), 4) + self.mod_stat(stat_ataque)
        return max(daño, 1)  # Mínimo 1 de daño

    def mostrar_resumen_combate(self):
        """Muestra un resumen de las capacidades de combate del personaje"""
        return (f"=== RESUMEN DE COMBATE ===\n"
                f"Clase de Armadura: {self.clase_armadura}\n"
                f"Puntos de Golpe: {self.puntos_golpe_actuales}/{self.puntos_golpe_maximos}\n"
                f"Daño por Ataque: {self.atacar()}\n"
                f"Modificador de Fuerza: {self.mod_stat('strength')}\n"
                f"Modificador de Destreza: {self.mod_stat('dexterity')}\n"
                f"Modificador de Constitución: {self.mod_stat('constitution')}")

# Funciones auxiliares para la creación de personajes
def elegir_opcion(opciones, tipo):
    """Función helper para elegir entre opciones"""
    print(f"\nElige una {tipo}:")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion['name']}")
    
    while True:
        try:
            seleccion = int(input("Opción: ")) - 1
            if 0 <= seleccion < len(opciones):
                return opciones[seleccion]
            print("Opción inválida. Intenta de nuevo.")
        except ValueError:
            print("Por favor ingresa un número.")

def generar_stats(detalles_raza):
    """Genera los stats base y aplica bonificaciones raciales"""
    # Stats base (método estándar D&D)
    stats_base = {
        'strength': 15, 
        'dexterity': 14, 
        'constitution': 13,
        'intelligence': 12, 
        'wisdom': 10, 
        'charisma': 8
    }
    
    # Aplicar bonificaciones de raza
    for bonus in detalles_raza.get('ability_bonuses', []):
        habilidad = bonus['ability_score']['name']
        # Convertir a minúsculas y quitar espacios
        habilidad = habilidad.lower().replace('-', '_')
        stats_base[habilidad] = stats_base.get(habilidad, 10) + bonus['bonus']
    
    return stats_base

def crear_personaje_interactivo():
    """Función principal para crear un personaje interactivamente"""
    print("=== CREACIÓN DE PERSONAJE ===")
    
    # Obtener datos de la API
    razas = get_races()['results']
    clases = get_classes()['results']
    
    # Elegir raza
    raza_elegida = elegir_opcion(razas, "raza")
    detalles_raza = get_race_details(raza_elegida['index'])
    
    # Elegir clase
    clase_elegida = elegir_opcion(clases, "clase")
    
    # Generar stats
    stats = generar_stats(detalles_raza)
    
    # Pedir nombre
    nombre = input("\nIngresa el nombre de tu personaje: ")
    
    # Crear y retornar instancia de Personaje
    return Personaje(
        nombre=nombre,
        raza=raza_elegida['name'],
        clase=clase_elegida['name'],
        stats=stats
    )

def crear_personaje_rapido(nombre, raza_index=0, clase_index=0):
    """Función para creación rápida sin interacción"""
    razas = get_races()['results']
    clases = get_classes()['results']
    
    raza_elegida = razas[raza_index]
    clase_elegida = clases[clase_index]
    detalles_raza = get_race_details(raza_elegida['index'])
    
    stats = generar_stats(detalles_raza)
    
    return Personaje(
        nombre=nombre,
        raza=raza_elegida['name'],
        clase=clase_elegida['name'],
        stats=stats
    )