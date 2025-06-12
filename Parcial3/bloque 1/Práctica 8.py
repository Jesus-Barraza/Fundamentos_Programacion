'''8.	Realizar un algoritmo de tipo de cambio de moneda sabiendo que 1 dólar es igual a $20.72 mexicanos.'''

#Algoritmo peso a dolar

#Definiciones
valor_peso=20.72

#Lecturas pt.1
print("Cálculo de la conversión de pesos a dólares")
print("Elije el tipo de moneda a convertir")
print("1. Pesos a dólares")
print("2. Dólares a pesos")
opcion=int(input(""))

if opcion==1:
    #Lecturas pt.2
    print("Ingrese la cantidad de pesos a convertir")
    pesos= float(input("$ "))
    
    #Cálculos pt.1
    dolares= pesos/valor_peso

    #Impresiones pt.1
    print("La cantidad de dólares es de $",str(round(dolares,2)))
elif opcion==2:
    #Lecturas pt.3
    print("Ingrese la cantidad de dólares a convertir")
    dolares= float(input("$ "))
    
    #Cálculos pt.2
    pesos= dolares*valor_peso

    #Impresiones pt.2
    print("La cantidad de pesos es de $",str(round(pesos,2)))
else:
    print("Opción no válida")