"""
C)	Ingresar n números y al finalizar desplegar cuantos números fueron mayores y cuantos menores al primer 
número ingresado."""
canNum = int(input("Ingrese cantidad de numeros a evaluar: "))
nu = 0
x = 0
menor = 0
mayores = 0
primer = 0
while x < canNum:
    x = x + 1
    nu = int(input("ingrese los numeros: "))
    if nu == 0 :
        print("ingrese un numero valido")
        x= x-1 
    else: 
        if x == 1:
            primer = nu
        if nu > primer:
            mayores = mayores +1
        else:
            menor = menor + 1

print("primer numero es:",primer," y hay:" ,mayores, "numeros mayores")
print("primer numero es:",primer," y hay:" ,menor-1, "numeros menores")