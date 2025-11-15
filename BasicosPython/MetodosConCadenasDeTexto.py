'''
No: 21
Tema: Métodos con cademas de texto
Autor: Prof. Eduardo67
Fecha: 15/11/2025
'''

palabra="manejo de cadenas en Python"
factura="20890"

print("\n") #Salto de línea

print(palabra.capitalize()) #Devuelve la primera letra en mayúsculas
print(palabra.lower()) #Devuelve la primera letra en mayúsculas
print(palabra.upper()) #Devuelve la primera letra en mayúsculas

palabra2="Esto Es Un Texto Como Título"
print(palabra2.swapcase()) #Invierte mayosculas y minúsculas

palabra3="esto es en eexto eomo eítulo"
print(palabra3)
print(palabra2.title()) #Pone el texto en formato de título


print(palabra2.__len__()) #Ontener la longitud de la cadena


print(palabra2.center(50)) #Centra el texto en un ncho específico
print(palabra2.center(50,"-")) #Centra el texto en un ncho específico, y pone un relleno

print(palabra2.ljust(50)) #Alinea un texto a la izquierda dentro de un ancho específico
print(palabra2.ljust(50,"*")) #Alinea un texto a la izquierda dentro de un ancho específico, con relleno

print(palabra2.rjust(50,"*")) #Alinea un texto a la derecha dentro de un ancho específico, con relleno

print(factura.zfill(8))#Rellena con ceros hasta alcanzar el número del parámetro

#Los métodos pueden agregarse en cascada

cadena="SiguE aprEnDiendO"

print("\ncadena original: " ,cadena)
print("\ncadena original: " ,cadena.title())
print("\ncadena original: " ,cadena.title().swapcase(),"\n")
print("\ncadena original: " ,cadena.lower().swapcase().center(23,"*"),"\n")





print("\n")


