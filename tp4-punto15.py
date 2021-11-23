# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver 
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;[115]
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador 
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se 
# deberán mostrar los datos de ambos

from lista import Lista 

entrenadores = Lista()
pokemones = Lista()
entrenadores_79 = Lista() #CORRESPONDE A PUNTO E
lista_tipos = Lista() #CORRESPONDE A PUNTO F 

file = open('entrenadores.txt')
file2 = open('pokemones.txt')


lineas = file.readlines()
lineas.pop(0)

for linea in lineas:
    entrenador = linea.split(';')
    entrenador_data = {}
    entrenador_data['Nombre'] = entrenador[0]
    entrenador_data['Torneos'] = int(entrenador[1])
    entrenador_data['Perdidas'] = int(entrenador[2])
    entrenador_data['Ganadas'] = int(entrenador[3])
    entrenador_data['ID'] = int(entrenador[4].split('\n')[0])
    entrenador_data['Pokemones'] = Lista()
    entrenadores.insertar(entrenador_data, 'Nombre')

lineas = file2.readlines()
lineas.pop(0)

for linea in lineas:
    pokemon = linea.split(';')
    pokemon_data = {}
    pokemon_data['Nombre'] = pokemon[0]
    pokemon_data['Nivel'] = int(pokemon[1])
    pokemon_data['Tipo'] = pokemon[2]
    pokemon_data['Subtipo'] = pokemon[3]
    pokemon_data['ID'] = int(pokemon[4].split('\n')[0])
    pokemones.insertar(pokemon_data, 'ID')

for i in range (entrenadores.tamanio()):
    id_entrenador = entrenadores.obtener_elemento(i)['ID']
    for j in range (pokemones.tamanio()):
        id_pokemon = pokemones.obtener_elemento(j)['ID']
        if (id_entrenador == id_pokemon):
            entrenadores.obtener_elemento(i)['Pokemones'].insertar(pokemones.obtener_elemento(j), 'Nombre')

def mostrar_datos (lista, pos): #Muestra datos de entrenadoras y sus pokemones
    entrenador = lista.obtener_elemento(pos)
    print ('°', entrenador ['Nombre'])
    print ('Torneos ganados:',entrenador['Torneos'], ' -Batallas perdidas:',entrenador['Perdidas'], ' -Batallas ganadas: ', entrenador['Ganadas'])
    print ('Pokemones:')
    for j in range (0, entrenador['Pokemones'].tamanio()):
        pokemones = lista.obtener_elemento(pos)['Pokemones']
        print (pokemones.obtener_elemento(j)['Nombre'], '-Nivel: ', pokemones.obtener_elemento(j)['Nivel'], '- Tipo: ', pokemones.obtener_elemento(j)['Tipo'], '-Subtipo: ', pokemones.obtener_elemento(j)['Subtipo'])

for i in range (entrenadores.tamanio()):
    mostrar_datos(entrenadores, i)
    print ()


#Punto A
nombre = input ('Ingrese el nombre del entrenador para saber la cantidad de pokemon que posee: ').capitalize() #Hace mayusculas la primer letra de la palabra
pos = entrenadores.busqueda(nombre, 'Nombre')
if pos != -1:
    print (nombre, ' posee', entrenadores.obtener_elemento(pos)['Pokemones'].tamanio())
print()

#Punto B
mas_torneos = entrenadores.obtener_elemento(0)
print ('Entrenadores que ganaron mas de tres torneos: ')

