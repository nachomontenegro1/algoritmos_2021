from grafo import Grafo

# 6. Partiendo del árbol genealógico de los dioses griegos que se observa en la imagen del ejercicio
# 22 de la guía de árboles (capítulo X), convertirlo en un grafo y resolver las siguientes actividades:
# a. además del nombre de los dioses, deberá cargar una breve descripción de quien es o lo que
# representa, no más de 20 palabras;
# b. deberá cargar todas las relaciones entre los distintos dioses: padre, madre, hijo, hermano,
# pareja, la etiquetas de dichas aristas son estos nombre de relación.
# c. dado el nombre de un dios mostrar los hijos de este;
# d. dado el nombre de un dios mostrar su nombre, padre, madre, hermanos y sus hijos;
# e. determinar si existe relación directa entre dos vértice cualquieras, de ser así cual es la relación
# entre ambos;
# f. dados dos dioses determinar el camino más corto entre estos y mostrarlo. Considere como
# camino más corto el que tenga menor número de aristas;
# g. realizar un barrido en profundidad y amplitud de dicho grafo;
# h. realizar un barrido mostrando el nombre de cada dios y el de su madre;
# i. mostrar todos los ancestros de un determinado dios;
# j. mostrar todos los nietos de Cronos;
# k. mostrar todos los hijos de Tea;

dioses = Grafo()

file = open('dioses.txt', encoding="utf8")
lineas = file.readlines()
lineas.pop(0)
for linea in lineas:
    dios = linea.split(';')
    dios_data = {}
    nombre = dios[0]
    dios_data['descripcion'] = dios[5]
    dios_data['genero'] = dios[6]
    dioses.insertar_vertice(nombre, data = dios_data)

for linea in lineas:
    dios = linea.split(';')
    nombre = dios[0]
    padre = dios[1]
    madre = dios[2]
    hermanos = dios[3].split('/')
    hijos = dios[4].split('/')
    genero = dios[6]
    pareja = dios[7].split('\n')[0]
    if (madre != '-'):
        dioses.insertar_arista(1, nombre, madre, data = 'hijo/a')
    if (padre != '-'):
        dioses.insertar_arista(1, nombre, padre, data = 'hijo/a')
    if (hijos[0] != '-'): # porque se creo una lista con un unico elemento que es '-' si no tiene hijos
        for hijo in hijos:
            if (genero == 'F'):
                dioses.insertar_arista(1, nombre, hijo,  data = 'madre')
            else:
                dioses.insertar_arista(1, nombre, hijo,  data = 'padre')
    if (hermanos[0] != '-'): # porque se creo una lista con un unico elemento que es '-' si no tiene hermanos
        for hermano in hermanos: 
            dioses.insertar_arista(1, nombre, hermano, data = 'hermano/a')
    
    if (pareja != '-'):
        dioses.insertar_arista(1, nombre, pareja, data = 'pareja')

print('------------ Inicio Ejercicio 06 ------------')
print()

# Punto C
nombre_dios = input('Ingrese el nombre de un dios para ver a sus hijos: ').capitalize()
hijos = dioses.hijos_dios(nombre_dios)
if (hijos == None):
    print ('El dios ingresado no se encuentra cargado.')
elif (not hijos == []):
    print ('Los hijos de', nombre_dios, 'son:')
    for hijo in hijos:
        print (' - ', hijo)
else:
    print ('No hay informacion sobre los hijos de', nombre_dios)
print()

# Punto D
nombre_dios = input('Ingrese el nombre de un dios para ver a su familia: ').capitalize()
padres, hijos, hermanos = dioses.familia_dios(nombre_dios)

if (padres == None):
    print ('El dios ingresado no se encuentra cargado.')
else:
    print ('Miembros de la familia de', nombre_dios, ':')    
    if (not padres == []):
        print ('Padres:')
        for padre in padres:
            print (' -', padre)
    if (not hermanos == []):            
        print ('Hermanos:')
        for hermano in hermanos:
            print (' -', hermano)
    if (not hijos == []):            
        print ('Hijos:')
        for hijo in hijos:
            print (' -', hijo)    
print()


# Punto E
print('A continuacion, ingrese los nombres de dos dioses para determinar si tienen una relacion directa.')
vertice_origen = input('Ingrese el nombre del primer dios: ').capitalize()
vertice_destino = input('Ingrese el nombre del segundo dios: ').capitalize()
relaciones = dioses.relacion_dioses(vertice_origen, vertice_destino)
if (not relaciones == []):
    print ('Relacion(es) entre', vertice_origen, 'y', vertice_destino, ':')
    for relacion in relaciones:
        print(' - ', vertice_origen, 'es', relacion, 'de', vertice_destino)
else:
    print('No existe relacion directa entre', vertice_origen, 'y', vertice_destino)
print()

# Punto F

print('A continuacion, ingrese los nombres de dos dioses para determinar el camino mas corto entre ambos.')
dios1 = input('Ingrese el nombre del primer dios: ').capitalize()
dios2 = input('Ingrese el nombre del segundo dios: ').capitalize()
print()
ver_origen = dioses.buscar_vertice(dios2)
ver_destino = dioses.buscar_vertice(dios1)

pila_camino = dioses.dijkstra(ver_origen, ver_destino)

destino = dios1
costo = None

print ('El camino mas corto es:')
while(not pila_camino.pila_vacia()):
    dato = pila_camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(' - ', dato[1][0])
        destino = dato[1][1]

print('El costo total del camino es', costo)
print()

# Punto G
a = input('Presione enter para ver el barrido en profundidad.')
dioses.barrido_profundidad(0)
print()
dioses.marcar_no_visitado()
a = input('Presione enter para ver el barrido en amplitud.')
dioses.barrido_amplitud(0)
dioses.marcar_no_visitado()
print()

# Punto H
a = input('Presione enter para ver el barrido de los dioses y sus madres.')
dioses.barrido_profundidad_dioses_madres(0)
dioses.marcar_no_visitado()
print()

# Punto I
ancestros = []
nombre_dios = input('Ingrese el nombre de un dios para ver a sus ancestros: ').capitalize()
dioses.ancestros_dios(nombre_dios, ancestros)
if (not ancestros == []):
    print('Ancestros de', nombre_dios)
    for ancestro in ancestros:
        print(' - ', ancestro)
else:
    print ('No hay informacion sobre los ancestros de', nombre_dios)
print()

# Punto J
print ('Nietos de Cronos:')
nietos = dioses.nietos_dios('Kronos')
for nieto in nietos:
    print (' - ', nieto)
print()

# Punto K
print ('Los hijos de Tea son:')
hijos = dioses.hijos_dios('Theia')
for hijo in hijos:
    print (' - ', hijo)
print()
