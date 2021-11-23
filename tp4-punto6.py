# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, 
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar
#  las siguientes actividades:
# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

from lista import Lista
lista_super=Lista()

datos = [
        {'name':'Wolverine','anio_aparicion': 1960, 'Casa de Comic' : 'DC', 'biografia': 'garras'},
        {'name':'Linterna Verde','anio_aparicion': 1970, 'Casa de Comic' : 'MARVEL', 'biografia': 'linterna'},
        {'name':'Dr. Strange','anio_aparicion': 1978, 'Casa de Comic' : 'DC', 'biografia': 'traje'},
        {'name': 'Black Panther','anio_aparicion':1970, 'Casa de Comic' : 'MARVEL', 'biografia': 'armadura'},
        {'name':'Capitana Marvel','anio_aparicion': 1976, 'Casa de Comic' : 'MARVEL', 'biografia': 'traje'},
        {'name':'Mujer Maravilla','anio_aparicion': 1998, 'Casa de Comic' : 'DC', 'biografia': 'capa'},
        {'name':'Flash','anio_aparicion': 1999, 'Casa de Comic' : 'MARVEL', 'biografia': 'rapidez'},
        {'name':'Star-Lord','anio_aparicion': 1991, 'Casa de Comic' : 'MARVEL', 'biografia': 'lord'},
        {'name': 'Iron man','anio_aparicion':1940, 'Casa de Comic' : 'MARVEL', 'biografia': 'armadura'},
     ]

for personas in datos:
    lista_super.insertar(personas,'name')

lista_super.barrido()
print()

#Punto A
print('Elemento Eliminado: ', lista_super.eliminar('Linterna Verde', 'name'))
print()

#Punto B
pos = lista_super.busqueda('Wolverine','name')
if (pos != -1):
   print('Wolverine apareció en el año: ', lista_super.obtener_elemento(pos)['anio_aparicion'])

#Punto C
pos2 = lista_super.busqueda('Dr. Strange','name')
if (pos2 != -1):
    lista_super.obtener_elemento(pos2)['Casa de Comic'] = 'MARVEL'
print()
lista_super.barrido()

 #Punto D
for i in range(lista_super.tamanio()):
    aux = lista_super.obtener_elemento(i)
    bus_traje = aux['biografia']
    if (('traje' in bus_traje) or ('armadura' in bus_traje)):
        print ('El personaje ',aux['name'],' tiene ', aux['biografia'])

#Punto E
print ('Superhéroes que aparecieron antes el año 1963: ')
for i in range (lista_super.tamanio()):
    aux = lista_super.obtener_elemento(i)
    if (aux['anio_aparicion'] < 1963):
        print (aux['name'],'--',aux['Casa de Comic'])

#Punto F
for i in range (lista_super.tamanio()):
    aux = lista_super.obtener_elemento(i)
    if ((aux['name'] == 'Capitana Marvel') or (aux['name'] == 'Mujer Maravilla')):
        print ('El personaje ',aux['name'],', pertenece a la casa de comic ', aux['casa de comic'])
   
#punto G

for i in range (lista_super.tamanio()):
    aux = lista_super.obtener_elemento(i)
    if ((aux['name'] == 'Flash') or (aux['name'] == 'Star-Lord')):
        print (aux)

#Punto H 
for i in range (lista_super.tamanio()):
    aux = lista_super.obtener_elemento(i)
    if (((aux['name'])[0] == 'B') or ((aux['name'])[0] == 'M') or ((aux['name'])[0] == 'S')):
        print (aux['name'])

#punto I
contador_marvel = 0
contador_dc = 0
for i in range(lista_super.tamanio()):

    aux = lista_super.obtener_elemento(i)
    if (aux['Casa de Comic'] == 'MARVEL'):
        contador_marvel += 1
    if (aux['Casa de Comic'] == 'DC'):
        contador_dc += 1

print (contador_marvel, ' personaje/s de marvel')
print (contador_dc, ' personaje/s de DC')
