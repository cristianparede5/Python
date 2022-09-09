#Enunciado

#Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar.

#Declaración de variables

fib=list()
n=int()

#Inicializacion de variables

n=0;

#Codigo

def fib(n):
    fib = [0, 1]

    if (n <= 0): return "Numero fuera de rango"
    if (n == 1): return 0
    if (n == 2): return fib

    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

    return fib

n = int(input("¿Cuantos numeros desea ver de la secuencia de fibonacci?: "))
print(fib(n))

#Prueba de escritorio

#ENTRADA                                 
#¿Cuantos numeros desea ver de la secuencia de fibonacci?: 10

#SALIDA

#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#PROCESO DEL CODIGO
# n = 0 | 10