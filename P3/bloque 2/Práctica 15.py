'''15. Desarrolle la solución para realizar la sumatoria de los números
comprendidos entre el 0 y el 100. Consideraciones:
a. Empezando en 100, con decrementos de 5 en cinco hasta el 0'''

#Algoritmo hasta 100 de 5

#Lecturas
print("Calculando la sumatoria de los números múltiplos de 5 de 100 a 0")

#Cálculos
n=0
for m in range (100,-5,-5):
    n=n+m
    print(str(n))

#Impresiones
print("Listo!")
print("El número resultante de la sumatoria es de: ",str(n),"!")
