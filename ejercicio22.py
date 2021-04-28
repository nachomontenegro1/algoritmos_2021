#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u 
#otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos 
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con 
#ayuda de la fuerza” realizar las siguientes actividades:
#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no 
#queden más objetos en la mochila;
#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
#c. Utilizar un vector para representar la mochila


mochila = ['pistola', 'Comida', 'Sable de luz', 'arturito']


def usar_fuerza(mochila, pos):
    if(pos< len(mochila)):
        
        if(mochila[pos] == 'Sable de luz'): 
            print ('Hay un sable de luz')
            return pos
        else:
            return usar_fuerza(mochila, pos+1)
    else:
        print ('No hay sable')
        return -1


print ('Fueron necesario sacar ',(usar_fuerza(mochila, 0)),' elementos')


    
    