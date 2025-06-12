Algoritmo salario
	
	//definiciones
	Definir salari,aumento,novo_salario Como Real;
	aumento=25;
	
	
	//Lecturas
	Escribir "Introducir el salario a aumentar";
	Leer salari;

	//Cálculos
	novo_salario=salari+(salari*aumento/100);

	//Impresiones
	Imprimir "El nuevo salario del trabajador es del: $",novo_salario;

FinAlgoritmo
