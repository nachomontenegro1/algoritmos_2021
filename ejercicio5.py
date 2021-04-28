#Desarrollar una función que permita convertir un número romano en un número decimal

romano = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
         (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def conversor (romano, numero, posicion):
    i,r = romano [posicion]
    if (numero == 0):
        return ''
    elif (numero >= i):
        numero -= i
        return r + str(conversor(romano, numero, posicion+1))
    else:
        return conversor(romano, numero, posicion+1)

print (conversor(romano,44,0))
