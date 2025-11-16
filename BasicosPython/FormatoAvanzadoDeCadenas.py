'''
No: 25
Tema: Formato Avanzado de cadenas
Autor: Prof. Eduardo67
Fecha: 16/11/2025
'''

#***********Formateo Avanzado de CAdenas*****************

print("\n")

num1=83
num2=9

print(f"El producto de {num1} y {num2} es {num1*num2}")

autor="Gabriel Garcia Marques"

print(f"El libro fué escrito por el autor: {autor.title()}")


def opcion(o):
    if(o%2==0):
        return "Aprende Python"
    else:
        return "Aprende Java"


print(f"Hola Python, dime que debería aprender.{opcion(4)}")

