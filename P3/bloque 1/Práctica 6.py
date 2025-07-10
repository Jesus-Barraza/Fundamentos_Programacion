'''6.	Determina el área y volumen de un cilindro, aplicando un radio ingresando su valor por 
teclado y también su altura.'''

#Algoritmo cilindro

#Definiciones
pi=3.1415926536

#Lecturas
print("Calculadora de volúmen y superficie de un cilindro")
print("Ingrese el radio de la base del cilindro (no especificar unidades)")
radio =float(input("Unidades: "))
print("Ingrese la altura del cilindro (no especificar unidades)")
altura =float(input("Unidades: "))

#Cálculos
area= pi*radio**2
volumen= pi*radio**2*altura

#Impresiones
print("El área de la base del cilindro es: ", str(area), "unidades cuadradas")
print("El volumen del cilindro es: ", str(volumen), "unidades cúbicas")
