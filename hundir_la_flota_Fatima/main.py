from tablero import *
from jugador import pedir_coordenadas
from disparo import  disparar
from vidas import quedan_barcos
import random #para la maquina haga disparos aleatorios.
import time #para hacer pausas entre turnos.

# Turno JUGADOR & MAQUINA:

es_turno_jugador = True #variable booleana que indica si el turno es del jugador.
print("Empieza el juego de hundir la flota!")
while True: #bucle del juego, se repite hasta que termine.
    turno= ""
    if es_turno_jugador:
        tablero_atacante = tablero_jugador # tablero desde el que dispara el jugador.
        tablero_defensor = tablero_maquina # tablero que recibe el disparo.
        i, j = pedir_coordenadas() # pide ambas coordenadas a la vez.
        turno= "Jugador"
    else:
        tablero_atacante = tablero_maquina
        tablero_defensor = tablero_jugador
        turno="Maquina"
        while True: #bucle para asegurarme que la maquina no repita disparos.
            i, j = random.randint(0,9), random.randint(0,9) #coordenadas aleatorias(0,9)
            if tablero_defensor[i][j] not in [ "X", "O"]: # con este if evito que la máquina repita disparos.
                break # sale del bucle si la celda esta vacia.
        print(f"maquina dispara en coordenadas:{i}, {j}")
        
    #disparo
    resultado= disparar(tablero_defensor, i, j) # llamo a la función disparar, y me guarda si fue acierto(True) o agua(False).
    
    #Mostrar tablero despues del disparo
    print("\n Tablero del Jugador")
    mostrar_tablero(tablero_jugador)
    
    print("\n Tablero de la maquina")
    mostrar_tablero(tablero_maquina)
    
    # print("1tablero de", turno)
    # mostrar_tablero(tablero_defensor)
    if resultado: # repite turno si acierta el disparo.
        print("vuelve a disparar")
        continue # vuelve al inicio del while para repetir turno.
    else: 
        # Si da agua, turno termina
        print("Turno terminado, siguiente disparo.")
        time.sleep(2)  # pausa de 2 segundos
        es_turno_jugador = not es_turno_jugador # esto lo pongo para cambiar de turno.
           
    # añado condicion para comprobar fin del juego, SI NO PONGO ESTO EL BUCLE NO TERMINA NUNCA..
    if not quedan_barcos(tablero_jugador):
        print(" La maquina ha ganado :(")
        break ## Termina el bucle y el juego.
    if not quedan_barcos(tablero_maquina):
        print("jugadora Fatima ha ganado!!")
        break  
    
#Mostrar tablero del jugador y de la maquina con los resultados finales.  
print("Tablero jugador:")
mostrar_tablero(tablero_jugador)
  
print("Tablero máquina:")
mostrar_tablero(tablero_maquina)     
  