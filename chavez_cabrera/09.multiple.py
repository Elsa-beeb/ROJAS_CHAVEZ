#programa 09
import os
#declara
nombre_de_clinica=""
nro_de_pecientes=0
#Input via os
nombre_de_clinica=(os.sys.argv[1])
nro_de_pecientes=int(os.sys.argv[2])

#processing
#si el numero de casas supera a 85
#mostrar "son atendidos en la mañana"
if(nro_de_pecientes<20):
    print("son atendidos en la mañana")
if(nro_de_pecientes>=20):
    print("son atendidos en la tarde")
