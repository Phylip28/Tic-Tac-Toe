import random
import time

def crear_tablero():
    board = [
        [1, 2, 3],
        [4, "X", 6], 
        [7, 8, 9]
    ]
    return board

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


def campos_libres(board):
    field = [(columna,fila) for columna in range(3) for fila in range(3) if isinstance(board[columna][fila], int)]
    return field if field else False

def verificar_tablero(board, sign):
    for posibilidades in range(3): 
        if board[posibilidades][0] == board[posibilidades][1] == board[posibilidades][2] == sign:   
            return True
        elif board[0][posibilidades] == board[1][posibilidades] == board[2][posibilidades] == sign: 
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign or board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def resultado(board, sign):
    if verificar_tablero(board, 'X'):
        return "La maquina gana -> X"
    elif verificar_tablero(board, 'O'):
        return "El jugador gana -> O"
    elif not verificar_tablero(board, sign):
        return "Empate"

def movimiento_maquina(board):
        casillas_libres = campos_libres(board)

        if casillas_libres:
            indice = random.randrange(len(casillas_libres))
            columna, fila = casillas_libres[indice]

            print("Turno de la maquina -> ")
            board[columna][fila] = "X"
            time.sleep(1)
            return True
        
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

while True:
    print("Bienvenido al juego de Tic Tac Toe")
    print("1. Iniciar juego")
    print("2. Como jugar")
    print("3. Salir del juego")
    
    try:
    
        opcion = int(input("Elija una opción: "))

        match opcion:
                case 1:
                    player_name = input("Ingresa tu nombre: ")
                        
                    tablero = crear_tablero()
                    estado_del_tablero(tablero)
                    
                    while True:
                        
                        movimiento_usuario(tablero, player_name)
                        estado_del_tablero(tablero)

                        if verificar_tablero(tablero, 'O'):
                            print(resultado(tablero, player_name))
                            break
                        
                        movimiento_maquina(tablero)
                        estado_del_tablero(tablero)
                        
                        if verificar_tablero(tablero, 'X'):
                            print(resultado(tablero, player_name))
                            break
                        
                        if not verificar_tablero(tablero, 'X') and not verificar_tablero(tablero, 'O') and not campos_libres(tablero):
                            print("Empate")
                            break
        
                case 2:
                    print("\n")
                    instrucciones()
                    print("\n")

                case 3:
                    print("\n","¡Gracias por jugar!")
                    break
    except ValueError:
        print("Por favor ingrese una opcion válida")