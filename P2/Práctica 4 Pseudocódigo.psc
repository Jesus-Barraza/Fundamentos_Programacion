Algoritmo cruz_roja
	
	//Definiciones
	Definir salario,salariofinal Como Real;
	Definir retencion,retencion500,retencion1000 Como Entero;
	retencion=3
	retencion500=7
	retencion1000=10
	
	//Lecturas
	Escribir "C�lculo de retenci�n del salario en la Cruz Roja";
	Escribir "Ingrese el salario del trabajador ($)";
	Leer salario;
	
	//C�lculos
	Si salario>=1000
		salariofinal=salario-(salario*retencion1000/100)
	SiNo
		Si salario>=500 y salario<1000
			salariofinal=salario-(salario*retencion500/100)
		SiNo
			salariofinal=salario-(salario*retencion/100)
		FinSi
	FinSi
	
	//Impresiones
	Imprimir "Los c�lculos han finalizado"
	Imprimir "El salario descontado del trabajador ser� de: $",salariofinal
	
FinAlgoritmo
