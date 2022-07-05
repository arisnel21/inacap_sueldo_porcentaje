cantYear = 1
year = 0
contMen = 0
contAd = 0
contVie = 0
cantErr = 0

while cantYear <= 5:
    year = int(input("ingrese edad a evaluar "))
    if year <= 0 :
        print("ingrese un numero valido !!")
        cantErr += 1
    elif year<18:
        contMen +=1
    elif year >=18 and year <=60:
        contAd += 1
    elif year >60 and year <= 130:
        contVie += 1



    cantYear = cantYear + 1

print("La cantidad de menores de edad es: ",contMen)
print("la cantidad de adultos es: ",contAd)
print("la cantidad de Viejitos es: ",contVie)
print("Ingresaste mal: ",cantErr," Edades")