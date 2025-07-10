'''17. Diseñe un solución que imprima todos los números naturales que
hay desde la unidad hasta un número que introducimos por teclado.'''

#Algoritmo naturales

#Definiciones
n=0

#Lecturas
print("Todos los numeros naturales del 0 a...")
print("Ingrese el número hasta el que desea llegar")
l=int(input())

#Cálculos
while n<l+1:
    print(str(n))
    n=n+1

#Impresiones
print("Listo!")
