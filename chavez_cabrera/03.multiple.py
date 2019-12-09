#programa 03
import os
#declara
nombre_de_evento=""
nro_de_invitados=0

#Input via os
nombre_de_evento=(os.sys.argv[1])
nro_de_invitados=int(os.sys.argv[2])

#processing
#el numero de invitados supera los 100
#mostrar "buena organizacion del evento"
if ( nro_de_invitados> 100):
    print("buena organizacion del evento")
if ( nro_de_invitados<=100):
    print("mala organizacion del evento")
