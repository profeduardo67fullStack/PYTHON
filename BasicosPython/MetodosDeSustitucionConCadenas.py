'''
No: 23
Tema: Métodos de Sustitución con cadenas de texto
Autor: Prof. Eduardo67
Fecha: 16/11/2025
'''

#**********METODOS DE SUSTITUCIÓN****************

print("\n")

#Format, se utiliza para formatear cadenas de texto


cadena = "bienveido a trabajar {0}"
print(cadena)

#Si queremos que se pase otro mensaje dentro de las llaves lo haremos con format

print(cadena.format("Eduardo"))

#Otro ejemplo

cadena = "Importe Bruto : ${0} + ${1} = Importe neto: {2}"

print(cadena.format(100,21,121))

#Otra forma de hacerlo

cadena = "Importe Bruto : ${bruto} + ${iva} = Importe neto: {neto}"

print(cadena.format(bruto=100,iva=100*16/100,neto=100*16/100+100))

#Método replace: se utiliza para reemplazar subcadenas dentro de una cadena de texto por otra específica

cadena2="Bienvenido a mi aplicación"
print(cadena2.replace("aplicación","Mi página"))

#Otro ejemplo de reemplazo

buscar = "nombre apellido"
reemplazar_por="Juan Perez"

print("Estimado Sr. nombre apellido".replace(buscar, reemplazar_por))

#Métodos Strip, lstrip y rstrip, eliminan caracteres dentro de los extremos de una cadena, por defecto eliminan espacios en blanco, tabulaciones y saltos de línea
cadena = " www.itapizaco.edu.mx "

print(cadena)

print(cadena.strip())

#Eliminar caracteres a la izquierda que coinciden cin el que se introduzce

print(cadena.lstrip(" w"))

#Eliminar caracteres a la derecha que coinciden cin el que se introduzce

print(cadena.rstrip())





