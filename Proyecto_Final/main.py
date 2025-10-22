from core.pj import crear_personaje_interactivo

def main():
    # Crear personaje interactivamente
    personaje = crear_personaje_interactivo()
    
    print("\n¡Personaje creado exitosamente!")
    print("=" * 50)
    print(personaje)
    print("\n")
    print(personaje.mostrar_resumen_combate())
    
    # Ejemplo de uso del método atacar
    print(f"\n{personaje.nombre} realiza un ataque causando {personaje.atacar()} puntos de daño!")
    
    # Ejemplo de creación rápida (opcional)
    # from core.pj import crear_personaje_rapido
    # personaje_rapido = crear_personaje_rapido("Frodo")
    # print(personaje_rapido)

if __name__ == "__main__":
    main()