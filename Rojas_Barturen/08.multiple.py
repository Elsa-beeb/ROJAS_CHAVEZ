#programa obtener un credito bancario
import os
#declarar
nomnbre=""
ingreso_mensual=0.0

#Input via os
nombre=os.sys.argv[1]
ingreso_mensual=(float(os.sys.argv[2]))

#prosecing
#si el ingreso mensual es mayor a 1500
#mostrar "el prestamo fue aprobado"
if(ingreso_mensual>1500):
    print("señor(a):",nombre,"el prestamo fue aprobado")
if(ingreso_mensual<=1500):
    print("señor(a):",nombre,"le podemos otorgar una tarjeta de credito")
