'''
No: 15
Tema: Definiendo funciones básicas
multiplica por 2. Se sumarán los multiplicados que correspondan a multiplicadores impares.
Autor: Prof. Eduardo67
Fecha: 09/11/2025
'''


#Función sin parámetros
def saludo():
    #Todo esto pertenece a la función
    print("HolaMundo, desde mi primera función")


saludo()

#Función con parámetros
def suma(par_a,par_b):
    a=par_a #Asignamos el primer parámetro pasado a una variable
    b=par_b #Asignamos e segundo parámetro a otra variable
    c=a+b #Realizamos la suma y guardamos
    print(f"La suma de los dos números {a} y {b} pasados como parámetros es: {c}")

#invocamos a la función suma() con dos argumenntos

suma(2,3)


#Declarando una función con valores asignados, por si no pasan el número de parámetros completo

def suma_predefinida(par_1=1, par_2=1):
    a=par_1
    b=par_2
    c=par_1*par_2
    print(f"Salida con parámetros asegurados, ya sean los definidos o los enviados {par_1} y {par_2} = {c}")


#Invocamos a la función

suma_predefinida()
suma_predefinida(5,3)
suma_predefinida(5)




