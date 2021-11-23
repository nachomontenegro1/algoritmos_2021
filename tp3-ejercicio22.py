# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU),
# de los cuales se conoce el nombre del personaje, el nombre del superhéroe y
# su género (Masculino M y Femenino F) –por ejemplo
# {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, 
# {Natasha Romanoff, Black Widow, F}, etc., 
# desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superheroes   

from cola import Cola
personaje = Cola()

class persona(object):
    nombre_personaje, nombre_super, genero = '', '', ''

    def __init__(self, nombre_personaje, nombre_super, genero):
            self.nombre_personaje = nombre_personaje
            self.nombre_super = nombre_super
            self.genero = genero
          

    def __str__(self):
          return self.nombre_personaje+': ' + self.nombre_super +'. '+ ' Genero: '+ self.genero

dato = persona ('Steve Rogers', 'Capitan America', 'M')
personaje.arribo(dato)
dato = persona ('Tony Stark', 'Iron Man', 'M') 
personaje.arribo(dato)
dato = persona ('Natasha Romanoff', 'Black Widow', 'F')
personaje.arribo(dato)
dato = persona ('Thor Odinson', 'Thor.', 'M')
personaje.arribo(dato)
dato = persona ('Sam Wilson', 'Falcon', 'M')
personaje.arribo(dato)
dato = persona ('Carol Danvers', 'Capitana Marvel', 'F')
personaje.arribo(dato)
dato = persona ('Wanda Maximoff', 'Bruja Escarlata', 'F')
personaje.arribo(dato)
dato = persona ('Stephen Strange', 'Doctor Strange', 'M')
personaje.arribo(dato)
dato = persona ('Bruce Banner', 'Hulk', 'M')
personaje.arribo(dato)
dato = persona ('Scott Lang', 'Ant-Man', 'M')
personaje.arribo(dato)


cantidad_elemento = 0
while (cantidad_elemento < personaje.tamanio()):
    dato = personaje.mover_final ()
    print (dato)
    cantidad_elemento += 1

print ()

cantidad_elemento = 0
while ( cantidad_elemento < personaje.tamanio()):
    dato = personaje.atencion()
    ##punto A
    if (dato.nombre_super == 'Capitana Marvel'):
        print ('Dato del Punto A: ')
        print (dato.nombre_personaje)

    ##punto B
    if (dato.genero =='F'):
        print ('Superhéroes Femeninos: ')
        print (dato.nombre_super)
    
    ##punto C
    if (dato.genero =='M'):
        print ('Superhéroes Maculinos: ')
        print (dato.nombre_personaje)
    
    ##punto D
    if (dato.nombre_personaje == 'Scott Lang'):
        print ('Dato del punto D: ')
        print (dato.nombre_super)
    
    ##Punto E
    if ((dato.nombre_personaje[0] == 's') or (dato.nombre_super[0] == 's')):
        print ('Nombre/s comenzado/s en "S": ')
        print (dato)
    
    ##punto F
    if (dato.nombre_personaje == 'carol danvers'):
        print ('Dato del punto F: ')
        print (dato.nombre_super)
   

    personaje.arribo(dato)
    cantidad_elemento +=1