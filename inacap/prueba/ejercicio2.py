"""B)	Desarrollo un programa que realice la siguiente serie hasta el 11(usando ciclos):
dos impares dos pares 
+1
-3
+2
-4
+5 
-7
+6
-8
+9
-11
------------
(resultado de la operatoria)
"""

x = 1
y = 2

res = 0

while x <= 11:
    if x % 2 != 0:
        print("+" + str(x))
        res = res + x
        x = x + 2
        print("-" + str(x))
        res = res - x

    else:
        print("+" + str(y))
        res = res + y
        y = y + 2
        print("-" + str(y))
        res = res - y
        y = y + 2

    x = x + 1
print("Resultado: ", res)

