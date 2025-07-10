'''16.Construir la solución para encontrar la sumatoria de los números múltiplos
de 5, comprendidos entre el numero 1 al 100, es decir 5+10+15+…+100. La solución
deberá imprimir cada uno de los números en cuestión y finalmente la sumatoria.'''

#Algoritmo multiplos de 5

#Definiciones
m=0
n=0

#Lecturas
print("Calculando los múltiplos de 5...")

#Cálculos
while m<=100:
    n=n+m
    print(str(m))
    m=m+5

#Impresiones
print("Listo!")
print("El número resultante de la sumatoria es de: ",str(n),"!")

'''Este código es similar al de la práctica 2-5, pero en este caso se utiliza un ciclo while para calcular los múltiplos de 5 de 0 a 100.
BTW hola profe aún sigo sin entender nada de esto, pero aquí sigo intentando.'''
