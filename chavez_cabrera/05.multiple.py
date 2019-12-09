#programa 05
import os
#declara
paracetamol=0.0
diclofenaco=0.0
doloneurobion=0.0
redex=0.0
grabol=0.0
prom=0.0

#input via os
paracetamol=float(os.sys.argv[1])
diclofenaco=float(os.sys.argv[2])
doloneurobion=float(os.sys.argv[3])
redex=float(os.sys.argv[4])
grabol=float(os.sys.argv[5])

#processing
prom=float(round((paracetamol+diclofenaco+doloneurobion+redex+grabol)/5,0))

#condicion  multiple
#si el prom => 90 y 120 (very good)
if(prom>=95 and prom<=100):
    print("very good!")
#si el prom es 90 y 94
if(prom>=90 and prom<=94):
    print("good!")

