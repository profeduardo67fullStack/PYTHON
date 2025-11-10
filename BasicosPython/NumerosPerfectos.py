'''
No: 14
Tema: Números Perfectos
multiplica por 2. Se sumarán los multiplicados que correspondan a multiplicadores impares.
Autor: Prof. Eduardo67
Fecha: 09/11/2025
'''
n=int(input("¿Cuantos números deseas? "))
suma=0
salida=""
for i in range(1,n):
    for j in range(1,i-1):
        if(i%j==0):
            suma+=j
    if(i==suma):
        salida=salida+str(i)+","
print(f'Los números perfectos que existen entre 1 y {n} son ---> {salida}')
