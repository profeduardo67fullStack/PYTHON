'''
No: 18
Tema: Practicando Matrices
Autor: Prof. Eduardo67
Fecha: 09/11/2025
'''

#Una matriz en Python la podemos ver como un vector de vectores
matriz=[[1,2,3],[4,5,6]]
print(matriz)


#Podemos recorrer esta matriz con ciclos anidados

for i in matriz:
    for j in i:
        print(j)


matriz[0][0]=4
print(matriz)