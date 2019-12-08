#programa ganar tikets del cine
import os
#declarar
nomnbre=""
numero_tikets=0

#Input via os
nombre=os.sys.argv[1]
numero_tikets=int(os.sys.argv[2])

#prosecing
#si el numero de tikets supera a 50
#mostrar "ganaste una entrada adicional"
if(numero_tikets>50):
    print(nombre,"ganaste una entrada adicional")
else:
    print(nombre,"sigue acumulando tikets")
#fin_if
