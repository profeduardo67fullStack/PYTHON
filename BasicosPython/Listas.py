'''
No: 19
Tema: Listas
Autor: Prof. Eduardo67
Fecha: 14/11/2025
'''

#inicializando una lista

lista=[1,True,"Alberto"]
print(lista)

#Funciones para trabajar con listas

listaDeAlumnos=["Júan","Pedro","María","Manuel"]
print(listaDeAlumnos)

#Agregar una elemento
listaDeAlumnos.append("Felipe")
print(lista)

#Insertar un nuevo elemento en un índice
listaDeAlumnos.insert(1,"ElementoNuevoDesplazando")
print(listaDeAlumnos)

#Extender la lista agregando mas de un valor, pasando como par+ametro un vector

listaDeAlumnos.extend([7,8,9])
print(listaDeAlumnos)

#Hacemos un pop, elimina el último elemento de nnuestra lista
x=listaDeAlumnos.pop()
print(listaDeAlumnos)
print(x)

#Removiendo con remove

listaDeAlumnos.remove("María")
print(listaDeAlumnos)

