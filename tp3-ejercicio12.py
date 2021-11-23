# 12.Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una 
# nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar, 
# ni métodos de ordenamiento.

from cola import Cola
from random import randint

cola1= Cola()
cola2= Cola()
cola_final= Cola()

list1= [3,6,8,9,1]
list2= [4,7,8,2,5]

print ('Para la Cola 1, sumamos: ')
for i in (list1):
     cola1.arribo(i)
     print (i)

print ('Para la Cola 2, sumamos: ')
for i in (list2):
     cola2.arribo(i)
     print (i)


print()

while (not cola1.cola_vacia() and not cola2.cola_vacia()):
### comparamos elemento a elemento desde el frente de cada cola con la otra
     if (cola1.en_frente() < cola2.en_frente()):
         cola_final.arribo(cola1.atencion())
     else:
         cola_final.arribo(cola2.atencion())
####si una de las dos colas esta vacia, cargaremos el elemento restante de la otra cola ,a la cola final
     if (cola1.cola_vacia()):
         cola_final.arribo(cola2.atencion())
     if (cola2.cola_vacia()):
         cola_final.arribo(cola1.atencion())

print ('Cola final')
cantidad_elemento = 0
while (cantidad_elemento < cola_final.tamanio()):
     dato = cola_final.mover_final ()
     print (dato)
     cantidad_elemento += 1