"""A)	Un alumno desea saber si aprueba la asignatura, el promedio final se calcula de la siguiente manera:
	
	60% Proyecto semestral.
	40% Presentación e informes. 
	
El ingreso de datos debe permitir decimales (1 decimal), cada nota debe estar entre 1 y 7 de lo 
contrario enviar mensaje de error y volver a solicitar ingreso.
"""

nota1 = float(input("ingrese la nota final semestral: "))
preInformes = float(input("ingrese nota de presentaciones e informes: "))



if nota1 > 0 and nota1 <=7:
     nota1 = nota1*0.6
     print("su nota semestral promediada es: ",nota1)
else:
    print("Nota no valida")


if preInformes > 0 and preInformes <=7:
     preInformes = preInformes*0.4
     
     print("su nota semestral promediada es: ",preInformes)

print("la nota final es: ",(nota1+preInformes))


 

