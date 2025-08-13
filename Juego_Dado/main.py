from jugador import Personaje
from dado import tirar_dados, imprimir_dado
from clear_cli import clear

def tirar_para_jugador(jugador):
    # tirar dados
    print(f"Tirando dado para {jugador.nombre}")
    resultado = tirar_dados()
    print(f"{jugador.nombre} obtuvo un {resultado}")
    return resultado

def mostrar_resultados(jugador1, resultado1, jugador2, resultado2, criterio):
    # los dados ASCII
    print("=== RESULTADOS FINALES ===")
    print(f"{jugador1.nombre}:")
    imprimir_dado(resultado1)
    print(f"{jugador2.nombre}:")
    imprimir_dado(resultado2)

    if criterio == "mayor":
        if resultado1 > resultado2:
            print(f"{jugador1.nombre} empieza primero")
        elif resultado2 > resultado1:
            print(f"{jugador2.nombre} empieza primero")
        else:
            print("Empate tirar otra vez.")
    elif criterio == "menor":
        if resultado1 < resultado2:
            print(f"{jugador1.nombre} empieza primero")
        elif resultado2 < resultado1:
            print(f"{jugador2.nombre} empieza primero")
        else:
            print("Empate, tirar otra vez")
    else:
        print("Criterio no válido. Debes escribir 'mayor' o 'menor'")

def main():
    clear()
    print("Bienvenidos al juego del dado")
    
    jugador1 = Personaje(turno=1)
    jugador2 = Personaje(turno=2)

    criterio = input("Quién empieza?, Escribe 'mayor' o 'menor': ").strip().lower()

    resultado1 = tirar_para_jugador(jugador1)
    input("Presiona Enter para que el siguiente jugador tire el dado")
    resultado2 = tirar_para_jugador(jugador2)

    mostrar_resultados(jugador1, resultado1, jugador2, resultado2, criterio)

if __name__ == "__main__":
    main()
