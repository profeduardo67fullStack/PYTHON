'''
No: 16
Tema: Funciones en Python con return
multiplica por 2. Se sumarán los multiplicados que correspondan a multiplicadores impares.
Autor: Prof. Eduardo67
Fecha: 09/11/2025
'''

distancia=0
velocidad=0

def convertir_a_metros(kilometros):
    metros=kilometros*1000
    print(f"Los kilómetros mandados a metros son: {metros}")
    return metros #Regresamos el valor obtenido para su uso desde la llamada


metros=convertir_a_metros(1)
velocidad=metros/10
print(f"La velocidad a la que te desplazas es: {velocidad} metros/segundos" )





