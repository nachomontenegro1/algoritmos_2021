#7. Implementar los algoritmos necesarios para resolver las siguientes tareas:
# a. concatenar dos listas, una atrás de la otra;
# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;[113]
# d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido

from lista import Lista 

lista1 = Lista()
lista2 = Lista()
lista_concatenada= Lista()

for i in range (0,10):
    lista1.insertar(i)

for i in range (0,10):
    lista2.insertar(i*2)

for i in range (lista1.tamanio()):
    lista_concatenada.insertar(lista1.obtener_elemento(i))

for i in range (lista2.tamanio()):
    lista_concatenada.insertar(lista2.obtener_elemento(i))
    print ('Listas Concatenadas: ')
    lista_concatenada.barrido()
    print()

cont_repetido = 0
for i in range (lista2.tamanio()):
    elemento = lista2.obtener_elemento(i)
    pos = lista1.busqueda(elemento)
    if pos == -1:
        lista1.insertar(elemento)
    else:
        cont_repetido +=1

print ('Listas concatenadas sin valores repetidos: ')
lista1.barrido()
print()

print('Cantidad de calores repetidos en ambas listas: ', cont_repetido)

for i in range (lista1.tamanio()):
    while i < lista1.tamanio():
        print (lista1.eliminar(lista1.obtener_elemento(i)))