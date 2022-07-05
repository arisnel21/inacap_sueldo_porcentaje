import numpy as np
resultado = 0
promedio = 0 
value_max = 0
longitud = 10 
arreglo = np.empty(longitud,dtype=int)

for i in range(longitud):
    arreglo[i]=(input("Ingrese un valor: "))
    
    resultado = (resultado + arreglo[i])
value_max = max(arreglo)
promedio+= resultado/3

if arreglo[i] > promedio:
    print(f'el numero mayor al promedio es: {arreglo[i]}')
else: 
    print("No existen numeros mayores al promedio!!")

print(f'el valor maximo ingresado es: {value_max}')
print(f'el arreglo -> {arreglo}')
print(f'El resultado de la sumatoria de los elementos es: {resultado}')
print(f'El promedio de los valores es: {promedio}')
