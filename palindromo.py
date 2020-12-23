#Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda.
def palindromo(texto):
    textoalreves= texto[::-1]
    if (texto == textoalreves):
        print("La entrada es un palíndromo")
    else:
        print("La entrada no es un palíndromo")
dato= input("Ingrese la palabra o numero que desea saber si es o no palíndromo")
palindromo(dato)



