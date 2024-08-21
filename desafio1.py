import random 

def crear(n,m):
    return [[0]*m for fil in range(n)]

def llenar(m):
    filas=len(m)
    columnas=len(m[0])
    for fil in range(filas):
        for col in range(filas):
            num_aleatorio=random.randint(1,10)
            m[fil][col]=num_aleatorio

def imprimir(matriz,estudiantes,materias):
    filas=len(matriz)
    columnas=len(matriz[0])
    for fil in range(filas):
        for col in range(columnas):
            print("%3d"% matriz[fil][col],end=" ")
        print()
    encabezado = "      " + "  ".join([f"{materia:^5}" for materia in materias])
    print(encabezado)
    print("-" * len(encabezado))

    
    for i in range(filas):
        fila = f"{estudiantes[i]:<6}" + "  ".join([f"{matriz[i][j]:^5}" for j in range(columnas)])
        print(fila)

matriz=crear(5,5)
print()
llenar(matriz)
estudiantes="clara","juan","tom","marco","manuel"
materias="fisica","mate","lengua","historia","ingles"
imprimir(matriz,estudiantes,materias)
print()

def promedio_e(matriz, estudiantes):
    for i in range(len(matriz)):
        promedio = sum(matriz[i]) / len(matriz[i])
        print("Promedio de {}: {:.2f}".format(estudiantes[i], promedio))

def promedio_m(matriz, materias):
    for j in range(len(materias)):
        promedio = sum(fila[j] for fila in matriz) / len(matriz)
        print("Promedio de {}: {:.2f}".format(materias[j], promedio))


promedio_e(matriz,estudiantes)
promedio_m(matriz,materias)