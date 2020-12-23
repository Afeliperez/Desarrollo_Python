#Escriba una función que reciba un numero y retorne como resultado el numero romano de dicho número.
def romano(valor):
    numeros=[1000, 900, 500,400,100,90,50,40,10,9,5,4,1]
    letras=['M','CM','D','CD', 'C','XC','L','XL','X','IX','V','IV','I']

    numeral =""
    i=0

    while valor>0:
        for _ in range(valor // numeros[i]):
            numeral +=letras[i]
            valor -=numeros[i]
        i +=1
    return numeral
dato = int(input("Ingrese un numero para convertir a romano: "))

print(romano(dato))


