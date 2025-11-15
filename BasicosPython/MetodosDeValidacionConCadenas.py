'''
No: 22
Tema: Métodos de validación con cademas de texto
Autor: Prof. Eduardo67
Fecha: 15/11/2025
'''
palabra1="manejo de cadenas en Python Tema 5"
palabra2="13102026"
palabra3="en este ejemplo tenemos 10 variables"
palabra4="PYTHON"
palabra5="  \n"
palabra6="Python1"

print("\n") #Salto de líunea

#Verifica si una cadema comienza con determinada palabra o caracter

print(palabra1.startswith("manejo")) #Busca desde el principio
print(palabra1.startswith("ne", 2,5)) #Busca la subcadena desde la posición 2 hasta la posición 5


print(palabra1.endswith("Tema 5")) #Identifica si la cadena termina con un determinado sufijo

print(palabra1.isalnum()) #Verifica si todos los caracteres son alfanuméricos, los espacios no son alfanuméricos
print(palabra2.isalnum()) #Verifica si todos los caracteres son alfanuméricos, los espacios no son alfanuméricos

print(palabra4.isalpha()) #Verifica si todos los caracteres son letras del alfabeto
print(palabra2.isdigit()) #Verifica si todos los caracteres son dígitos numéricos
print(palabra4.isdigit()) #Verifica si todos los caracteres son dígitos numéricos

print(palabra3.islower()) #Verifica si todos los caracteres estan en minúscula
print(palabra4.isupper()) #Verifica si todos los caracteres estan en mayúscula
print(palabra5.isspace()) #Verifica si todos los caracteres son espacios en blanco, tabulaciones o saltos de línea
print(palabra6.istitle()) #Verifica si la cadema sigue el formato de título




print("\n") #Salto de líunea
