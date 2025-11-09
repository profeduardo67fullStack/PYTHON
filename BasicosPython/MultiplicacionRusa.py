'''
No: 11
Tema: Multiplicación rusa, "El primer número (multiplicando) se divide entre dos y el segundo número (Multiplicador) se
multiplica por 2. Se sumarán los multiplicados que correspondan a multiplicadores impares.
Autor: Prof. Eduardo67
Fecha: 09/11/2025
'''

n1=int(input("Dame un número: " ))
n2=int(input("Dame otro númeoro: " ))
suma=0
while n1>=1:
    if n1%2 !=0:
        suma=suma+n2
    n1=int(n1/2)
    n2=n2*2
print(f'El resultado de la multiplicación es = {suma}')


