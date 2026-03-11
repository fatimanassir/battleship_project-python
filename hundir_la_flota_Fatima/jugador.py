# pedir coordenadas(i, j) & hacer validaciones.

def pedir_coordenadas():
    '''Pide coordenadas(i,j), el usuario debe ingresar numero de 0-9.
     La función continúa solicitando entradas (i, j) hasta que el usuario proporcione
    números enteros válidos en el rango 0-9 para ambos, fila y columna. (else /except: captura entras no numericas.)
    Si las entradas son validas, return coordenadas (i,j) '''
    while True:
        try:
            i = int(input("Introduce numero del 0-9 en fila: "))
            j = int(input("Introduce numero del 0-9 columna: "))
        except ValueError:
            print("Entradas no válidas, por favor, introduce numeros enteros entre 0-9")
            continue # ignore todo lo que viene después en el ciclo actual y vuelva a preguntar por las coordenadas(i, j) desde el principio.
        
        if 0 <= i < 10 and 0 <= j < 10:
            print(f"Coordenadas válidas ingresadas: ({i}, {j})")
            return (i, j)