'''
No: 3
Tema: Lectura de datos de consola
Autor: Prof. Eduardo67
Fecha: 27/10/2025

'''

Entrada = input() #Texto de entrada
print(Entrada) 
nombre = input("Como te llamas: ") #Mostrar texto en pantalla pidiendo el dato que necesitamos
print("Bienvenido a trabajar ", nombre) 


#Los valores que recibe la función input() son cadenas de texto, por eso es necesario hacer una conversión llamada cash o parse

n1 = input("Número 1: ")
n2 = input("Número 2: ")
suma = int(n1) + int(n2)
resta = int(n1) - int(n2)

print("El resultado de la suma es: " + str(suma)) #Podemos poner + o , para concatenar
print("El resultado de la suma es: " , str(resta)) #Podemos poner + o , para concatenar
