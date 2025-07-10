'''20. Construir la solución para calcular e imprimir las potencias de dos
empezando en 0 hasta el 10. Consideraciones:
a. Utilizar un ciclo “Para” para solucionar el problema.
b. Imprimir el número, potencia y resultado en cada uno de los pasos.'''

#Algoritmo potencias de 2 parte 1

#Definiciones
z=0

#Lecturas
print("Calculando las potencias de 2...")

#Cálculos
for z in range(0,11):
    a=2**z
    print("2 elevado a la",str(z),"es",str(a))

#Impresiones
print("Listo!")
