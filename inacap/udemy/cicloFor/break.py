contador = 0 
for letra in 'Holanda':
    if letra == 'a':
        contador+=1
        print(f'letra encontrada {letra} y se entro {contador} veces')
        break # esto hace que una vez se encuentre la letra a rompa el ciclo 
              # para mostrar asi el resultado
else: 
    print('Fin ciclo for')