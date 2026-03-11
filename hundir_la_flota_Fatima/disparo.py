# funcion para disparar.

def disparar(tablero_defensor, i, j):
    ''' 
    simula un disparo en el tablero de la maquina.
    comprueba la posicion (i, j):
    -Si hay barco ("B"): muestra un mensaje de "tocado..."
    -Si no hay barco: marca la posición como agua ("o") y muestra "Agua".
    -si el usuario introduce coordenadas ya usadas: muestra  mensaje "ya disparaste en (i,j)
    "'''
    if tablero_defensor [i][j] == "B":
        tablero_defensor[i][j] = "X"
        print(f"Tocado en posición: {i}, {j}")
        return True
    elif tablero_defensor[i][j] == " ":
        tablero_defensor[i][j] = "O"
        print("Agua")
        return False
    else: # cuando el usuario introduce coordenadas ya usadas.
        print(f"Ya disparaste en {i},{j}")
        return False
  