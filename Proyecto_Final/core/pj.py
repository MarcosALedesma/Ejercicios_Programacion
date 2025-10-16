# personaje.py
import random
import sys
import os

# Agregar el directorio raíz al path para importar desde api
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from api.dnd_api import obtener_races, obtener_classes, obtener_race_detalle

class Personaje:
    def __init__(self, nombre, raza, clase, stats):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.stats = stats

    def __str__(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}, Clase: {self.clase}, Stats: {self.stats}"

    def show_stats(self):
        print()
        print("Stats Base".center(21))
        print("╔"+("═" * 20)+"╗")
        print(f"║Nombre: {self.nombre}".ljust(21)+"║")
        print(f"║Raza: {self.raza}".ljust(21)+"║")
        print(f"║Clase: {self.clase}".ljust(21)+"║")
        print("║"+("═"* 20)+"║")
        print(f"║Fuerza: {self.stats['strength']}".ljust(21)+"║")
        print(f"║Destreza: {self.stats['dexterity']}".ljust(21)+"║")
        print(f"║Constitución: {self.stats['constitution']}".ljust(21)+"║")
        print(f"║Inteligencia: {self.stats['intelligence']}".ljust(21)+"║")
        print(f"║Sabiduría: {self.stats['wisdom']}".ljust(21)+"║")
        print(f"║Carisma: {self.stats['charisma']}".ljust(21)+"║")
        print("╚"+("═" * 20)+"╝")

#==== Auxiliares ====#
def elegir_opcion(opciones, tipo):
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

#==== Stats ====#
def rolear_stats():
    dados = [random.randint(1, 6) for _ in range(6)]
    dados.remove(min(dados))
    return sum(dados)

def generar_stats(detalles_raza):
    stats_base = {
        'strength': rolear_stats(),
        'dexterity': rolear_stats(),
        'constitution': rolear_stats(),
        'intelligence': rolear_stats(),
        'wisdom': rolear_stats(),
        'charisma': rolear_stats(),
    }

    # bonificaciones de raza
    for bonus in detalles_raza.get('ability_bonuses', []):
        habilidad = bonus['ability_score']['name']
        habilidad = habilidad.lower().replace('-', '_')
        stats_base[habilidad] = stats_base.get(habilidad, 10) + bonus['bonus']

    return stats_base

#==== Creación ====#
def crear_personaje_interactivo():

    # API
    razas = obtener_races()['results']
    clases = obtener_classes()['results']

    # raza
    raza_elegida = elegir_opcion(razas, "raza")
    detalles_raza = obtener_race_detalle(raza_elegida['index'])

    # Clase
    clase_elegida = elegir_opcion(clases, "clase")

    # Generar stats
    stats = generar_stats(detalles_raza)

    # nombre
    nombre = input("\nIngresa el nombre de tu personaje: ")

    # Crear personaje
    personaje = Personaje(
        nombre=nombre,
        raza=raza_elegida['name'],
        clase=clase_elegida['name'],
        stats=stats
    )
    
    return personaje
