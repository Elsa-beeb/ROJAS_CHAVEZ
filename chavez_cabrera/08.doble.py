#programa 08
import os
#declara
direccion=""
nro_de_casas=0
#Input via os
direccion=(os.sys.argv[1])
nro_de_casas=int(os.sys.argv[2])

#processing
#si el numero de casas supera a 85
#mostrar "gratis bonificacion de la casa propia"
if(nro_de_casas<85):
    print("gratis bonificacion de la casa propia")
else:
    print("no alcanza el rango de casas")
