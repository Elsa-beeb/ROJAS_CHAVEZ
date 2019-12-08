#programa obtener una beca
import os
#declarar
nomnbre=""
promedio_ponderado=0.0

#Input via os
nombre=os.sys.argv[1]
promedio_ponderado=(float(os.sys.argv[2]))

#prosecing
#si el promedio ponderado es mayo a 16
#mostrar "ganaste una beca"
if(promedio_ponderado>16):
    print(nombre,"ganaste una beca")
else:
    print(nombre,"no ganaste la beca, promedio ponderado bajo")
