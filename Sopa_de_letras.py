import random

# Define el tamaño de la sopa de letras
filas = 50
columnas = 50

# Define las letras que se usarán en la sopa de letras
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Genera una matriz vacía
sopa_de_letras = [[' ' for i in range(columnas)] for j in range(filas)]

# Genera una lista de palabras para incluir en la sopa de letras
palabras = ["PYTHON", "PROGRAMACION", "LETRAS", "SOPA", "ALGORITMO", "REVERSO","ARQUITECTURA","MIPS","ENSAMBLADOR"
            ,"MARS"]

def agregar_palabras():
    for palabra in palabras:
        # Elije una dirección aleatoria
        direccion = random.choice(["horizontal", "vertical"])
        if direccion == "horizontal":
            # Elije una fila y una columna aleatorias para la primera letra
            fila = random.randint(0, filas - 1)
            columna = random.randint(0, columnas - len(palabra))
            # Inserta la palabra en la matriz
            for i in range(len(palabra)):
                sopa_de_letras[fila][columna + i] = palabra[i]
        elif direccion == "vertical":
            # Elije una fila y una columna aleatorias para la primera letra
            fila = random.randint(0, filas - len(palabra))
            columna = random.randint(0, columnas - 1)
            # Inserta la palabra en la matriz
            for i in range(len(palabra)):
                sopa_de_letras[fila + i][columna] = palabra[i]

def rellenar_ramdon():
    for i in range(filas):
        for j in range(columnas):
            if sopa_de_letras[i][j] == ' ':
                sopa_de_letras[i][j] = random.choice(letras)

#def imprimir_sopa():
    #for i in range(filas):
       # for j in range(columnas):
        #    print(sopa_de_letras)

def buscar_horizontal(sopa_de_letras, palabra, i, j):
    n = len(sopa_de_letras[0])
    if j + len(palabra) > n:
        return False

    for k in range(len(palabra)):
        if sopa_de_letras[i][j+k] != palabra[k]:
            return False

    return True
def buscar_vertical(sopa_de_letras, palabra, i, j):
    n = len(sopa_de_letras)
    if i + len(palabra) > n:
        return False

    for k in range(len(palabra)):
        if sopa_de_letras[i+k][j] != palabra[k]:
            return False

    return True


def buscar_palabra(sopa_de_letras, palabra):
    n = len(sopa_de_letras)
    m = len(sopa_de_letras[0])

    for i in range(n):
        for j in range(m):
            if sopa_de_letras[i][j] == palabra[0]:
                if buscar_horizontal(sopa_de_letras, palabra, i, j) or \
                   buscar_vertical(sopa_de_letras, palabra, i, j):
                    print("si esta")
                    return (i, j)

    return None


palabrita = "SOPA"
agregar_palabras()
rellenar_ramdon()
respuesta = buscar_palabra(sopa_de_letras,palabrita)
if respuesta:
    print(respuesta)
else:print("no esta")

















