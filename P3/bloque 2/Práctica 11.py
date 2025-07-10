'''11. Realizar una solución algoritmica para que lea del teclado el nombre, edad,
dirección, sexo y sueldo de un trabajador. Almacenar lo anterior en variables
adecuadas (tipo de variable). En función al sexo, si es mujer otorgarle un aumento
al sueldo del 10% y en caso contrario si es hombre solamente el 5% de aumento. Al
final imprimir en pantalla el sueldo final ya con el aumento.'''

#Algoritmo aumento de sueldo

#Definiciones
femenino=10
masculino=5
valor_no_valido=0

#Lecturas
print("Programa para aumentar el sueldo de los trabajadores por sexo")
print("Ingrese el nombre del trabajador")
nombre=input()
print("Ingrese la edad del trabajador")
edad=input()
print("Ingresa el domicilio del trabajador")
domicilio=input()
print("Ingresa el sexo del trabajador")
sexo=input("M para masculino y F para femenino: ")
print("Ingresa el sueldo del trabajador")
sueldo=float(input("$ "))

#Cálculos
sexo=str.upper(sexo)

if sexo=="F":
    aumento=femenino
elif sexo=="M":
    aumento=masculino
else:
    sexo="valor no válido"
    aumento=valor_no_valido

sueldofinal=sueldo+(sueldo*(aumento/100))

#Impresiones
print("Resultados de la conversión de datos:")
print("Nombre del trabajador:",nombre)
print("Edad del trabajador:",edad)
print("Domicilio del trabajador:",domicilio)
print("Sexo del trabajador:",str(sexo))
print("Nuevo salario del trabajador: $",str(round(sueldofinal,2)))
