'''2.	Diseñar una solucion algoritmica que permita calcular el salario mensual de un trabajador, 
teniendo en cuenta los días trabajados y el valor de cada dia. Imprimir el salario mensual.'''

#Algoritmo salario mensual

#Lecturas
print("Calculadora del salario mensual de un trabajador")
print("Ingrese el n° de días trabajados en el mes")
dias=int(input("Dias: "))
print("Ingrese el n° de horas trabajadas por dia")
horas=float(input("Horas: "))
print("Ingrese el salario en hora de los trabajadores")
valor_horas=float(input("$ "))

#Cálculos
salario_mensual=(dias*horas*valor_horas)

salario_mensual=round(salario_mensual,2)

#Impresiones
print("El salario mensual del trabajador es de: $",str(salario_mensual))
