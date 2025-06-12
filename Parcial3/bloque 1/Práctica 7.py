'''7.	Diseñar un algoritmo que lea por consola el valor de una factura, en este caso aplicaremos 
un impuesto adicional del 18%. Imprimir el valor factura ya con el impuesto.'''

#Algoritmo factura

#Definiciones
impues= 18

#Lecturas
print("Cálculo de la factura con impuesto")
print("Ingrese el valor original de la factura")
valor=float(input("$"))

#Cálculos
impuesto= valor*impues/100
total= valor+impuesto

#Impresiones
print("El valor del impuesto es de $",str(round(impuesto,2)))
print("El valor total de la factura es de $",str(round(total,2)))