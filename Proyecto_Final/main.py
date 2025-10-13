#main.py
import pj
import monstruos
import combate
from  dashborad import menu
from clear_cli import clear  

clear()
print("╔"+("═" * 57)+"╗")
print("║"+"Bienvenido al juego".center(57)+"║")
jugador = pj.crear_personaje()
enemigo = monstruos.Murcielago()  # creas enemigo antes del menú

clear()

combate.combate(jugador, enemigo)  # sistema de combate

if jugador.vida <= 0:
    print("Game Over")
else:
    jugador.show_stats()