#1. Desarrolle un programa que pase un peso de kilogramo a libras teniendo en cuenta que cada kilogramo equivale a 2.2 libras.

kilogramo=float()
libra=float()

kilogramo=2.2;
libra=0.0;

pregunta=float(input('Cuantos Kilogramos quiere pasar a libras:'))

libra=pregunta*kilogramo;

print(str(pregunta)+ ' kilogramos equivale a '+ str(libra)+ ' libras.')