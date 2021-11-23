# 11. Dada una cola con personajes de la saga Star Wars,
# de los cuales se conoce su nombre y planeta 
# de origen. Desarrollar las funciones necesarias para resolver las siguientes
# actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks.

from cola import Cola
personaje = Cola()
cola_aux = Cola()

class informacion(object):
    nombre, planeta = '', ''

    def __init__(self, planeta, nombre):
            self.nombre = nombre
            self.planeta = planeta
          

    def __str__(self):
          return self.nombre+ '-. Planeta: '+ self.planeta



dato = informacion ('alderaan','jar jar binks')
personaje.arribo(dato)
dato = informacion ('endor','nick fury sinparche' )
personaje.arribo(dato)
dato = informacion ('tierra','luke skywalker')
personaje.arribo(dato)
dato = informacion ('alderaan', 'arturo')
personaje.arribo(dato)
dato = informacion ('desconocido','maestro yoda')
personaje.arribo(dato)
dato = informacion ('tatooine', 'droide')
personaje.arribo(dato)
dato = informacion ('tatooine','chiwi')
personaje.arribo(dato)
dato = informacion ( 'alderaan', 'el tenebroso')
personaje.arribo(dato)
dato = informacion ('tierra', 'han solo')
personaje.arribo(dato)

cantidad_elemento = 0
while (cantidad_elemento < personaje.tamanio()):
    dato = personaje.mover_final ()
    print (dato)
    cantidad_elemento += 1

print()

###Punto A
cantidad_elemento = 0
while (cantidad_elemento < personaje.tamanio()):
    dato = personaje.mover_final()
    if ((dato.planeta == 'alderaan') or (dato.planeta == 'endor') or (dato.planeta == 'tatooine')):

        print ('Personaje ', dato.nombre ,' del planeta ', dato.planeta)
   
    cantidad_elemento += 1

print ()

####Punto B
cantidad_elemento = 0
while (cantidad_elemento < personaje.tamanio()):
    dato = personaje.mover_final()
    if ((dato.nombre == 'han solo') or (dato.nombre == 'luke skywalker')):

        print ('El planeta natal de ', dato.nombre ,' es ', dato.planeta)
    # else:
    #     print (dato)

    cantidad_elemento += 1    

##Punto C
cantidad_elemento = 0
nuevo_personaje = informacion ( 'marte', 'E-T')
while (cantidad_elemento < personaje.tamanio()):
    dato = personaje.atencion ()
   
    if (dato.nombre == 'maestro yoda'):
        personaje.arribo(nuevo_personaje)
    

    personaje.arribo(dato)
    cantidad_elemento += 1




##Punto D
cantidad_elemento = 0

while (cantidad_elemento < personaje.tamanio()):
    dato = personaje.mover_final()
   
    if (dato.nombre == 'jar jar binks'):
        dato = personaje.atencion ()
        print ('personaje ',dato,' eliminado')
    cantidad_elemento += 1

print()

cantidad_elemento = 0
while (cantidad_elemento < personaje.tamanio()):
    dato = personaje.mover_final ()
    print (dato)
    cantidad_elemento += 1







