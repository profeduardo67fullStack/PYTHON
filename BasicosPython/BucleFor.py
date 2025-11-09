'''
No: 12
Tema: Bucle FOR básico, entendiendo la diferencia con otros lenguajes de programación
multiplica por 2. Se sumarán los multiplicados que correspondan a multiplicadores impares.
Autor: Prof. Eduardo67
Fecha: 09/11/2025
'''
from collections.abc import Iterable #Se utiliza en el ejemplo 3 para verificar si un elemento es iterable

#Ejemplo sin rango definido, mas que los extemos
for i in range(0,5):
    print(i)

#Ejemplo con rangos definidos
print("Iniciamos...")
for i in [1,2,3]:
    print("Hola ", end="")
print()
print("Finalizamos...")

#Verificando si un elemento es iterable o no con la función isistance()

lista=[1,2,3]
cadena="Python"
numero=10
print(isinstance(lista,Iterable))
print(isinstance(cadena,Iterable))
print(isinstance(numero,Iterable))

#Cuando una variable de control no se va a utilizar en el cuerpo del bucle se puede utilizar _

print("INICIO")
for _ in [0,1,2]:
    print(" Hola ", end="")
print()
print("FINAL")
        
#Cuando se utiliza la variable de control es importante recordar que esta va tomando el valor del elemento que se itera

i=10
print(f"El ciclo ha iniciado y la variable tiene el valor de {i}")
for i in [0,1,2]:
    print(f"ahora i vale {i}")
    i=100
    print(f"después i vale {i}")
print()
print(f"EL CICLO HA TERMINADO AHORA LA VARIABLE VALE {i}")


