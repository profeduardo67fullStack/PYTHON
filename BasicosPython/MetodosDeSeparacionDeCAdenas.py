'''
No: 28
Tema: Métodos para separar cadenas
Autor: Prof. Eduardo67
Fecha: 16/11/2025
'''

#Como dividir cadenas enPython

#Método PARTITION()
tupla = "http://www.itapizaco.edu.mx".partition("://")#Parte la cadena en tres partes, antes del separador, el separador y después del separador
print(tupla)
protocolo, separador, dominio = tupla#Agregamos cada una de la tupla a variables separadas
print("Protocolo : {0}\Dominio: {1}".format(protocolo, dominio))


#MÉTODO SPLITLINES, Su trabajo es dividir la cadena de una lista de lineas individuales


#Nos genera una lista con los elementos de cada linea de un párrafo, eliminando los caracteres de salto de línea por defecto
texto = """liena1
Linea 2
Linea 3
Linea 4
"""
print(texto.splitlines())

texto="parrafo 1\n parrafo 2\n parrafo 3"
print(texto.splitlines())

#METODO SPLIT()

cadena = "yo programo en Python"
print(cadena.split())#Divide la cadena por cualquier secuencia con espacios en blanco
mi_cadena = "Manzanas,Peras,Naranjas,Platanos,Tunas"
print(mi_cadena.split(","))#Divide la cadena por el delimitador dado
print(mi_cadena.split(",",maxsplit=2))#Le indica que ralice como máximo dos cortes y el resto de la cadena permanecerá como un solo elemento en la lista

animales = "perro,gato,raton,cabello"
print(animales.split("a"))

color_string="azul#rojo#amarillo#naranja"
colores = color_string.split("#",0)
print(colores)


#SPLIT VS RSPLIT

animales = "perro,gato,raton,caballo"
print(animales.split(None,2))#Se harían los cortes de izquierda a derecha

animales = "perro,gato,raton,caballo"
print(animales.rsplit(None,2))#Se harían los cortes de izquierda a derecha

animales = "perro,gato,raton,caballo"
print(animales.rsplit(",",maxsplit=2))




