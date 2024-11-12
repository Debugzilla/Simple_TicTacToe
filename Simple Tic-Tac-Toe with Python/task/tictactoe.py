# Inicializar el tablero como una matriz 3x3 vacía
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Función para imprimir el tablero actual
def imprimir_tablero(tablero):
    print("---------")
    for fila in tablero:
        print(f"| {' '.join(fila)} |")
    print("---------")

# Función para verificar si las coordenadas son válidas
def movimiento_valido(tablero, fila, columna):
    return 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " "

# Función para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    combinaciones_ganadoras = [
        [(0, 0), (0, 1), (0, 2)],  # Primera fila
        [(1, 0), (1, 1), (1, 2)],  # Segunda fila
        [(2, 0), (2, 1), (2, 2)],  # Tercera fila
        [(0, 0), (1, 0), (2, 0)],  # Primera columna
        [(0, 1), (1, 1), (2, 1)],  # Segunda columna
        [(0, 2), (1, 2), (2, 2)],  # Tercera columna
        [(0, 0), (1, 1), (2, 2)],  # Diagonal principal
        [(0, 2), (1, 1), (2, 0)]   # Diagonal secundaria
    ]
    for combinacion in combinaciones_ganadoras:
        if all(tablero[f][c] == jugador for f, c in combinacion):
            return True
    return False

# Bucle del juego
def bucle_juego():
    turno = "X"  # "X" empieza el juego

    while True:
        imprimir_tablero(tablero)

        # Pedir al usuario las coordenadas
        coordenadas = input(f"Turn of {turno}. Enter the coordinates (fila columna): ")

        try:
            fila, columna = map(int, coordenadas.split())
            fila -= 1  # Convertir a índice de matriz (0-2)
            columna -= 1  # Convertir a índice de matriz (0-2)
        except ValueError:
            print("Error: you must enter two numbers separated by a space.")
            continue

        # Verificar si el movimiento es válido
        if movimiento_valido(tablero, fila, columna):
            tablero[fila][columna] = turno  # Colocar la ficha en el tablero

            # Verificar si el jugador actual ha ganado
            if verificar_ganador(tablero, turno):
                imprimir_tablero(tablero)
                print(f"{turno} wins")
                break

            # Cambiar de turno
            turno = "O" if turno == "X" else "X"
        else:
            print("Error: Invalid movement. The cell is occupied or out of range")

        # Comprobar si el tablero está lleno (empate)
        if all(celda != " " for fila in tablero for celda in fila):
            imprimir_tablero(tablero)
            print("Draw")
            break

# Llamar a la función para iniciar el juego
print("Initial board:")
bucle_juego()
