#número primo es un número entero que solamente es divisible por él mismo
def primo(numero):
    for i in range(2,numero):
        if numero%i==0:
            return (print("El número no es primo"))
    return (print("El número es primo"))



dato= int( input("Ingrese el número a evaluar: "))
primo(dato)



