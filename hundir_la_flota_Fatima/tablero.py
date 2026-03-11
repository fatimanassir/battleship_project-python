# Crear tablero mediante funcion.

def tablero_10x10():
    '''
    nos crea y devuelve tablero 10x10 con espacio (" ").
    '''
    tablero = [] # Me crea una lista vacía llamada tablero, que contendrá las 10 filas del tablero.
    for i in range(10): #Bucle: se repetirá 10 veces (una por cada fila del tablero)
        fila = [] # me creauna lista vacía llamada fila que representará una fila del tablero.
        for j in range(10): # recorre las 10 columnas de la fila.
            fila.append(" ") # añade espacio " " a la fila, representando una celda vacía del tablero.
        tablero.append(fila) # Cuando la fila está completa con 10 celdas, la añade al tablero
    return tablero # Devuelve la lista tablero


#funcion que muestra el tablero.
def mostrar_tablero(tablero):
    '''para cada fila en tablero
    imprimir fila
    '''
    for fila in tablero:
        print(fila)
        
        
#definimos variables: tablero_jugador & tablero_maquina.
tablero_jugador = tablero_10x10()
tablero_maquina = tablero_10x10()

# Posicionar los barcos del JUGADOR:

# 4 barcos de 1 posición de eslora:
tablero_jugador[0][0] = "B"
tablero_jugador[9][0] = "B"
tablero_jugador[0][9] = "B"
tablero_jugador[9][9] = "B"
# 3 barcos de 2 posición de eslora:
#primero
tablero_jugador[0][3] = "B"
tablero_jugador[0][4] = "B"
#segundo
tablero_jugador[9][3] = "B"
tablero_jugador[9][4] = "B"
#tercero
tablero_jugador[3][0] = "B"
tablero_jugador[3][1] = "B"
# 2 barcos de 3 posición de eslora:
#primero
tablero_jugador[5][5] = "B"
tablero_jugador[6][5] = "B"
tablero_jugador[7][5] = "B"
#segundo
tablero_jugador[5][2] = "B"
tablero_jugador[6][2] = "B"
tablero_jugador[7][2] = "B"
# 1 barcos de 4 posición de eslora:
tablero_jugador[8][8] = "B"
tablero_jugador[8][9] = "B"
tablero_jugador[8][7] = "B"
tablero_jugador[8][6] = "B"

# Posicionar los barcos de la MAQUINA
# 4 barcos de 1 posición de eslora:
tablero_maquina[0][0] = "B"
tablero_maquina[9][0] = "B"
tablero_maquina[0][9] = "B"
tablero_maquina[9][9] = "B"
# 3 barcos de 2 posición de eslora:
#primero
tablero_maquina[0][3] = "B"
tablero_maquina[0][4] = "B"
#segundo
tablero_maquina[9][3] = "B"
tablero_maquina[9][4] = "B"
#tercero
tablero_maquina[3][0] = "B"
tablero_maquina[3][1] = "B"
# 2 barcos de 3 posición de eslora:
#primero
tablero_maquina[5][5] = "B"
tablero_maquina[6][5] = "B"
tablero_maquina[7][5] = "B"
#segundo
tablero_maquina[5][2] = "B"
tablero_maquina[6][2] = "B"
tablero_maquina[7][2] = "B"
# 1 barcos de 4 posición de eslora:
tablero_maquina[8][8] = "B"
tablero_maquina[8][9] = "B"
tablero_maquina[8][7] = "B"
tablero_maquina[8][6] = "B"

# HAGO el PRINT de variabales tablero jugador y tablero maquina.
print(tablero_jugador)
print(tablero_maquina) 