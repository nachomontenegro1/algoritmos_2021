from pila import Pila
from random import randint

class Bitacora(object):
    planeta, capturado, recompensa = '', '', float

    def __init__(self, planeta, capturado, recompensa):
         self.planeta = planeta
         self.capturado = capturado
         self.recompensa = recompensa

    def __str__(self):
         return self.planeta+' - '+self.capturado+' - '+self.recompensa

boba = Pila()
djarin = Pila()

#Cargamos la bitacora de Boba Fett

dato = Bitacora ('tierra','han solo',10000000)
boba.apilar(dato)
dato = Bitacora ('rojo','droide',200)
boba.apilar(dato)
dato = Bitacora ('azul','enano verde',10)
boba.apilar(dato)
dato = Bitacora ('mercurio','asesino',5542)
boba.apilar(dato)


#Cargamos la bitacora de Din Djarin
dato = Bitacora ('257','soldado',4478)
djarin.apilar(dato)
dato = Bitacora ('900','luke',845600)
djarin.apilar(dato)
dato = Bitacora ('7882','lela',420)
djarin.apilar(dato)


contador_capturas_boba = 0
contador_capturas_djarin = 0
captura = False
num_mision = 0
cont_mision = 0
mision_captura = 0
acum_boba = float
acum_djarin = float

print ('Planetas visitados por Boba Fett')
acum_boba = 0
while (not boba.pila_vacia()):
    x = boba.desapilar()
    contador_capturas_boba = contador_capturas_boba + 1
    cont_mision = cont_mision + 1
    acum_boba = acum_boba + x.recompensa
    print (x.planeta)
        

    if (x.capturado == 'han solo'):
        captura = True
        mision_captura = cont_mision

print ('En total realizo ' + str(contador_capturas_boba) + ' capturas')

print ('Recaudó ' + str(acum_boba) + ' creditos galacticos')


print ('Planetas visitados por Din Djarin')
acum_djarin = 0
while (not djarin.pila_vacia()):
    x = djarin.desapilar()
    contador_capturas_djarin = contador_capturas_djarin + 1
    acum_djarin = acum_djarin + x.recompensa
    print (x.planeta)

print ('En total realizo ' + str(contador_capturas_djarin) + ' capturas')

print ('Recaudó ' + str(acum_djarin) +  ' creditos galacticos')

if (acum_boba > acum_djarin):
    print ('El mercenario Boba Fett acumulo mas creditos galacticos')
else:
    print ('El mercenario Din Djarin acumulo mas creditos galacticos')

if (captura):
    print ('Boba Fett capturo a han solo en la mision ' + str(mision_captura))