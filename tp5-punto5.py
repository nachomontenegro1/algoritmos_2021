# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU),
#  desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para 
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a 
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.


from arbol_binario import Arbol


datos = [
    {'nombre':'Iron Man', 'heroe': True},
    {'nombre':'Thanos', 'heroe': False},
    {'nombre':'Kang', 'heroe': False},
    {'nombre':'Captain Marvel', 'heroe': True},
    {'nombre':'Agatha Harkness', 'heroe': False},
    {'nombre':'Captain America', 'heroe': True},
    {'nombre':'Taneleer Tivan', 'heroe': False},
    {'nombre':'Black Widow', 'heroe': True},
    {'nombre':'Doctor Strnge', 'heroe': True},
    {'nombre':'Scarlet Witch', 'heroe': True},
    {'nombre':'Ravonna Renslayer', 'heroe': False},
]

arbol = Arbol()

for personaje in datos:
    arbol = arbol.insertar_nodo(personaje['nombre'], personaje) # por el arbol avl

#Punto B
print('Villanos Ordenados Alfabeticamente')
arbol.inorden_villanos()
print()

#Punto C
print ('Superhéroes con nombre iniciado en "C"')
arbol.inorden_heroes_C()
print()

#Punto D
print('En el arbol hay', arbol.contar_nodos(True), 'heroes.')
print()

#Punto E
buscado = input('Escriba las primeras letras del nombre del personaje que desea cambiar: ')
arbol.busqueda_proximidad(buscado)
buscado = input('Ingrese el nombre completo del personaje que desea cambiar de la lista anterior: ')
pos = arbol.busqueda(buscado)
if (pos):
    nuevo_nombre = input('Ingrese el nuevo nombre: ')
    nombre, superheroe = arbol.eliminar_nodo(buscado)
    superheroe['nombre'] = nuevo_nombre
    arbol = arbol.insertar_nodo(nuevo_nombre, superheroe)
print()
arbol.inorden()
print()

#Punto F
print ('Heroes de manera descendente')
arbol.postorden_heroes()
print()

#Punto G
arbol_heroes = Arbol()
arbol_villanos = Arbol()

arbol_heroes = arbol.separar_arbol(arbol_heroes, True)
print ('Arbol de superheroes: ')
arbol_heroes.inorden()
print('Hay ',arbol_heroes.contar_nodos(True),' nodos')
print ()

arbol_villanos = arbol.separar_arbol(arbol_villanos, False)
print ('Arbol de villanos')
arbol_villanos.inorden()
print('Hay ',arbol_villanos.contar_nodos(False),' nodos')
print ()