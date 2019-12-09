#programa 07
import os
#declara
nombre_del_solicitante=""
ano_de_inscripcion=0
#Input via os
nombre_del_solicitante=(os.sys.argv[1])
ano_de_inscripcion=int(os.sys.argv[2])

#processing
#si el numero de hojas supera a 35
#mostrar "gratis anillado"
if(ano_de_inscripcion<2030):
    print("no pagan inscripcion")
else:
    print("si pagan inscripcion")
