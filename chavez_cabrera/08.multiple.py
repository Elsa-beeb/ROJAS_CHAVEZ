#programa 08
import os
#declara
nombre=""
nro_de_cajas=0
#Input via os
nombre=(os.sys.argv[1])
nro_de_cajas=int(os.sys.argv[2])

#processing
#si el numero de casas supera a 85
#mostrar "gratis bonificacion de la casa propia"
if(nro_de_cajas>73):
    print("de regalo una caja mas")
if(nro_de_cajas<=73):
    print("no alcanzo el limite")
