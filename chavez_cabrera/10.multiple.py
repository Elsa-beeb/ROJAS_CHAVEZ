#programa 10
import os
#declara
primer_bimestre=0
segundo_bimestre=0
tercer_bimestre=0
cuarto_bimestre=0
prom=0

#input via os
primer_bimestre=int(os.sys.argv[1])
segundo_bimestre=int(os.sys.argv[2])
tercer_bimestre=int(os.sys.argv[3])
cuarto_bimestre=int(os.sys.argv[4])

#processing
prom=int(round((primer_bimestre+segundo_bimestre+tercer_bimestre+cuarto_bimestre)/4,0))

#condicion  multiple
#si el prom => 17 y 20 (very good)
if(prom>=17 and prom<=20):
    print("very good!")

#si el prom es 14 y 16
if(prom>=14 and prom<=16):
    print("good!")
