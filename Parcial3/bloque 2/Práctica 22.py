'''22. Construir la solución para calcular e imprimir las potencias de dos empezando en
0 hasta el 10. Consideraciones:
a. Utilizar un ciclo “Repetir” para solucionar el problema.
b. Imprimir el número, potencia y resultado en cada uno de los pasos.'''

#Algoritmo potencias de 2 parte 3

#Definiciones
z=0
a=0

#Lecturas
print("Calculando las potencias de 2...")

#Cálculos
while z<11:
    a=2**z
    print("2 elevado a la",str(z),"es igual a",str(a))
    z=z+1

#Impresiones
print("Listo!")

'''Hay un pequeño problema, este código es literalmente una
copia del 2-11, esto se debe a que Python no maneja el
ciclo del "Repetir - Mientras que", así que su simil,
"Mientras - Finmientras", será usado para esta actividad'''