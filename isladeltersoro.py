jugador = input ("Bienvenidos a la isla del tesoro tu mision sera encontrar el tesoro, ¿cúal es tu nombre? ")
opc1 = input("¿escoges el camino de la derecha  o izquierda? ") # primera opción
opc1 = opc1.lower()


if(opc1== "derecha"):
    print("caiste en un agujero game over ") # primera opción

elif(opc1== "izquierda"): # primera opción
    print("Siguiente nivel") # primera opción
    opc2 = input("¿escoges el camino nadar  o esperar? ") # 2da opción
    opc2 = opc2.lower()

    if( opc2 == "nadar"): # 2da opción
        print("caiste en un agujero game over")
    elif (opc2=="esperar"):  # 2da opción 
        print("Siguiente nivel") # 2da opción
        opc3 = input("¿Camino de arañas o de serpientes? ") # 3ra opción
        opc3 = opc3.lower()

        if ( opc3 == "serpientes"): # 3ra opción
            print("Una serpiente te enveneno GAME OVER") # 3ra opción
        elif( opc3 =="arañas"): # 3ra opción
            print("Siguiente nivel")# 3ra opción3ta opción
            opc4 = input("¿Acabas de ver osos cerca. ¿Prefieres correr o caminar? ") # 4ta opción
            opc4 = opc4.lower()

            if ( opc4 == "correr"): # 3ta opción
                print("El oso corre detrás de ti y te atrapa GAME OVER")
            elif(opc4=="caminar"):
                print("pasaste al siguiente nivel")
                opc5 = input("¿playa, bosque o mar? ")
                opc5 = opc5.lower()
                if(opc5== "playa"):
                    print("Un coco te cayó encima GAME OVER")
                elif(opc5=="mar"):
                    print("Bebiste agua salada y te deshidrataste")
                elif(opc5=="bosque"):
                    print("siguiente nivel")
                    opc6=input("¿prefieres comida, dormir o fogata? ")
                    opc6 = opc6.lower()
                    if(opc6=="comida"):
                        print("Se hizo de noche y te dio hipotermia GAME OVER")
                    elif(opc6=="dormir"):
                        print("Se hizo de noche y  un lobo te atacó GAME OVER")
                    elif(opc6=="fogata"):
                        print("pasas a siguiente nivel")
                        opc7=input("se acerrcan los piratas ¿nadar o esconderse? ")
                        opc7 = opc7.lower()
                        if(opc7=="nadar"):
                            print("Atacado por los piratas GAME OVER")
                        elif(opc7=="esconderse"):
                            print("pasas al siguiente nivel")
                            opc8=input("¿Cual puerta escoges roja, amarillo o azul? ")
                            opc8 = opc8.lower()
                            if(opc8=="roja"):
                                print("Eres quemado GAME OVER")
                            elif(opc8=="amarillo"):
                                print("Devorado por bestias GAME OVER")
                            elif (opc8=="azul"):
                             print("Sobreviviste, "+ str(jugador) + " el tesoro es tuyo")
                            else:
                                    print ("Escribiste mal, verifica" )