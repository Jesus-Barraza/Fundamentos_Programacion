'''12. Desarrollar la solución para que dadas 2 calificaciones numéricas obtenga el
promedio de ambas considerando que la primera calificación esta ponderada a un 60%
y la segunda a un 40%. El programa deberá de considerar el promedio para imprimir en
pantalla lo siguiente:
a. “Aprobado”, si el promedio es de 70 o más.
b. “Medalla al Mérito Ácademico”, si es 100.
c. “No aprobado”'''


#Algoritmo calificación

#Definiciones
peso1=60
peso2=40
medalla="Medalla al mérito académico"

#Lecturas
print("Programa para calcular la calificación!")
print("Ingresa la primera calificación (1-100)")
calificacion1=float(input())
print("Ingresa la segunda calificación (1-100)")
calificacion2=float(input())

#Cálculos
calificacionfinal=(calificacion1*peso1+calificacion2*peso2)/100

round(calificacionfinal,1)

if calificacionfinal>=70:
    aprobacion="aprobado"
else:
    aprobacion="reprobado"

#Impresiones
print("Resultados de la calificación:")
print("Calificación final:",str(calificacionfinal))
print("Este alumno está",aprobacion)
if calificacionfinal>=100:
    print(medalla)
