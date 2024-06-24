# Juego de la predicción, similar al de "el gato y la caja".
# https://elgatoylacaja.com/elnudo/el-juego-de-la-prediccion?utm_source=sitioEGLC&utm_medium=gato-hoy

# Imports
import random

# Colores
red = "\033[91m"
green = '\033[92m'
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m"

# Variables Globales
jugadasPosibles = ['i', 'd'] # jugadas posibles, i = izquierda o d = derecha
historialJugadas = [] # historial total de jugadas
subHistorialJugadas = [] # historial parcial de jugadas, divididas en sub-arrays de 4 elementos
historialRecienteJugadas = [] # ultimas 4 jugadas
ultimaJugadaUsuario = '' # se guarda la ultima jugada para agregarla posteriormente a historialJugadas
contadorRondas = 1 # ronda actual
puntosMaximo = 50 # cantidad de rondas
puntosUsuario = 0 # rondas ganadas por usuario
puntosIA = 0 # rondas ganadas por IA

# Reglas
def dar_reglas(): # Se utiliza únicamente al inicio de la partida. Imprime las reglas del juego.
    print('=============================================================')
    print(f'{yellow}1) Evita que la IA anticipe tu jugada{reset}')
    print(f'{yellow}2) Tienes dos opciones: I (izquierda) o D (derecha){reset}')
    print(f'{yellow}3) El primero en alcanzar los {puntosMaximo} puntos, gana{reset}')
    print(f'\n{yellow}¿Podrás ganarle a la IA? ¡Suerte!{reset}')

# Jugada Usuario
def jugada_usuario():
    global ultimaJugadaUsuario

    jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower() # El usuario ingresa su jugada ('i' o 'd')

    while jugadaUsuario not in jugadasPosibles: # Si la jugada NO es ni 'i' o 'd', ...
        if jugadaUsuario == '/historial':
            print(historialJugadas) # Imprime todas las jugadas del usuario
            jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower()
        # elif jugadaUsuario == '/subhistorial':
        #     print(subHistorialJugadas) # Imprime las jugadas del usuario, divididas en arrays de 4 elementos
        #     jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower()
        elif jugadaUsuario == '/reciente':
            print(historialRecienteJugadas) # Imprime las ultimas 4 jugadas del usuario
            jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower()
        elif jugadaUsuario == '!help': # Imprime los distintos comandos
            print(f'{green}/historial{reset} para ver todas las jugadas que hiciste hasta el momento.')
            #print(f'{green}/subhistorial{reset} para ver las jugadas que hiciste, divididas en arrays de 4 elementos.')
            print(f'{green}/reciente{reset} para ver las últimas 4 jugadas realizadas.')
            jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower()
        else:
            print(f'{yellow}Jugada inválida. Por favor, escribe nuevamente.{reset}\n') # Imprime 'jugada inválida'
            jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower()

    ultimaJugadaUsuario = jugadaUsuario # Si la jugada es 'i' o 'd', se guarda en esta variable temporalmente. Esto debido a que no quiero que sea tenido en cuenta por la IA cuando realice su jugada, por lo tanto se agrega al historialJugadas una vez realizada la comparacion
    return jugadaUsuario # Retorna el valor de la jugada del usuario

# Jugada IA
def jugada_ia():
    global subHistorialJugadas, historialRecienteJugadas
    contadorI = 0
    contadorD = 0

    if len(historialJugadas) <= 4: # Las primeras 4 jugadas, se juegan aleatoriamente
        jugadaIA = jugadasPosibles[random.randrange(2)] # alternativa: random.choice(jugadasPosibles)
        if len(historialJugadas) % 4 == 0: # En la 4ta jugada, se guarda el primer sub-array y el historial de jugadas reciente
            # subHistorialJugadas.append(historialJugadas[:4]) 
            historialRecienteJugadas = historialJugadas[:4]
    else: 
        # En el resto de rondas, varía según el algoritmo que esté en el momento:
        # Si está el ALGORITMO QUE CREÉ, se tiene en cuenta las jugadas recientes y cada 4 jugadas prioriza la jugada que más realizó el usuario en cada sub-array. En caso de haber un empate, se elige aleatoriamente.
        # Si está el ALGORITMO DEL GATO Y LA CAJA, se tiene en cuenta las jugadas recientes y si encuentra ese patrón en el historial de jugadas, se imprime la jugada siguiente realizada por el usuario con mayor frecuencia. En caso de haber un empate, se elige aleatoriamente.
        # Para usar mi algoritmo o el otro, hay que COMENTAR/DESCOMENTAR varias líneas
        historialRecienteJugadas = historialJugadas[-4:] # alternativa: historialJugadas[ (len(historialJugadas) - 4):]
        jugadaIA = jugadasPosibles[random.randrange(2)]

        for i in range( len(historialJugadas) - len(historialRecienteJugadas) ): # no quiero que el historial reciente (últimas 4 jugadas) afecte a la jugada, por lo que lo descarto
            if historialJugadas[i : i+len(historialRecienteJugadas)] == historialRecienteJugadas:
                if historialJugadas[i+len(historialRecienteJugadas)] == 'i':
                    contadorI += 1
                else:
                    contadorD += 1

                # print(f'{historialJugadas}')
                # print(f'Este patrón se encontró a partir del elemento {i}.')
                # print(f'La siguiente jugada sería {historialJugadas[i+len(historialRecienteJugadas)]}. Hasta ahora, {contadorI} veces fue elegido IZQUIERDA y {contadorD} veces fue elegido DERECHA.')

                jugadaIA = comparar_contadores(contadorI,contadorD)

        # if len(historialJugadas) % 4 == 0:
        #     subHistorialJugadas.append(historialRecienteJugadas)
        # jugadaIA = opcion_mas_elegida_por_usuario_en_cada_subarray()
        
    print(f'{red}IA:{reset}', jugadaIA)
    return jugadaIA

