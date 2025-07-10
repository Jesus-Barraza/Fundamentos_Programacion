'''3.	Diseñar la solucion algoritmica que solicite 2 numeros enteros y a partir de estos numeros 
calcular e imprimir las cuatro operaciones básicas.'''

#Algoritmo operaciones

#Lecturas
print("Calculadora de operaciones")
print("Ingrese 2 números enteros")
num1=input("El primer número (en reales): ")
num2=input("El segundo número (en reales): ")

#Cálculos
suma=int(num1)+int(num2)
resta=int(num1)-int(num2)
multiplica=int(num1)*int(num2)
divide=int(num1)/int(num2)

#Salidas
print("La suma de los números es: ",str(suma))
print("La resta de los números es: ",str(resta))
print("La multiplicación de los números es: ",str(multiplica))
print("La división de los números es (aproximadamente): ",str(round(divide,3)))
