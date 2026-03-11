#para ver si quedan barcos.
def quedan_barcos(tablero):
    '''
    Comprueba si todavía quedan barcos en el tablero.
    args:
    tablero: lista de listas que representa el tablero del juego.
    
    Funcionamiento:
    Recorre cada fila del tablero y busca si existe la letra "B",
    que representa un barco.
    
    Si encuentra una "B", significa que aún queda al menos un barco
    y devuelve True.

    Si revisa todo el tablero y no encuentra ninguna "B",
    devuelve False.
    '''
    for fila in tablero:
        if "B" in fila:
            return True # si hay barco ("B") me devuelve True.
    return False #Solo devuelve False si ninguna fila tiene barcos.