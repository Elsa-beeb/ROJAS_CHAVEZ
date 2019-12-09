#programa subir de nivel en un video juego
import os
#declarar
nomnbre=""
puntaje=0

#Input via os
nombre=os.sys.argv[1]
puntaje=(int(os.sys.argv[2]))

#prosecing
#si el puntaje es mayor a 50
#mostrar "subiste de nivel"
if(puntaje>50):
    print(nombre,"subiste de nivel")
if(puntaje<=50):
    print(nombre,"le falta puntaje")
