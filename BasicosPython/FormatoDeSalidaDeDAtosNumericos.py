'''
No: 26
Tema: Formato De salida de datos numéricos
Autor: Prof. Eduardo67
Fecha: 16/11/2025
'''

#Formateo de salida de datos numéricos


# SECCION1

archivo ="NTUSER.DAT"

#La r significa que es una cadena cruda, evita que en Windows las barras invertidas sean interpretadas como caracteres de escape
#Y la f significa cadena formateada, podemos incruitar cuestiones de python directamete

path = rf'C:\Users\cosca\{archivo}'

print(path)

#Formato de datos numericos

pi=3.14159265359
piformateado=f"Valor redondeado = {pi:.3f}"#Vamos a formateas a pi, los dos puntos introduce las especificaciones de formatos, .3 especifica que queremos 3 decimales, y
#f que es un valor de punto flotante
print(piformateado)


#Formato de como alinear y rellenar cadenas

lenguaje="Python"
formateado = f"Bienvenido a, {lenguaje:=>10}"#El signo de igual es el caracter que se utilizará para completar el espacio, el mayor indica una alineación a la derecha,
#y 10 el ancho total del campo
print(formateado)

#Rellenar número con ceros iniciales

num_formateado = 42
num_formateado = f"numero : {num_formateado:06}"#El cero es el caracter de relleno y el 6 es el total del campo
print(num_formateado)


#Alenear pero a la izquierda

plataforma = "MOOC"
palabraformateada = f"Plataforma: {plataforma:_<10}"
print(palabraformateada)

