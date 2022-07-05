num = 1

while num <= 20:
    cont = 1 
    x = 0
    while cont <= num:
        if num % cont == 0:
            x = x + 1
        cont = cont + 1
    
    if x == 2 :
        print ( "El numero ",num," es primo")
    
    num = num + 1 