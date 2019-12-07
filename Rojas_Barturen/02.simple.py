#programa ganar tikets del cine
import os
#declara
nomnbre=""
producto=""
cantidad=0

#Input via os
nombre=os.sys.argv[1]
producto=os.sys.argv[2]
cantidad=int(os.sys.argv[3])

#prosecing
#si el numero de producto supera a 50
#mostrar "ganaste un producto adicional"
if(producto>50):
    print(nombre,"ganaste un producto adicional")