for i in range (entrenadores.tamanio()):
    entrenador= entrenadores.obtener_elemento(i)
    lista_pokem = entrenador['Pokemons']
    if (entrenador['Torneos'] > 3):
        print (entrenador['Nombre'],' ganó', entrenador ['Torneos'], ' torneos')

    if entrenador['Torneos'] > mas_torneos['Torneos']:
        mas_torneos = entrenador

    if (entrenador ['Ganadas'] * 100 // (entrenador['Perdidas'] + entrenador['Ganadas']) > 79):
        entrenadores_79.insertar(entrenador, 'Nombre') 

    for j in range (lista_pokem.tamanio()):
        pokemon = lista_pokem.obtener_elemento(j)
        if ((pokemon['Tipo'] == 'Fuego' and pokemon['Subtipo'] == 'Planta') or (pokemon['Tipo'] == 'Agua' and pokemon['Subtipo']== 'Volador')):
            lista_tipos.insertar(entrenador, 'Nombre')  

print()

#Punto C
lista_pokem = mas_torneos['Pokemones']
mayor_nivel = lista_pokem.obtener_elemento(0)
for i in range(lista_pokem.tamanio()):
    if (lista_pokem.obtener_elemento(i)['Nivel'] > mayor_nivel['Nivel']):
        mayor_nivel = lista_pokem.obtener_elemento(i)

#Punto D
entr = input ('Ingrese el nombre de entrenador para conocer sus datos y sus pokemon').capitalize()
pos = entrenadores.busqueda(entr, 'Nombre')
if (pos != -1):
    mostrar_datos(entrenadores, pos)
    print()

#Punto E
print('Entrenadores con win rate mayor a 79%: ')
for i in range (entrenadores_79.tamanio()):
    print (entrenadores_79.obtener_elemento(i)['Nombre'])

print()

#Punto F
print('Entrenadores que tienen Pokemon de tipo fuego/planta o agua/volador:')
for i in range(lista_tipos.tamanio()):
    print(lista_tipos.obtener_elemento(i)['Nombre'])

print()

#Punto G
def promedio_nivel (lista_pokemon):
    """Calcula el promedio de nivel de los pokemones en una lista"""
    total_niveles = 0
    for i in range (lista_pokemon.tamanio()):
        total_niveles += lista_pokemon.obtener_elemento(i)['Nivel']
    return total_niveles/lista_pokemon.tamanio()

nombre = input('Ingrese el nombre del entrenador para calcular el promedio de nivel de sus Pokemon: ').capitalize()
pos = entrenadores.busqueda(nombre, 'Nombre')
if (pos != -1):
    """round redondea un numero"""
    promedio = round(promedio_nivel(entrenadores.obtener_elemento(pos)['Pokemones'],2))
    print('El promedio de nivel de los Pokemon de', entr, 'es:', promedio)

print()

#Punto H
def entrenadores_pokemon (pokemon, lista):
    """Determina cuantos entrenadores tienen a un determinado pokemon."""
    cantidad_entrenadores = 0
    for i in range (lista.tamanio()):
        pos = lista.obtener_elemento(i)['Pokemones'].busqueda(pokemon, 'Nombre')
        if (pos != -1):
            cantidad_entrenadores += 1
    return cantidad_entrenadores

poke = input('Ingrese el nombre del Pokemon para determinar cuantos entrenadores lo tienen: ').capitalize()
print (entrenadores_pokemon(poke, entrenadores), 'entrenador(es) tiene(n) a', poke)

print()

#Punto I
def Entrenador_pokemon_repetido(Lista):
    ocurrencias = None

    for i in range(0, Lista.tamanio()):
        entrenador = Lista.obtener_elemento(i)
        
        for i in range(0, entrenador['pokemons'].tamanio()):
            ocurrencias = 0

            for j in range(0, entrenador['pokemons'].tamanio()):
                if entrenador['pokemons'].obtener_elemento(i)['nombre'].lower() == entrenador['pokemons'].obtener_elemento(j)['nombre'].lower():
                    ocurrencias += 1

                    if ocurrencias > 1:
                        break
            
            if ocurrencias > 1:
                print(entrenador)
                break

print ('Entrenadores con pokemon repetidos: ')
Entrenador_pokemon_repetido(entrenadores)



#Punto J
print('Los entrenadores que tienen un Tyrantrum, Terrakion o Wingull son:')
for i in range(entrenadores.tamanio()):
    entrenador =  entrenadores.obtener_elemento(i)
    lista_pokemones = entrenador['Pokemones']
    for j in range(lista_pokemones.tamanio()):
        if (lista_pokemones.obtener_elemento(j)['Nombre'] == 'Tyrantrum' or 
            lista_pokemones.obtener_elemento(j)['Nombre'] == 'Terrakion' or 
            lista_pokemones.obtener_elemento(j)['Nombre'] == 'Wingull'):
            print(entrenador['Nombre'])

print()

#Punto K
ent = input('Ingrese el nombre del entrenador para saber si tiene a un Pokemon: ').capitalize()
pos = entrenadores.busqueda(ent, 'Nombre')
if pos != -1:
    poke = input('Ingrese el nombre del pokemon: ').capitalize()
    pos2 = entrenadores.obtener_elemento(pos)['Pokemones'].busqueda(poke, 'Nombre')
    if pos2 != -1:
        print(ent, 'tiene a', poke)
        entrenador = entrenadores.obtener_elemento(pos)
        print(ent, '| Torneos Ganados:', entrenador['Torneos'], '| Batallas perdidas:', entrenador['Perdidas'], '| Batallas ganadas:', entrenador['Ganadas'])
        pokemon = entrenadores.obtener_elemento(pos)['Pokemones'].obtener_elemento(pos2)
        print (poke, '| Nivel:', pokemon['Nivel'], '| Tipo:', pokemon['Tipo'], '| Subtipo:', pokemon['Subtipo'])
    else:
        print(ent, 'no tiene a', poke)
else:
    print ('No existe entrenador con ese nombre.')
