Algoritmo Calificaci�n
	
	//Definiciones
	Definir califica1,califica2,calificaf,califica1f,califica2f como Real;
	Definir peso1,peso2 Como Entero;
	Definir aprobacion,medalla como Cadena;
	peso1=60
	peso2=40
	medalla="Medalla al m�rito acad�mico"
	
	//Lecturas
	Escribir "Programa para calificaci�n!";
	Escribir "Inserta la primera calificaci�n";
	Leer califica1;
	Escribir "Inserta la segunda calificaci�n";
	Leer califica2;
	
	//C�lculos
	califica1f=califica1*peso1/100;
	califica2f=califica2*peso2/100;
	calificaf=califica1f+califica2f;
	
	Si calificaf>=70 Entonces
		aprobacion="aprobado";
	SiNo
		aprobacion="reprobado";
	FinSi
	
	//Impresiones
	Escribir "Resultados finales de la calficaci�n";
	Escribir "La calificaci�n del alumno es de: ",calificaf
	Escribir "Este alumno est�: ",aprobacion
	Si calificaf=100 Entonces
		Escribir medalla
	FinSi
	
FinAlgoritmo
