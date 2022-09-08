#Declaramos Variables

base=int();
altura=int();
area=float();

#Inicializamos las Varibales

base=0;
altura=0;
area=0.0;

#Codigo

base=int(input("Diga de cuanto es la base: "))

altura= base**2;
area= base*altura/2;

print("El area del triangulo es de: ",area)

#PRUEBA DE ESCRITORIO  

#ENTRADA
#Diga de cuanto es la base: 30

#SALIDA:
#El area del triangulo es de: 13500.0

#PROCESO DEL CODIGO
# base=0    | base= 30
# altura=0  | altura= 900 | Da 900 porque se eleva al cuadrado la base y de ahi el resultado de la altura.
# area=0.0  | area= 13500.0