#programa para ganar una manzana confitada
import os
#declarar
nomnbre=""
cantidad=0

#Input via os
nombre=os.sys.argv[1]
cantidad=(int(os.sys.argv[2]))

#prosecing
#si la cantidad es mayos a 4
#mostrar "ganaste una manzana confitada"
if(cantidad>4):
    print(nombre,"ganaste una manzana confitada")
else:
    print(nombre,"gracias por su compra")
