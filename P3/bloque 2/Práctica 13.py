'''13. Construir la solución para que dado el precio unitario de un artículo X y
el número de artículos comprados. Calcule e imprima el Costo total a pagar por los
artículos comprados, considerando que se le asignara un descuento del 10 % si son
más de 10 artículos y 5 % si la compra de artículos en menor a 10.'''

#Algoritmos precios

#Definiciones
descuento10=10
descuento=5

#Lecturas
print("Programa para calcular el precio de un producto")
print("Ingresa el números del producto a comprar (unidades)")
unidades=int(input())
print("Ingresa el precio del producto")
precio=float(input("$ "))

preciobruto=precio*unidades

#Cálculos
if unidades>=10:
    adescontar=preciobruto*(descuento10/100)
    preciofinal=preciobruto-adescontar
else:
    adescontar=preciobruto*(descuento/100)
    preciofinal=preciobruto-adescontar

#Impresiones
print("Resultados de la compra:")
print("El precio original es de: $",str(round(preciobruto,2)))
print("Se descontó: $",str(round(adescontar,2)))
print("El precio a pagar es de: $",str(round(preciofinal,2)))
print("Gracias por su compra")
