#------OBJETIVOS------
#cambiar metodo jugada
#introducir discriminacion al ordenador
#hacer cambio entre jugador y ordenador
#crear metodo aleatorio

import random


# --------- variables goblales -----------

# esto es la matriz donde trabajaremos, en este caso tan solo es una tupla
Tablero = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

TableroImaginario=["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]

# Esta variable indicara si el juego debe seguir o ha finalizado
el_juego_funciona = True

# Esta variable nos indicara quien es el ganador si lo hay, sino permanecera en estado None
Ganador = None
GanadorImaginario = None
#  Esta variable indica de quien es el turno, de forma predeterminada empezaran las cruces 
jugador_humano="X"
ordenador="O"
Jugador_del_Turno = jugador_humano
# ------------- funciones ---------------

# Jugar al 3 en ralla
def Jugar():

  # reiniciar el tablero
  MostrarTablero()

  # bucle principal, el bucle cerrara cuando haya ganador o tablas
  while el_juego_funciona:

    #Jugada de cada jugador
    #*************
    Jugada(Jugador_del_Turno)

    # comprobamos victoria y empate
    Comprobar_fin_juego()

    # cambiamos de X a O y viceversa
    Cambiar_jugador()
  
  # Cuando el bucle principal termina indicamos quien ha ganado
  if Ganador == "X" or Ganador == "O":
    print(Ganador + " ha ganado. ")
  elif Ganador == None:
    print("Tablas.")


# aqui mostramos el tablero de pantalla, en un lado tendremos nuestro propio tablero y en el otro una indicacion numerica
def MostrarTablero():
  print("\n")
  print(" " +  Tablero[0] + " | " + Tablero [1] + " | " + Tablero[2]    +"            1|2|3")
  print("------------" +                                                 "          -----")
  print(" " +  Tablero[3] + " | " + Tablero [4] + " | " + Tablero[5]    +"            4|5|6")
  print("------------" +                                                 "          -----")
  print(" " +  Tablero[6] + " | " + Tablero [7] + " | " + Tablero[8]    +"            7|8|9")
  print("\n")


# funcion usada para las jugadas, ambos jugadores comparten funcion
def Jugada(Jugador):

    if Jugador=="X":
        jugada_humana()
    elif Jugador=="O":
        jugada_ordenador()


def jugada_ordenador():
    #tramemos las variables globales.
    global GanadorImaginario
    contador=0
    print("es turno del ordenador ")
    for i in range(1,9):
        TableroImaginario=Tablero
        posicionImaginaria= i
        posicionImaginaria=int(posicionImaginaria)
        posicionImaginaria-=1
        if TableroImaginario[posicionImaginaria]== "-":
            TableroImaginario[posicionImaginaria]="O"
            comprobar_victoria_imaginaria()
            if GanadorImaginario== "O":
                Tablero[posicionImaginaria]="O"
                contador=1
                break
            else:
                pass

        else:
            pass
    if contador==0:
        valido=False
        while not valido:
            posicion= random.randint(1,9)
            posicion= int(posicion) -1
             # Nos aseguramos que se coloca en una casilla no escogida previamente
            if Tablero[posicion] == "-":
             valido = True
            else:
             print("El ordenador esta pensando ")
    return


def jugada_humana():
    # pedimos una jugada
  print("es el turno del Jugador ")
  posicion = input("elige una casilla entre 1-9: ")

  # valido sera un valor para generar un bucle que solo se abrira cuando se de una jugada valida
  valido = False
  while not valido:

    # Nos aseguramos de que juegan dentro del tablero
    while posicion not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      posicion = input("Input invalido. elige una casilla entre 1-9: ")
 
    # corregimos la posicion para que el ordenador la entienda
    posicion = int(posicion) - 1

    # Nos aseguramos que se coloca en una casilla no escogida previamente
    if Tablero[posicion] == "-":
      valido = True
    else:
      print("casilla ocupada, piensa otra opcion. ")

  # colocamos la pieza en nuestra "matriz"
  Tablero[posicion] = "X"

  # refrescamos el tablero con la nueva jugada
  MostrarTablero()

# funcion para comprobar el final de juego
def Comprobar_fin_juego():
  comprobar_victoria()
  comprobar_tablas()


# funcion para comrpobar si hay una victoria
def comprobar_victoria():
  # Set global variables
  global Ganador
  # traemos las variables globales necesarias
  ganador_fila = comprobar_filas()
  ganador_columna = comprobar_columnas()
  ganador_diagonal = comprobar_diagonales()
  # Obtenemos el jugador victorioso
  if ganador_fila:
    Ganador = ganador_fila
  elif ganador_columna:
    Ganador = ganador_columna
  elif ganador_diagonal:
    Ganador = ganador_diagonal
  else:
    Ganador = None


# comprobacion de cada fila
def comprobar_filas():
  # traemos las variables globales necesarias
  global el_juego_funciona
  # comprobamos que todos los valores en una fila sean iguales y no esten vacios
  fila_1 =Tablero[0] ==Tablero[1] ==Tablero[2] != "-"
  fila_2 =Tablero[3] ==Tablero[4] ==Tablero[5] != "-"
  fila_3 =Tablero[6] ==Tablero[7] ==Tablero[8] != "-"
  # si hay linea hay victoria
  if fila_1 or fila_2 or fila_3:
    el_juego_funciona = False
  # obtenemos el ganador
  if fila_1:
    return Tablero[0] 
  elif fila_2:
    return Tablero[3] 
  elif fila_3:
    return Tablero[6] 
  # seguimos el codigo si no hay fila
  else:
    return None


# comprobamos las columnas para ganar
def comprobar_columnas():
  # traemos las variables globales necesarias
  global el_juego_funciona
  # comprobamos que tienen el mismo valor y no estan vacias
  columna_1 =Tablero[0] ==Tablero[3] ==Tablero[6] != "-"
  columna_2 =Tablero[1] ==Tablero[4] ==Tablero[7] != "-"
  columna_3 =Tablero[2] ==Tablero[5] ==Tablero[8] != "-"
  # si hay columna hay victoria
  if columna_1 or columna_2 or columna_3:
    el_juego_funciona = False
  #  obtenemos el ganador
  if columna_1:
     return Tablero[0] 
  elif columna_2:
    return Tablero[1] 
  elif columna_3:
    return Tablero[2] 
  # seguimos el codigo si no hay columna
  else:
    return None


# comprobamos las diagonales para ganar
def comprobar_diagonales():
  # traemos las variables globales necesarias
  global el_juego_funciona
  # comprobamos que tengan el mismo valor y no sea vacio
  diagonal_1 =Tablero[0] ==Tablero[4] ==Tablero[8] != "-"
  diagonal_2 =Tablero[2] ==Tablero[4] ==Tablero[6] != "-"
  # si hay diagonal hay victoria
  if diagonal_1 or diagonal_2:
    el_juego_funciona = False
  # obtenemos el ganador
  if diagonal_1:
    return Tablero[0] 
  elif diagonal_2:
    return Tablero[2]
  #continuamos el codigo
  else:
    return None


# funcion para comprobar si hay tablas
def comprobar_tablas():
  # traemos las variables globales necesarias
  global el_juego_funciona
  # si el tablero esta lleno hay tablas
  if "-" not in Tablero:
    el_juego_funciona = False
    return True
  # De otra forma no hay tablas
  else:
    return False


def comprobar_victoria_imaginaria():
    Ganador_fila_imaginaria = comprobar_filas_imaginarias()
    Ganador_columna_imaginaria = comprobar_columnas_imaginarias()
    Ganador_diagonal_imaginaria = comprobar_diagonales_imaginarias()

    if Ganador_fila_imaginaria:
      GanadorImaginario = "O"
    elif Ganador_columna_imaginaria:
     GanadorImaginario = "O"
    elif Ganador_diagonal_imaginaria:
      GanadorImaginario = "O"
    else:
      GanadorImaginario = None
    return GanadorImaginario



def comprobar_filas_imaginarias():
 # comprobamos que todos los valores en una fila sean iguales y no esten vacios
  fila_1imaginaria =TableroImaginario[0] ==TableroImaginario[1] ==TableroImaginario[2] != "-"
  fila_2imaginaria =TableroImaginario[3] ==TableroImaginario[4] ==TableroImaginario[5] != "-"
  fila_3imaginaria =TableroImaginario[6] ==TableroImaginario[7] ==TableroImaginario[8] != "-"
  # obtenemos el ganador
  if fila_1imaginaria:
    return TableroImaginario[0] 
  elif fila_2imaginaria:
    return TableroImaginario[3] 
  elif fila_3imaginaria:
    return TableroImaginario[6] 
  # seguimos el codigo si no hay fila
  else:
    return None

def comprobar_columnas_imaginarias():
    # comprobamos que tienen el mismo valor y no estan vacias
  columna_1imaginaria =TableroImaginario[0] ==TableroImaginario[3] ==TableroImaginario[6] != "-"
  columna_2imaginaria =TableroImaginario[1] ==TableroImaginario[4] ==TableroImaginario[7] != "-"
  columna_3imaginaria =TableroImaginario[2] ==TableroImaginario[5] ==TableroImaginario[8] != "-"

  #  obtenemos el ganador
  if columna_1imaginaria:
     return TableroImaginario[0] 
  elif columna_2imaginaria:
    return TableroImaginario[1] 
  elif columna_3imaginaria:
    return TableroImaginario[2] 
  # seguimos el codigo si no hay columna
  else:
    return None

def comprobar_diagonales_imaginarias():
    # comprobamos que tengan el mismo valor y no sea vacio
  diagonal_1imaginaria =TableroImaginario[0] ==TableroImaginario[4] ==TableroImaginario[8] != "-"
  diagonal_2imaginaria =TableroImaginario[2] ==TableroImaginario[4] ==TableroImaginario[6] != "-"

  # obtenemos el ganador
  if diagonal_1imaginaria:
    return TableroImaginario[0] 
  elif diagonal_2imaginaria:
    return TableroImaginario[2]
  #continuamos el codigo
  else:
    return None

#  funcion para cambiar jugador en cada turno
def Cambiar_jugador():
  # traemos las variables globales necesarias
  global Jugador_del_Turno
  #si el jugador es X pasamos a O
  if Jugador_del_Turno == jugador_humano:
    Jugador_del_Turno = ordenador
  #  si el jugador es O pasamos a X
  elif Jugador_del_Turno == ordenador:
    Jugador_del_Turno = jugador_humano

Jugar()

input("pulsa enter para terminar el juego")