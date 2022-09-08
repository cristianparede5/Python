#Enunciado

#Últimos dígitos ¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número
#entero? ¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número entero 
#por teclado, y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado).

#Declaramos variables

numero=int();

#Inicializacion de variable

numero=0;

#codigo

numero=int(input("Diga un numero: "))

print("El ultimo dijito es: ",(numero%10))
print("Y sus dos ultimos dijitos son: ",(numero%100))

#PRUEBA DE ESCRITORIO

#ENTRADA

#Diga un numero: 218

#SALIDA

#El ultimo dijito es: 8
#Y sus dos ultimos dijitos son: 18

#PROCESO DEL CODIGO

# Numero=0     | Numero=218