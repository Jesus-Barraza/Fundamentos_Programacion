'''19. Desarrollar la solución para crear una nota de venta. La solución deberá de solicitar
el # de artículos vendidos, el código de cada artículo, la descripción o nombre del artículo
y el precio unitario. Calcular e imprimir el precio neto, Descuento, IVA, total a pagar.
Considere lo siguiente:
a. Si el # de artículos es superior a 10 se aplica el 10% de descuento sobre el precio neto.
b. El precio neto es igual al # de artículos por el precio unitario.
c. El IVA es del 16% y se aplica sobre el precio neto.
d. El total a pagar es igual al precio neto – descuento + IVA'''

#Algoritmo nota de venta

#Definiciones
unitario=0
cantidad=0
iva=16

#Lecturas
print("Nota de venta")
print("Ingrese la descripción del producto")
descripcion=input()
print("Ingrese el código del producto")
codigo=input()
print("Ingrese el precio unitario")
unitario=float(input("$"))
print("Ingrese la cantidad")
cantidad=int(input())

#Cálculos
descuento=0
if cantidad>10:
    descuento=10

neto=cantidad*unitario
descontar=neto*descuento/100
iva=(neto-descontar)*iva/100
total=neto-descontar+iva

#Impresiones
print("Nombre/descripción del producto:",descripcion)
print("Código del producto:",codigo)
print("Precio neto: $",str(round(neto,2)))
print("Descuento: $",str(round(descontar,2)))
print("IVA: $",str(round(iva,2)))
print("Total a pagar: $",str(round(total,2)))

#¿Cuál es el propósito de la variable "iva" en el código?
#Deja te respondo recomendados del algoritmo, el iva cumple con el propósito fundamental de impuesto por el producto
# y se calcula en base al precio neto del producto.