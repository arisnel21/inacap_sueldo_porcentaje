sueBase = float(input("Ingrese el sueldo base del trabajador: "))
ventas = int(input("Ingrese cantidad de ventas realizadas: "))
comision = 0
if ventas >= 3 :
    comision = sueBase * 0.1
    totalVenta = sueBase + comision
    print("El total de sueldo obtenido este mes por las 3 ventas realizadas es de: ",totalVenta)  
else: 
    print("No lograste las 3 ventas asi que no ganaste comision este mes tu sueldo base es: ",sueBase)


  
