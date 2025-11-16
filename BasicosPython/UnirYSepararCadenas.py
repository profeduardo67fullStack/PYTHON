'''
No: 27
Tema: Introducción Unir y separar una cadena
Autor: Prof. Eduardo67
Fecha: 16/11/2025
'''

#Método de unión


#Concatena todos los elementos insertando la cadena sobre la que se llama numero en cada elemento iterable
formato_factura = ("No. 2025-0","-1010 (ID: )",")")
numero= "275"
numero_factura = numero.join(formato_factura)
print(numero_factura)

#Ejemplo 2
palabras = ["Hola", "Mundo", "Python"]
frase = "-".join(palabras)

print(frase)