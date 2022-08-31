#1 - División con resto Plantear un algoritmo que permita informar, para dos valores a y b el resultado de la división a/b y el resto de esa división.

#Declaración de Variables
numeroA=float()
numeroB=float()

#Inicialización de Variables
numeroA=0.0;
numeroB=0.0;

#Codigo
#Números 'A' y 'B' a dividir
numeroA=float(input('Diga el número ''A'' a dividir:'))
numeroB=float(input('Diga en número ''B'' a dividir:'))

#Cuenta
division=numeroA/numeroB;
resto=numeroA%numeroB;

#Se muestra por pantalla el resultado de la division y el resto
print('El resultado es: ',division)
print('El resto es: ', resto)
