#programa obtener una bonificacion por venta de unique
import os
#declarar
nomnbre=""
monto=0.0

#Input via os
nombre=os.sys.argv[1]
monto=(float(os.sys.argv[2]))

#prosecing
#si el monto es mayor a 350
#mostrar "ganaste una licuadora"
if(monto>350):
    print(nombre,"ganaste una licuadora")
if(monto<=350):
    print(nombre,"ganaste un kid de limpieza facial")
