Algoritmo Aumentosueldo
	
	//Definiciones
	Definir nombre,direccion como Cadena;
	Definir edad,aumento,femenino,masculino Como Entero;
	Definir sueldo,sueldofinal Como Real;
	Definir sexo Como Caracter
	femenino=10
	masculino=5
	
	//Lecturas
	Escribir "Programa para aumentar el sueldo de los trabajadores por sexo";
	Escribir "Ingresar el nombre del trabajador";
	Leer nombre;
	Escribir "Ingresar la edad del trabajador";
	Leer edad;
	Escribir "Ingresar la direcci�n del trabajador";
	Leer direccion;
	Escribir "Ingresar el sexo del trabajador (M,F)";
	Leer sexo;
	Escribir "Ingresar el sueldo del trabajador ($)";
	Leer sueldo;
	
	//C�lculos
	aumento=0
	
	si sexo="F" o sexo="f" Entonces
		aumento=femenino;
	SiNo
		si sexo="m" o sexo="M" Entonces
			aumento=masculino;
		FinSi
	FinSi
	
	sueldofinal=sueldo+(sueldo*aumento/100)
	
	//Impresiones
	Imprimir "Resultados de la conversi�n de datos";
	Imprimir "Nombre del trabajador: ",nombre;
	Imprimir "Edad del trabajador: ",edad;
	Imprimir "Direcci�n del trabajador: ",direccion;
	Imprimir "Sexo del trabajador: ",sexo;
	Imprimir "Nuevo sueldo del trabajador: $",sueldofinal;
	
FinAlgoritmo
