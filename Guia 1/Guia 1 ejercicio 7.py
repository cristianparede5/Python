#Enunciado
#7. Conversión de medidas. Desarrolle un programa para convertir una medida dada en pies a sus equivalentes
#en: yardas pulgadas cenơmetros metros Sabiendo que: 1 pie = 12 pulgadas 
#1 yarda = 3 pies 1 pulgada = 2.54 centímetros 1 metro = 100 centimeros

#Declaramos Variables

pie=int();
yarda=int();
pulgada=int();
centimetros=float();
metro=int();

#Inicializamos las variables

pie=0;
yarda=0;
pulgada=0;
centimetros=0;
metro=0;

#Codigo

pie=int(input("Diga cual es la medida en pie: "))

pulgada= pie*12;
yarda= pie/3;
centimetros= pulgada*2.54;
metro= centimetros/100;

print("La medida a pie que puso es de: ",pie)
print("En pulgada seria: ",pulgada)
print("En yarda seria: ",yarda)
print("En centimetros seria: ",centimetros)
print("Y en metros seria: ",metro)

#PRUEBA DE ESCRITORIO

#ENTRADA
#Diga cual es la medida en pie: 8

#SALIDA
#La medida a pie que puso es de: 8
#En pulgada seria: 96
#En yarda seria: 2.66
#En centimetros seria: 243.84
#Y en metros seria: 2.4384

#PROCESO DEL CODIGO

#pie=0          | pie=8
#yarda=0        | yarda=2.66
#pulgada=0      | pulgada=96
#centimetros=0  | centimetros=243.84
#metro=0        | metros=2.4384