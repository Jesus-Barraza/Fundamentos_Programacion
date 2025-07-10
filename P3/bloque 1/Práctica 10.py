'''10.	Defina un algoritmo que permita calcular el nuevo salario de un trabajador si a este le 
incrementaron su sueldo en un 25% adicional a su sueldo anterior.'''

#Algoritmo salarios

#Definiciones
aumento=25

#Lecturas
print("Cálculo de salarios con un aumento del 25%")
print("Ingresa el salario actual")
salario=float(input("Salario: "))

#Cálculos
salariofinal=salario+((salario*aumento)/100)

#Impresiones
print("El salario final es: $",str(round(salariofinal,2)))