from core.pj import crear_personaje_interactivo

def main():
    print("=== GENERADOR DE PERSONAJES D&D ===")
    
    mi_personaje = crear_personaje_interactivo()
    
    print("\n=== ESTADÍSTICAS FINALES DEL PERSONAJE ===")
    mi_personaje.show_stats()
    

if __name__ == "__main__":
    main()
