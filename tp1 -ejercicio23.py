
def salida_laberinto(matriz, x, y, caminos=[]):
    """Salida del laberinto."""
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if(matriz[x][y] == 2):
            caminos.append([x, y])
            print("Saliste del laberinto")
            print(caminos)
            caminos.pop()
        elif(matriz[x][y] == 1):
            matriz[x][y] = 3
            caminos.append([x, y])
            # print("mover este")
            salida_laberinto(matriz, x, y+1, caminos)
            # print("mover oeste")
            salida_laberinto(matriz, x, y-1, caminos)
            # print("mover norte")
            salida_laberinto(matriz, x-1, y, caminos)
            # print("mover sur")
            salida_laberinto(matriz, x+1, y, caminos)
            caminos.pop()
            matriz[x][y] = 1


lab = [[1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 0, 1],
       [1, 1, 1, 0, 1, 0, 1],
       [0, 1, 1, 1, 1, 1, 1],
       [0, 1, 0, 0, 0, 0, 0],
       [2, 1, 0, 0, 0, 0, 0]]
    
salida_laberinto(lab, 0, 0)