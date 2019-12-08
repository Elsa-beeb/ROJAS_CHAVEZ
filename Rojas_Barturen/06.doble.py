#programa para ganar puntos
import os
#declarar
nomnbre=""
calificacion=0.0

#Input via os
nombre=os.sys.argv[1]
calificacion=(float(os.sys.argv[2]))

#prosecing
#si la calificacion es mayor a 10.5
#mostrar "ganaste puntos por obtener calificacion aprobatoria"
if(calificacion>10.5):
    print(nombre,"ganaste puntos por obtener calificacion aprobatoria")
else:
    print(nombre,"no ganaste puntos por tener calificación desaprobatoria")
