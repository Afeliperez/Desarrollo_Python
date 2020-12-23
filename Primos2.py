#Escriba una función que devuelva una lista de numeros primos con base a la cantidad que el usuario le solicite, Ejemplo si el usuario ingresa 3 debe retornar los 3 primeros numeros primos.
def primo():
    numero = 2
    yield   numero
    while True:
        temp = numero
        while True:
            temp +=1
            contador  =1
            divisor= 0
            while contador <= temp:
                if temp % contador == 0:
                    divisor +=1
                if divisor > 2:
                    break
                contador +=1
            if divisor ==2:
                yield temp
                numero  = temp
Nnumeros= int(input("ingrese la cantidad de numeros primos que desea ver: "))
g = primo()
primos = [next(g) for _ in range (Nnumeros)]
print(primos)


