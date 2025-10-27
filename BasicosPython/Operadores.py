'''
No: 2
Tema: Probando los operadores
Autor: Prof. Eduardo67
Fecha: 27/10/2025

'''

x=2; y=3

print("Operadores Relacionales con los valores: x = " , 2 , "y = " , y)
print("x == y = ", x==y) # False
print("x != y = ", x!=y) # True
print("x > y = ", x>y) # False
print("x < y = ", x<y) # True
print("x >= y = ", x>=y) # False
print("x <= y = ", x<=y) # True


#Notemos que para tipos Boolenos True es igual a 1

print(True == 1) # True
print(True > 0.999) # True

print("abc" < "abd") # True
print("A" < "a") # True

#Por que el valor unicode de A es menor al valor unicode de a

print("El valor Unicode o ASCII de la A es: ", ord('A')) #65
print("El valor Unicode o ASCII de la A es: ", ord('a')) #97

#Tambien podemos comparar un vector (Coordenadas)

print([3,4] >= [3,5]) #False


x=10
y=2

#Comprobando la precedencia de los operadores artiméticos

calif1 = 100.0
calif2 = 70.0

promedio = (calif1+calif2) / 2

aprobado = promedio >= 70.0
excelente = promedio > 90.0 and calif1 > 85 and calif2 > 85

print("Promedio: ", promedio)
print("Aprobado: ", aprobado)
print("¿Desempeño Excelente?: ", excelente)

