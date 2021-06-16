from pila import Pila
from random import randint

class Personaje (object):
        nombre, cant_peliculas = '' , int
        
        def __init__(self, nombre, cant_peliculas):
            self.nombre = nombre
            self.cant_peliculas = cant_peliculas
        
        def __str__(self):
            return self.nombre + '-' +self.cant_peliculas

personaje = Pila()

dato = Personaje ('iron man', 6)
personaje.apilar(dato)
dato = Personaje ('capitan america', 5)
personaje.apilar(dato)
dato = Personaje ('hulk', 9)
personaje.apilar(dato)
dato = Personaje ('hormiga', 3)
personaje.apilar(dato)
dato = Personaje ('black widow', 4)
personaje.apilar(dato)
dato = Personaje ('groot', 5)
personaje.apilar(dato)
dato = Personaje ('rocket raccoonn', 5)
personaje.apilar(dato)
dato = Personaje ('thor', 6)
personaje.apilar(dato)
dato = Personaje ('pantera', 3)
personaje.apilar(dato)
dato = Personaje ('fury', 20)
personaje.apilar(dato)
dato = Personaje ('thanos', 2)
personaje.apilar(dato)
dato = Personaje ('ford falcon', 1)
personaje.apilar(dato)


cont_posicion = 0  

while (not personaje.pila_vacia()):
    x = personaje.desapilar()
    cont_posicion = cont_posicion + 1

    if (x.nombre == 'rocket raccoonn'):
        print ('rocket raccoonn esta en la posicion ' + str(cont_posicion))
    if (x.nombre == 'groot'):
        print ('groot esta en la posicion ' + str(cont_posicion)) 

    if (x.cant_peliculas >= 5):
        print (x.nombre + ', participo en mas de 5 peliculas. En total: ' + str(x.cant_peliculas))   

    if (x.nombre == 'black widow'):
        print ('black widow participo en ' + str(x.cant_peliculas) + ' peliculas' )

    if (x.nombre[0] == 'c' or x.nombre[0] == 'd' or x.nombre[0] == 'g'):
        print ('personaje comenzado con letra c,d o g ')