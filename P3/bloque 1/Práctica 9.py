'''9.	Defina un algoritmo que permita calcular la nota final de un alumno, teniendo en cuenta que ha 
realizado 3 evaluaciones y que cada evaluación esta sometida a un peso , el cual es: 
    a.	La primera nota tiene un peso de 25%. 
    b.	La segunda nota tiene un peso de 45%. 
    c.	La tercera nota tiene un peso de 30%'''

#Algoritmo notas

#Definiciones
pesoeva1=25
pesoeva2=45
pesoeva3=30

#Lecturas
print("Cálculo de notas basadas en su evañiación")
print("Ingresa las 3 calificaciones de la evaluación (del 1 al 100)")
eva1=float(input("Evaluación 1: "))
eva2=float(input("Evaluación 2: "))
eva3=float(input("Evaluación 3: "))

#Cálculos
notafinal=((eva1*pesoeva1)+(eva2*pesoeva2)+(eva3*pesoeva3))/100

#Impresiones
print("La nota final es: ",str(round(notafinal,1)))
