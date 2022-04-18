sueldo = int ( input("Ingrese sueldo del trabajador: "))
mesesAnti = int (input("ingrese meses de antiguedad: "))

anoAntiguedad =  int (mesesAnti * 0.084) 


if sueldo >= 500000 or anoAntiguedad >= 2 :
    
    sueldoReajustado = int (sueldo * 0.1)+sueldo
    reajuste = int(sueldo * 0.1)
    print("El sueldo ingresado es:", sueldo ,"\n",
         "El reajuste de sueldo es:", reajuste,"\n",
         "El sueldo reajustado es:",sueldoReajustado,"\n",
         "La cantidad de años de antiguedad es:",anoAntiguedad
        )
else: 
    print("No cumple los requisitos para un reajuste de sueldo. ")
    