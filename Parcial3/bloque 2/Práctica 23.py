'''23.Crear una solución que permita calcular e imprimir el IMC de una persona.
Solicitar el Nombre Completo, edad, estatura y peso. Además el programa debera de
imprimir las siguientes leyendas según el IMC:
a.“Peso Normal” de 18 a 25
b.“Sobrepeso I” de 25 a 26.9
c.“Sobrepeso II” de 27 a 29.9
d.“Obesidad tipo I” de 30 a 34.9
e.“Obesidad tipo II” de 35 a 39.9
f.“Obesidad tipo III” de 40 a 50

Notas: Realizar el proceso anterior mientras que el usuario asi lo considere.'''

#Algoritmo calculadora IMC

#Lecturas
print("Empresa genérica de salud SA de CV")
print("Ingrese el nombre del paciente")
nombre=input()
print("Ingrese la edad del paciente (años)")
edad=input()
print("Ingres el peso del paciente (kg)")
peso=float(input())
print("Ingrese la altura del paciente (metros)")
altura=float(input())

#Cálculos pt.1
print("¿Desea calcular el Índice de Masa Corporal (IMC)?")
confirmado=input("(Si/No) ")

confirmado=str.upper(confirmado)

if confirmado=="SI":

    imc=peso/altura**2

    if imc<18:
        resultado="Bajo peso"
    elif imc>=18 and imc<25:
        resultado="Peso normal"
    elif imc>=25 and imc<27:
     resultado="sobrepeso I"
    elif imc>=27 and imc<30:
     resultado="sobrepeso II"
    elif imc>=30 and imc<35:
        resultado="Obesidad tipo I"
    elif imc>=35 and imc<40:
        resultado="Obesidad tipo II"
    elif imc>=40 and imc<50:
        resultado="Obesidad tipo III"
    else:
        resultado="Mayor a Obesidad tipo III"
else:
    imc=0.0
    resultado="(No se realizó el proceso del cálculo del IMC)"


#Impresiones
print("Se han realizado los cálculos")
print("Nombre del paciente: ",nombre)
print("Edad del paciente: ",edad)
print("Índice de masa corporal del paciente: ",str(round(imc,1)))
print("El paciente se encuentra en estado de",str(resultado))

#RIP llenado automático de VSCode, nos vemos el 5 de abril (?