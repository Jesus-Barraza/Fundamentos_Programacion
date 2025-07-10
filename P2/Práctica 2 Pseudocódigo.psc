Algoritmo Calificación
	
	//Definiciones
	Definir califica1,califica2,calificaf,califica1f,califica2f como Real;
	Definir peso1,peso2 Como Entero;
	Definir aprobacion,medalla como Cadena;
	peso1=60
	peso2=40
	medalla="Medalla al mérito académico"
	
	//Lecturas
	Escribir "Programa para calificación!";
	Escribir "Inserta la primera calificación";
	Leer califica1;
	Escribir "Inserta la segunda calificación";
	Leer califica2;
	
	//Cálculos
	califica1f=califica1*peso1/100;
	califica2f=califica2*peso2/100;
	calificaf=califica1f+califica2f;
	
	Si calificaf>=70 Entonces
		aprobacion="aprobado";
	SiNo
		aprobacion="reprobado";
	FinSi
	
	//Impresiones
	Escribir "Resultados finales de la calficación";
	Escribir "La calificación del alumno es de: ",calificaf
	Escribir "Este alumno está: ",aprobacion
	Si calificaf=100 Entonces
		Escribir medalla
	FinSi
	
FinAlgoritmo
