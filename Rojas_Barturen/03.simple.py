#programa ganar una tasa
import os
#declarar
nombre=""
total_compra=0.0

#Input via os
nombre=(os.sys.argv[1])
total_compra=float(os.sys.argv[2])

#prosecing
#si el total_compra supera a 100
#mostrar "ganaste una tasa"
if(total_compra>100):
    print(nombre,"ganaste una tasa")
