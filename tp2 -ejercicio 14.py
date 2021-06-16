from pila import Pila
from random import randint

pila_datos = Pila()
pila_aux = Pila()
num=int


for i in range (0,5):
    num =  int(input('ingrese numero para agregar a la pila: '))
    if pila_datos.pila_vacia() or (num >= pila_datos.elemento_cima()): 
            pila_datos.apilar(num)
            print ( "numero cargado")
    else:
        while (not pila_datos.pila_vacia() and num < pila_datos.elemento_cima()):  
            pila_aux.apilar(pila_datos.desapilar())
        pila_datos.apilar(num)
        print ( "numero cargado")

        while (not pila_aux.pila_vacia()):
            pila_datos.apilar(pila_aux.desapilar())

while (not pila_datos.pila_vacia()):
    print (pila_datos.desapilar())