#programa 06
import os
#declara
precio=0.0
iva=0.0

#Input via os
precio=float(os.sys.argv[1])
iva=float(os.sys.argv[2])

#processing
#si el iva es menor a 60
#mostrar "no paga impuesto"
total_de_iva=(precio*iva)
if(iva<60):
#output
 print("no pagas el impuesto del iva:",total_de_iva)
