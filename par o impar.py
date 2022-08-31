#2. Escribir un programa que pregunte un nombre de usuario, y que después muestre por pantalla si su cantidad de letras es par o impar.
#     
#    | Entrada | Salida |
#    | --- | --- |
#    | camilo | par |
#    | sol | impar |

#Declaramos Variables

pregunta=str()
res=str()

#Inicialización de Variables

pregunta='  '
res='  '

#Codigo

pregunta=input('Diga lo primero que se le venga a la mente:')
res=len(pregunta)
if res % 2 == 0:
    print('Esta palabra contiene: ',res,' letras')
    print('ES PAR!')
else:
    print('Esta palabra contiene: ',res,' letras')
    print('ES IMPAR!')    