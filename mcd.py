#Escriba una función que reciba dos numeros y retorne el cálculo de su máximo común divisor.
def mcd(a,b):
    if b == 0:
        return a
    else:
        return mcd(b, a%b)
dato1 = int(input("Ingrese el primer : "))
dato2 = int(input("Ingrese el segundo valor: "))
print(str(mcd(dato1,dato2)))



