'''
No: 6
Tema: Implementando formula general para la resolución de ecuaciones de segundo grado
Autor: Prof. Eduardo67
Fecha: 08/11/2025
'''
import math

a=int(input(" Ingresa el valor de A "))
b=int(input(" Ingresa el valor de B "))
c=int(input(" Ingresa el valor de C "))
discriminante=(b**2)-4*a*c
if(discriminante > 0):
    x1=(-b+math.sqrt(discriminante))/(2*a)
    x2=(-b-math.sqrt(discriminante))/(2*a)
    print(f'X1={round(x1,2)}\nX2={x2}') #con f'' le damos formato a la salida \n, inserta un salto de línea
elif discriminante==0:
    x=-b/(2*a)
    print(f'X={x}')
else:
    print('<< No tiene solución >>')


