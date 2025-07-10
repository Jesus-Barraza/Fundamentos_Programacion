'''18. Crear una solucion que solicite un numero entero positivo comprendido
entre el 1 al 10 (solo esos numeros), apartir de este numero calcular e imprimir
la tabla de multiplicar correspondiente. Nota: si se ingresa cualquier otro numero
no se calcula e imprime la tabla de multiplicar.'''

#Algoritmo tablas de multiplicar

#Definiciones
tabla=0
numero=1

#Lecturas
print("Tablas de multiplicar")
while tabla>10 or tabla<1:
    print("Ingrese un número para calcular su tabla (1 - 10)")
    tabla=int(input())
    if tabla>10 or tabla<1:
        print("Número no válido, intente de nuevo")

#Cálculos
print("tabla del",str(tabla))
for numero in range(1,11):
    print(str(tabla),"por",str(numero),"es",str(tabla*numero)) 
