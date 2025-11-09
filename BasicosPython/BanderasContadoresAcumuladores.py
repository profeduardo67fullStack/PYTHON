'''
No: 13
Tema: Verificando conceptos como banderas, contadores y acumuladores
multiplica por 2. Se sumarán los multiplicados que correspondan a multiplicadores impares.
Autor: Prof. Eduardo67
Fecha: 09/11/2025
'''
import random
print("INICIO")
sacaste_cinco=False
cuenta_cincos=0
for i in range(3):
    dado=random.randrange(1,7)
    print(f"tirada{i+1}: {dado}")
    if dado==5:
        sacaste_cinco=True
        cuenta_cincos+=1
if sacaste_cinco:
    print("HAS TIRADO UN 5 ")
else:
    print("NUNCA SE TIRO UN 5 ")

print(f"El total han(n) salido {cuenta_cincos} números 5 ")

