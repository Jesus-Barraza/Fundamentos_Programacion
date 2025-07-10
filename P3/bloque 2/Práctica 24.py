'''24. Construya una solución en Pseudocódigo que permita calcular y mostrar el Total a Pagar por las compras/ventas
de los productos determinados.
Consideraciones:
• Para calcular el total a pagar es necesario considerar los siguientes formulas: Valor (10%)
o Sub-Total=Precio Unitario * Cantidad
o Total a pagar= Sub-Total – Descuento + IVA
• Se otorga un 10% de descuento si se compra más de 5 artículos, en caso contrario 5%.
• Utilizar un ciclo “Repetir/Mientras” para realizar el proceso N veces, mientras el usuario responda a la pregunta
¿Deseas capturar otro? (Si/No).
• Al final mostrar el Total a pagar Acumulado, así como el numero de veces que se realizo el proceso de compra/venta.'''

#Algoritmo paga infinita

#Importaciones
import os 

#Definiciones
repeticion="SI"
iva=16
n=0
preacu=0

#Escrituras
print("Tienda de la esquina que no importa su nombre SA de CV")

#Ciclo entero pt.1
while repeticion=="SI":
    #Limpieza de pantalla
    os.system("clear")
    os.system("cls")

    #Lecturas
    print("Ingrese la descripción/el nombre del producto")
    desc=input()
    print("Ingrese el código del producto")
    code=int(input())
    print("Ingresa la cantidad del producto")
    cant=int(input())
    print("Ingrese el precio unitario del producto")
    precuni=float(input("$"))

    #Cálculos
    if cant>5:
        desc=10
    else:
        desc=5
    
    prec=precuni*cant
    predesc=prec*desc/100
    preiva=(prec-desc)*iva/100
    pretot=prec-predesc+preiva
    preacu=preacu+pretot
    n=n+1

    #Impresiones pt.1
    print("Nombre/Descripción del producto: ",desc)
    print("Código del producto: ",str(code))
    print("Precio neto: $",str(round(prec,2)))
    print("Descuento aplicado: $",str(round(predesc,2)))
    print("IVA: $",str(round(preiva,2)))
    print("Precio total: $",str(round(pretot,2)))

    #Ciclo entero pt.2
    print("")
    print("")
    print("")
    print("¿Desea capturar otro producto?")
    repeticion=str.upper(input("(SI/NO) "))

#Impresiones pt.2
print("De un total de",str(n),"productos únicos, el total a pagar es de: $",str(round(preacu,2)))
