#programa cine 02
import os
#declara
nombre=""
numero_de_asiento=0

#Input via os
nombre=os.sys.argv[1]
numero_de_asiento=int(os.sys.argv[2])

#processing
#si el numero de asientos supera a 5
#mostrar "ganaste un caramelo"
if(numero_de_asiento>=5):

#output
  print(nombre,"ganaste un caja de cancha!")
