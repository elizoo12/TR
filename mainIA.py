##Importar todas las IA's programadas aqui y hacer una selecion entre todas

#------IMPORTS------


#------VARIABLES------
dificultad= input("seleciona una dificultad entre 1-3: ")
finbucle= False
#------EJECUCION------
while finbucle== False:
  if dificultad=="1":
    #ejecutar RANDOM
    print(1)
    finbucle= True
  elif dificultad=="2":
    #ejecutar METODO
    print(2)
    finbucle= True
  elif dificultad=="3":
    #ejecutar MINIMAX
    print(3)
    finbucle=True
  else:
    dificultad=input("dificultad invalida, seleciona un valor entre 1-3: ")
