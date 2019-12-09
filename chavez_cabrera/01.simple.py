#programa de salario de un empleado 01
import os
#declara
horas=0
precio=0

#input via os
horas=int(os.sys.argv[1])
precio=float(os.sys.argv[2])

#processing
pago=(horas*precio)

#output
print(pago,"sueldo final")
