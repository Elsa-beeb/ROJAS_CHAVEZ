#programa ganar una tasa
import os
#declarar
nomnbre=""
total=0

#Input via os
nombre=os.sys.argv[1]
total_compa=(int(os.sys.argv[2]))

#prosecing
#si el total_compra supera a 100
#mostrar "ganaste una tasa"
if(total>100):
    print(nombre,"ganaste una tasa")
if(total<=100):
    print(nombre,"ganaste un lava bajilla")
