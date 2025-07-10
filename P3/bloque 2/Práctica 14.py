'''14. Construir la solución para que con base al salario de un trabajador realice un descuento
como aportación a la Cruz Roja. Considere lo siguiente:
a. Si el sueldo es superior a $1000 semanales se le retendrá un 10% sobre el salario.
b. Si el salario está comprendido entre $500 y $1000 se le retendrá el 7%.
c. Si el salario es menor de $500, se le retendrá solamente el 3%.
d. El programa deberá de imprimir el tipo descuento realizado, así como finalmente el sueldo neto.'''

#Algoritmo cruz_roja

#Definiciones
retencion=3
retencion500=7
retencion1000=10

#Lecturas
print("Cálculo de retención del salario de la cruz roja")
salario=float(input("Ingrese el salario del trabajador: $"))

salario=round(salario,2)

#Cálculos
if salario>=1000:
    salariofinal=salario-(salario*retencion1000/100)
elif salario>=500:
    salariofinal=salario-(salario*retencion500/100)
else:
    salariofinal=salario-(salario*retencion/100)

#Impresiones
print("Finalizó el cálculo de la retención del salario")
print("El salario final es de: $",str(round(salariofinal,2)))
print("Fin del programa")