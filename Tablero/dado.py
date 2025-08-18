from clear_cli import clear
import random
import time

caras_ascii = {
    1: '''
        ╔════════╗
        ║        ║
        ║   ●    ║
        ║        ║
        ╚════════╝
        ''',
    2: '''
        ╔════════╗
        ║ ●      ║
        ║        ║
        ║      ● ║
        ╚════════╝
        ''',
    3: '''
        ╔════════╗
        ║ ●      ║
        ║   ●    ║
        ║      ● ║
        ╚════════╝
        ''',
    4: '''
        ╔════════╗
        ║ ●   ●  ║
        ║        ║
        ║ ●   ●  ║
        ╚════════╝
        ''',
    5: '''
        ╔════════╗
        ║ ●   ●  ║
        ║   ●    ║
        ║ ●   ●  ║
        ╚════════╝
        ''',
    6: '''
        ╔════════╗
        ║ ●   ●  ║
        ║ ●   ●  ║
        ║ ●   ●  ║
        ╚════════╝
        '''
}

def tirar_dados():
    cara = 0
    for _ in range(10):
        cara = random.randint(1, 6)
        clear()
        for line in caras_ascii[cara].splitlines():
            print(line)
        time.sleep(0.1)
        clear()
    return cara

def imprimir_dado(num):
    for linea in caras_ascii[num].splitlines():
        print(linea)

