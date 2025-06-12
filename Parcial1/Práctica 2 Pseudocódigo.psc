Algoritmo salario_mensual
	
	//definiciones
	Definir dias Como Entero;
	Definir valor_dia,salario Como Real;
	
	//Lecturas
	Escribir "Ingresa el n° de días trabajados en el mes";
	Leer dias;
	Escribir "Ingresa el salario diario del trabajador ($)";
	Leer valor_dia;
	
	//Cálculos
	salario=dias*valor_dia;

	//Impresiones
	Imprimir "El salario del trabajador de este mes es de: $",salario;
	
FinAlgoritmo
