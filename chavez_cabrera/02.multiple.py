#programa 02
import os
#declara
nombre=""
numero_de_paginas=0

#Input via os
nombre=(os.sys.argv[1])
numero_de_paginas=int(os.sys.argv[2])

#processing
#si el numero de paginas supera a 70
#mostrar "obtienes gratis portada"
if(numero_de_paginas>70):
    print(nombre,"obtienes gratis portada")
if(numero_de_paginas==70):
    print(nombre,"no alcanzo la promocion")
