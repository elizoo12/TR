#EL OBJETIVO DE ESTE ARCHIVO ES SER EL QUE SE EJECUTARA, OSEA, todo EL CODIGO VENDRA A PARAR AQUI.

#------imports------
from main import Jugar

modo = input("si quieres jugar contra el ordenador pulsa 1, si quieres jugar un amigo pulsa 2: ")

valido=False
while valido==False:
    if modo == "1":
     valido=True
     Jugar()
    elif modo == "2":
     valido=True   
     
    else:
     modo= input("valor invalido, pulsa 1 para jugar con un ordenador o 2 para jugar con un amigo: ")