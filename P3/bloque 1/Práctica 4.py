'''4.	Diseñar un algoritmo que permita aplicar un descuento en el supermercado de tal forma permita
visualizar el monto a pagar después de aplicar dicho procedimiento.'''

#Algoritmo descuentos

#Lecturas
print("Calculadora de descuentos")
print("Ingrese el precio del producto")
precio=float(input("$"))
print("Ingrese el descuento del producto")
descuento=float(input("%"))

#Cálculos
adescuentar=precio*descuento/100
preciofinal=precio-adescuentar

#Impresiones
print("El descuento es de $",str(round(adescuentar,2)))
print("El precio final es de $",str(round(preciofinal,2)))