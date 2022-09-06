#Declaracion de variables
pregunta=str();

#Inicializacion de variables
pregunta="        ";

pregunta=input("Diga cualquier cosa: ")

#La palabra se pone todo en mayuscula
pregunta_upper=pregunta.upper()

#La palabra se pone todo en minuscula
pregunta_lower=pregunta.lower()

#La palabra se pone la primera letra en mayuscula y el resto en minuscula
pregunta_capitalize=pregunta.capitalize()

#Aca se muestra por pantalla
print(pregunta_upper, pregunta_lower, pregunta_capitalize)

#Prueba de escritorio

#Entrada | Salida

#HamAcA  | HAMACA hamaca Hamaca
#caMiNo  | CAMINO camino Camino
#CristIan| CRISTIAN cristian Cristian 