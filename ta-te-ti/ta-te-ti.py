# Ta Te Ti (la IA no predice, sólo juega)
import random, time

jugadasDisponibles = [1,2,3,4,5,6,7,8,9]
jugadasTablero = [1,2,3,4,5,6,7,8,9]

def imprimirTablero():
    print('')
    print(f' {jugadasTablero[0]} || {jugadasTablero[1]} || {jugadasTablero[2]} ')
    print('=============')
    print(f' {jugadasTablero[3]} || {jugadasTablero[4]} || {jugadasTablero[5]} ')
    print('=============')
    print(f' {jugadasTablero[6]} || {jugadasTablero[7]} || {jugadasTablero[8]} ')
    print('')

print('=======================')
imprimirTablero()

# ============================================== Asignar Símbolo
red = "\033[91m"
blue = "\033[94m"
reset = "\033[0m"

circuloCruz = ['O', 'X']
simboloJugador = random.choice(circuloCruz)

if simboloJugador == 'O':
    simboloJugador  = f'{red}O{reset}'
    simboloIA       = f'{blue}X{reset}'
elif simboloJugador == 'X':
    simboloJugador  = f'{blue}X{reset}'
    simboloIA       = f'{red}O{reset}'

print(f'El CÍRCULO juega 1° y la CRUZ juega 2°. Tú símbolo es {simboloJugador} y el símbolo de la IA es {simboloIA}.')
print('')

# ============================================== Jugar Usuario
def jugarUsuario():
    flag = True
    while flag == True:
        jugada = int( input('Elegiste la posición: ') )

        if jugada in jugadasDisponibles:
            jugadasDisponibles.remove(jugada)
            #print(jugadasDisponibles)
            jugadasTablero[jugada - 1] = simboloJugador
            imprimirTablero()
            flag = False
        else:
            print('Jugada incorrecta. Por favor, elige otra posición.')

# ============================================== Jugar IA
def jugarIA():
    time.sleep(1.5)
    jugada = random.choice(jugadasDisponibles)
    jugadasDisponibles.remove(jugada)
    jugadasTablero[jugada - 1] = simboloIA
    print(f'La IA eligió la posición: {jugada}')
    imprimirTablero()

# ============================================== Verificar Partida
ganador = False

def verificarPartida(simbolo):
    global ganador
    if \
    (jugadasTablero[0] == simbolo and jugadasTablero[1] == simbolo and jugadasTablero[2] == simbolo) or \
    (jugadasTablero[3] == simbolo and jugadasTablero[4] == simbolo and jugadasTablero[5] == simbolo) or \
    (jugadasTablero[6] == simbolo and jugadasTablero[7] == simbolo and jugadasTablero[8] == simbolo) or \
    (jugadasTablero[0] == simbolo and jugadasTablero[3] == simbolo and jugadasTablero[6] == simbolo) or \
    (jugadasTablero[1] == simbolo and jugadasTablero[4] == simbolo and jugadasTablero[7] == simbolo) or \
    (jugadasTablero[2] == simbolo and jugadasTablero[5] == simbolo and jugadasTablero[8] == simbolo) or \
    (jugadasTablero[0] == simbolo and jugadasTablero[4] == simbolo and jugadasTablero[8] == simbolo) or \
    (jugadasTablero[2] == simbolo and jugadasTablero[4] == simbolo and jugadasTablero[6] == simbolo):
        print(f'Hay un ganador. El jugador con el símbolo {simbolo} ganó.')
        print('=======================')
        ganador = True
        
# ============================================== Juego
while len(jugadasDisponibles) != 0:
    if simboloJugador == f'{red}O{reset}':
        print('=======================')
        print('')

        jugarUsuario()
        verificarPartida(simboloJugador)
        if ganador == True:
            break
        if len(jugadasDisponibles) == 0:
            print('Empate.')
            print('=======================')
            break

        jugarIA()
        verificarPartida(simboloIA)
        if ganador == True:
            break
        if len(jugadasDisponibles) == 0:
            print('Empate.')
            print('=======================')
            break
        
        print('=======================')
    else:
        print('=======================')
        print('')

        jugarIA()
        verificarPartida(simboloIA)
        if ganador == True:
            break
        if len(jugadasDisponibles) == 0:
            print('Empate.')
            print('=======================')
            break
    
        jugarUsuario()
        verificarPartida(simboloJugador)
        if ganador == True:
            break
        if len(jugadasDisponibles) == 0:
            print('Empate.')
            print('=======================')
            break
    
        print('=======================')