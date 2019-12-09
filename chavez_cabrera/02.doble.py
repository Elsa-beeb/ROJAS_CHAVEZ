#programa 02
import os
#Declarar
Usuario=""
clave=""
Usuario=str(os.sys.argv[1])
clave=str(os.sys.argv[2])
#processing
#si la claves es de 4 digitos
#mostrar "acceso correcto"
if(clave=="1234"):
    print("Acceso correcto")
else:
    print("no es el usuario")
