import random
import time

# Crea el tablero inicial con 'X' en el centro (posición inicial de la máquina)
def crear_tablero():
    board = [
        [1, 2, 3],
        [4, "X", 6], 
        [7, 8, 9]
    ]
    return board

# Muestra el estado actual del tablero en la consola
def estado_del_tablero(board):
    print(f'''                                              +-------+-------+-------+
                                              |       |       |       |
                                              |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
                                              |       |       |       |
                                              +-------+-------+-------+
                                              |       |       |       |                       
                                              |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
                                              |       |       |       |
                                              +-------+-------+-------+
                                              |       |       |       |
                                              |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
                                              |       |       |       |
                                              +-------+-------+-------+                                    ''')
    
# Maneja y procesa el movimiento del jugador, asegurando que sea válido
def movimiento_usuario(board, name = "Player"):
    while True:
        try:
            casillas_libres = campos_libres(board)

            if casillas_libres:
                posicion = int(input(f"Turno de {name} -> "))

                if posicion in range(1, 10):
                    for columna in range(3):
                        for fila in range(3):
                            if board[columna][fila] == posicion:
                                board[columna][fila] = "O"
                                return True
                    print("Esta posicion ya esta ocupada")
                    continue
                else:
                    print("Por favor ingrese un numero en el rango de 1 a 9")
                    continue
                
        except ValueError:
            print("Por favor ingrese un numero valido")
            continue

# Retorna una lista de las posiciones disponibles en el tablero
def campos_libres(board):
    field = [(columna,fila) for columna in range(3) for fila in range(3) if isinstance(board[columna][fila], int)]
    return field if field else False

# Verifica si hay un ganador en el tablero actual
def verificar_tablero(board, sign):
    # Revisa filas
    for posibilidades in range(3): 
        if board[posibilidades][0] == board[posibilidades][1] == board[posibilidades][2] == sign:   
            return True
        # Revisa columnas
        elif board[0][posibilidades] == board[1][posibilidades] == board[2][posibilidades] == sign: 
            return True
    # Revisa diagonales
    if board[0][0] == board[1][1] == board[2][2] == sign or board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

# Determina y retorna el resultado final del juego
def resultado(board, sign):
    if verificar_tablero(board, 'X'):
        return "La maquina gana -> X"
    elif verificar_tablero(board, 'O'):
        return "El jugador gana -> O"
    elif not verificar_tablero(board, sign):
        return "Empate"

# Procesa el movimiento de la máquina de manera aleatoria
def movimiento_maquina(board):
        casillas_libres = campos_libres(board)

        if casillas_libres:
            indice = random.randrange(len(casillas_libres))
            columna, fila = casillas_libres[indice]

            print("Turno de la maquina -> ")
            board[columna][fila] = "X"
            time.sleep(1)
            return True
        
# Muestra las instrucciones del juego al usuario
def instrucciones():
    bienvenida = ["Bienvenido al Tutorial de Tic Tac Toe",
        "1. El tablero tiene 9 casillas numeradas del 1 al 9",
        "2. Tú juegas con 'O', la máquina con 'X'",
        "3. Para hacer un movimiento, ingresa el número de la casilla",
        "4. Gana quien complete una línea de tres símbolos iguales"]
    
    for linea in bienvenida:
        print(linea)
        time.sleep(2)

    print("Aqui tienes un ejemplo de como se ve el tablero:")

    print('''
            +---------------------------------------------------------------------------------------------------------+
            |                                                                                                         |
            |                                                                                                         | 
            |                                        +-------+-------+-------+                                        |
            |                                        |       |       |       |                                        |
            |                                        |   1   |   2   |   O   |                                        |
            |                                        |       |       |       |                                        |
            |                                        +-------+-------+-------+                                        |
            |                                        |       |       |       |                                        |
            |                                        |   4   |   x   |   6   |                                        |
            |                                        |       |       |       |                                        |
            |                                        +-------+-------+-------+                                        |
            |                                        |       |       |       |                                        |
            |                                        |   7   |   8   |   9   |                                        |
            |                                        |       |       |       |                                        |
            |                                        +-------+-------+-------+                                        |
            |                                                                                                         |
            |                                                                                                         |
            +---------------------------------------------------------------------------------------------------------+ 
    ''')
    time.sleep(3)

# Bucle principal del juego
while True:
    print("Bienvenido al juego de Tic Tac Toe")
    print("1. Iniciar juego")
    print("2. Como jugar")
    print("3. Salir del juego")
    
    try:
        opcion = int(input("Elija una opción: "))

        match opcion:
                # Opción para iniciar el juego
                case 1:
                    player_name = input("Ingresa tu nombre: ")
                        
                    tablero = crear_tablero()
                    estado_del_tablero(tablero)
                    
                    while True:
                        # Turno del jugador
                        movimiento_usuario(tablero, player_name)
                        estado_del_tablero(tablero)

                        # Verifica si el jugador ganó
                        if verificar_tablero(tablero, 'O'):
                            print(resultado(tablero, player_name))
                            break
                        
                        # Turno de la máquina
                        movimiento_maquina(tablero)
                        estado_del_tablero(tablero)
                        
                        # Verifica si la máquina ganó
                        if verificar_tablero(tablero, 'X'):
                            print(resultado(tablero, player_name))
                            break
                        
                        # Verifica si hay empate
                        if not verificar_tablero(tablero, 'X') and not verificar_tablero(tablero, 'O') and not campos_libres(tablero):
                            print("Empate")
                            break
        
                # Opción para mostrar las instrucciones
                case 2:
                    print("\n")
                    instrucciones()
                    print("\n")

                # Opción para salir del juego
                case 3:
                    print("\n","¡Gracias por jugar!")
                    break
    except ValueError:
        print("Por favor ingrese una opcion válida")
