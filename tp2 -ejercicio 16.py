from pila import Pila
from random import randint

pila1 = Pila()
pila2 = Pila()
pila_repetido = Pila()
pila1_aux = Pila()

#Cargamos personajes pila 1
pila1.apilar('enano verde')
pila1.apilar('chiwi')
pila1.apilar('arturo')

#Cargamos personajes pila 2
pila2.apilar('droide')
pila2.apilar('tenebroso')
pila2.apilar('enano verde')


    


while(not pila1.pila_vacia()):
    aux=pila1.desapilar()
    if ( aux == pila2.elemento_cima()):
        pila_repetido.apilar(aux)
        pila2.desapilar()
        print ('personaje repetido cargado')
    else:
        pila1_aux.apilar(aux)
        print ('no hay coincidencia')

while(not pila2.pila_vacia() and not pila1_aux.pila_vacia()):
    aux=pila2.desapilar()
    if (aux == pila1_aux.elemento_cima()):
        pila_repetido.apilar(aux)
        print ('personaje repetido cargado')
    else:
    
        print ('no hay coincidencia')

while (not pila_repetido.pila_vacia()):
    print (pila_repetido.desapilar())