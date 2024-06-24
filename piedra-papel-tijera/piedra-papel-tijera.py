# Piedra - Papel - Tijera (v2) 

# * Falta optimizar porque se repite código. Aguante los break. *

# COLORES
red = "\033[91m"
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m"

# VARIABLES GLOBABLES
modoDeJuego = ''
flagSeguirJugando = True

# FUNCIÓN - Elegir Modo de Juego
def elegir_modo():

    # Variables
    global modoDeJuego
    flagElegirModo = True

    # Iniciar Ejecución
    print('===================================')
    print('- MODOS DE JUEGO -')
    print(f'\n{blue}1. Jugador vs PC{reset}')
    print(f'{red}2. Jugador vs Jugador{reset}')

    while flagElegirModo:

        modoElegido = input('\nIngresa el número correspondiente: ')

        # Verifico que sea un número
        while not modoElegido.isnumeric():
            print(f'{yellow}Error. Por favor, ingresa un número.{reset}')
            modoElegido = input('\nIngresa el número correspondiente: ')

        # Mostramos el modo elegido
        if int(modoElegido) == 1:
            print(f'{blue}MODO ELEGIDO: Jugador vs PC{reset}')
            
            modoDeJuego = 'jugadorvspc'
            flagElegirModo = False
        elif int(modoElegido) == 2:
            print(f'{red}MODO ELEGIDO: Jugador vs Jugador{reset}')
            modoDeJuego = 'jugadorvsjugador'
            flagElegirModo = False
        else:
            print(f'{yellow}Error. Por favor, ingresa un número posible.{reset}')

# FUNCIÓN - Jugador vs PC
def jugador_pc():

    import random

    # Variables Locales
    flagJugadaUsuario = True
    listaJugadas = ['Piedra', 'Papel', 'Tijera'] 
    resultado = ''
    victoriasUsuario = 0
    victoriasIA = 0

    # Iniciar Ejecución
    while True:

        # Iniciar Juego
        print('===================================')
        print(f'{yellow}¿Piedra - Papel - Tijera?{reset} (Fin para salir)')
        print('')

        # Jugada Usuario
        while True:
            jugadaUsuario = input('Jugada Usuario: ')
            jugadaUsuario = jugadaUsuario.strip().capitalize()

            if jugadaUsuario == 'Fin': 
                flagJugadaUsuario = False
                break
            elif (jugadaUsuario not in listaJugadas):
                print(f'{red}Jugada no válida. Por favor, vuelve a escribir tu jugada.{reset}')
            else:
                break

        # Finalizar Ejecución
        if not flagJugadaUsuario: 
            print('===================================')
            break

        # Jugada IA
        jugadaIA = listaJugadas[random.randrange(3)]

        # Mostrar Jugadas
        print(f'\n{blue}(TÚ) {jugadaUsuario}{reset}')
        print(f'{red}(IA) {jugadaIA}{reset}\n')
            
        # Comparar Jugadas
        if jugadaUsuario == jugadaIA:
            print('Empate')
        elif(jugadaUsuario == 'Piedra' and jugadaIA == 'Tijera') or \
            (jugadaUsuario == 'Papel'  and jugadaIA == 'Piedra') or \
            (jugadaUsuario == 'Tijera' and jugadaIA == 'Papel'):
            print('Ganaste')
            victoriasUsuario += 1
        else:
            print('Perdiste')
            victoriasIA += 1

        # Mostrar Resultado
        print (f'{yellow}Resultado:{reset} {blue}{victoriasUsuario}{reset} - {red}{victoriasIA}{reset}')
        print(resultado)

        if victoriasUsuario == 3 or victoriasIA == 3:
            print('===================================')
            break

# FUNCIÓN - Jugador vs Jugador
def jugador_jugador():

    import getpass

    # Variables Locales
    flagJugadaUsuario = True
    listaJugadas = ['Piedra', 'Papel', 'Tijera'] 
    resultado = ''
    victoriasUsuario1 = 0
    victoriasUsuario2 = 0

    # Iniciar Ejecución
    while True:

        # Iniciar Juego
        print('===================================')
        print(f'{yellow}¿Piedra - Papel - Tijera?{reset} (Fin para salir)')
        print('')

        # Jugada Usuario 1
        while True:
            jugadaUsuario1 = getpass.getpass('Jugada Usuario 1: ') #input()
            jugadaUsuario1 = jugadaUsuario1.strip().capitalize()

            if jugadaUsuario1 == 'Fin': 
                flagJugadaUsuario = False
                break
            elif (jugadaUsuario1 not in listaJugadas):
                print(f'{red}Jugada no válida. Por favor, vuelve a escribir tu jugada.{reset}')
            else:
                break

        # Finalizar Ejecución
        if not flagJugadaUsuario: 
            print('===================================')
            break

        # Jugada Usuario 2
        while True:
            jugadaUsuario2 = getpass.getpass('Jugada Usuario 2: ') #input()
            jugadaUsuario2 = jugadaUsuario2.strip().capitalize()

            if jugadaUsuario2 == 'Fin': 
                flagJugadaUsuario = False
                break
            elif (jugadaUsuario2 not in listaJugadas):
                print(f'{red}Jugada no válida. Por favor, vuelve a escribir tu jugada.{reset}')
            else:
                break

        # Finalizar Ejecución
        if not flagJugadaUsuario: 
            print('===================================')
            break

        # Mostrar Jugadas
        print(f'\n{blue}(Usuario 1) {jugadaUsuario1}{reset}')
        print(f'{red}(Usuario 2) {jugadaUsuario2}{reset}\n')
            
        # Comparar Jugadas
        if jugadaUsuario1 == jugadaUsuario2:
            print('Empate')
        elif(jugadaUsuario1 == 'Piedra' and jugadaUsuario2 == 'Tijera') or \
            (jugadaUsuario1 == 'Papel'  and jugadaUsuario2 == 'Piedra') or \
            (jugadaUsuario1 == 'Tijera' and jugadaUsuario2 == 'Papel'):
            print('Ganó el Usuario 1')
            victoriasUsuario1 += 1
        else:
            print('Ganó el Usuario 2')
            victoriasUsuario2 += 1

        # Mostrar Resultado
        print (f'{yellow}Resultado:{reset} {blue}{victoriasUsuario1}{reset} - {red}{victoriasUsuario2}{reset}')
        print(resultado)

        if victoriasUsuario1 == 3 or victoriasUsuario2 == 3:
            print('===================================')
            break

# EJECUCIÓN PRINCIPAL
while flagSeguirJugando:

    elegir_modo()
    if modoDeJuego == 'jugadorvspc':
        jugador_pc()
    elif modoDeJuego == 'jugadorvsjugador':
        jugador_jugador()

    seguirJugando = input(f'{yellow}¿Quieres seguir jugando? ¿SI o NO? {reset}').strip().upper()

    while seguirJugando != 'SI' and seguirJugando != 'NO':
        print(f'{red}Error. Por favor, escribe una opción válida.{reset}')
        seguirJugando = input(f'{yellow}¿Quieres seguir jugando? ¿SI o NO? {reset}').strip().upper()

    if seguirJugando == 'NO':
        print('===================================')
        flagSeguirJugando = False