def opcion_mas_elegida_por_usuario_en_cada_subarray(): # Esta función sirve para el algoritmo que cree yo. 
    contadorI = 0
    contadorD = 0

    if len(historialJugadas) % 4 == 0: # Cada 4 jugadas, se identifica, en cada una de las sub-arrays, cual fue la jugada mas elegida EN CADA sub-array, y dependiendo de eso, la IA elige una u otra jugada
        for i in subHistorialJugadas:
            if opcion_mas_elegida_por_usuario(i) == 'i':
                contadorI += 1
            else:
                contadorD += 1
        jugadaIA = comparar_contadores(contadorI,contadorD)
        return jugadaIA
    else: # De lo contrario, se tiene en cuenta la opcion mas elegida en las jugadas recientes del usuario.
        jugadaIA = opcion_mas_elegida_por_usuario(historialRecienteJugadas)
        return jugadaIA

def opcion_mas_elegida_por_usuario(array):
    contadorI = array.count('i') # Se cuentan y se guardan las jugadas 'i'
    contadorD = array.count('d') # Se cuentan y se guardan las jugadas 'd'
    jugadaIA = comparar_contadores(contadorI,contadorD) # Se compara las jugadas y se guarda una jugada u otra, la cual será usada por la IA
    return jugadaIA

def comparar_contadores(i,d): # Compara ambos contadores y retorna la jugada de la IA según corresponda
    if i > d:
        return 'i'
    elif i < d:
        return 'd'
    elif i == d:
        return jugadasPosibles[random.randrange(2)]

# Comparar Jugadas
def comparar_jugadas(jugadaUsuario, jugadaIA): # Si las jugadas son IGUALES, suma un punto la IA, sino, suma un punto el usuario
    global puntosUsuario, puntosIA

    if jugadaUsuario != jugadaIA:
        puntosUsuario += 1 
    elif jugadaUsuario == jugadaIA:
        puntosIA += 1

# Dar Resultado
def dar_resultado(): # Se utiliza únicamente al final de la partida. Imprime el resultado con el ganador/perdedor.
    print('=============================================================')
    print(f'{yellow}- RESULTADO -{reset}\n')
    print(f'{blue}Tú ({puntosUsuario}){reset} - {red}IA ({puntosIA}){reset}')

    if puntosUsuario > puntosIA:
        print(f'\n{yellow}Ganaste.{reset}')
    else:
        print(f'\n{yellow}Perdiste.{reset}')

# Programa Principal
dar_reglas() # Imprimimos las reglas
while puntosUsuario < puntosMaximo and puntosIA < puntosMaximo: # Comenzamos un ciclo donde el usuario y la IA van a jugar
    print('=============================================================')
    print(f'{yellow}- RONDA {contadorRondas} -{reset} (Escribe {green}!help{reset} para ver todos los comandos.)\n')
    # print(f'{yellow}historialJugadas: {historialJugadas}{reset}\n')
    # print(f'{yellow}subHistorialJugadas: {subHistorialJugadas}{reset}\n')
    # print(f'{yellow}historialRecienteJugadas: {historialRecienteJugadas}{reset}\n')
    print(f'{blue}Tú ({puntosUsuario}){reset} - {red}IA ({puntosIA}){reset}\n')
    jugadaUsuario = jugada_usuario()
    jugadaIA = jugada_ia()
    comparar_jugadas(jugadaUsuario, jugadaIA)
    historialJugadas.append(ultimaJugadaUsuario) # Ahora sí, se agrega la jugada del usuario a historialJugadas
    historialRecienteJugadas = historialJugadas[-4:] # También se actualiza el historial de jugadas recientes
    contadorRondas += 1
dar_resultado() # Al finalizar se imprime el resultado
print('=============================================================')