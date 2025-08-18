from jugador import Personaje
from tablero import tirar_jugador, mostrar_dados_finales, decidir_turno, jugar_tablero 
from clear_cli import clear

def main():
    clear()
    print("Bienvenidos al juego del dado")
    
    jugador1 = Personaje(turno=1)
    jugador2 = Personaje(turno=2)
    while True:
        criterio = input("¿Quién empieza? Escribe 'mayor' o 'menor': ").strip().lower()
        if criterio == "mayor" or criterio == "menor":
            break
        else:
            print("criterio no valido")
    # Decidir turnos iniciales
    resultado1 = tirar_jugador(jugador1)
    input("Presiona Enter para que el siguiente jugador tire el dado")
    resultado2 = tirar_jugador(jugador2)

    mostrar_dados_finales(jugador1, resultado1, jugador2, resultado2)

    primero, segundo = decidir_turno(jugador1, resultado1, jugador2, resultado2, criterio)

    if primero is None:
        print("Empate. Vuelvan a tirar los dados para decidir quién empieza")
        return
    
    print(f"{primero.nombre} comienza el juego seguido de {segundo.nombre}")

    jugar_tablero(primero, segundo)

if __name__ == "__main__":
    main()

