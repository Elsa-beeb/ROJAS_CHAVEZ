#programa productos adicionales
#declarar
import os
#declara
nomnbre=""
producto=""
cantidad=0

#Input via os
nombre=os.sys.argv[1]
producto=os.sys.argv[2]
cantidad=(int(os.sys.argv[3]))

#prosecing
#si el numero de producto supera a 10
#mostrar "ganaste un producto adicional"
if(cantidad>10):
    print(nombre,"ganaste un producto adicional")
else:
    print(nombre,"sigue intentando gracias")
