'''
No: 10
Tema: Menú deopciones
Autor: Prof. Eduardo67
Fecha: 09/11/2025
'''

num1=int(input("Introduce el primer número entero: "))
num2=int(input("Introduce el segundo número entero: "))
opcion=int(input("1.- Sumar\n2.- Restar\n3.- Multiplicar\n4.- Terminar\nSelecciona una opción: "))
while opcion!=4:
    if opcion==1:
        print(f"la suma total es --> {num1+num2}")
    elif opcion==2:
        print(f"la suma total es --> {num1-num2}")
    elif opcion==3:
        print(f"la suma total es --> {num1*num2}")
    opcion=opcion=int(input("1.- SUmar \n 2.- Restar \n 3.- Multiplicar \n 4.- Terminar \n Selecciona una opción: "))
