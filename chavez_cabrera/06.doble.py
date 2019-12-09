#programa 06
import os
#declara
nombre_del_libro=""
nro_de_hojas=0

#Input via os
nombre_del_libro=(os.sys.argv[1])
nro_de_hojas=int(os.sys.argv[2])

#processing
#si el numero de hojas supera a 35
#mostrar "gratis anillado"
if(nro_de_hojas>20):
    print("gratis anillado")
else:
    print("pagar el anillado")
