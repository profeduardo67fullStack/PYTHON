'''
No: 17
Tema: Practicando Vectores
multiplica por 2. Se sumarán los multiplicados que correspondan a multiplicadores impares.
Autor: Prof. Eduardo67
Fecha: 09/11/2025
'''

nombre=["Pedro","Juan","María","Manuel"]
nombres=[["Pedro", "Juán", "Reynaldo"], "María",1,2,3,[True,23,"Eduardo"]]

print(nombre)
print(nombres)

#Operaciones básicas sobre arreglos

vector=[1,3,5] #Declaramos e inicializamos un vector
print(vector)

#Mostrar índices específicos
print(vector[0])
print(vector[1])
print(vector[2])

#Asignar valores específicos por índice
vector[0]=7
vector[1]=6
vector[2]=5

print(vector)

print(vector[-1])
print(vector[-2])
print(vector[-3])

#Duplicando el contenido de un vector

vector=vector+vector
print(vector)

vector=vector*2
print(vector)

#Recorrer un vector con for

for item in vector:
    print(item)

#Acceder al vector y al mismo tiempo multiplicarlo por 2
for item in vector:
    print(item*2)

