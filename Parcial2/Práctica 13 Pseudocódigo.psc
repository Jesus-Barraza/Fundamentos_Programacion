Algoritmo Calculadora_IMC
	
	//Definiciones
	Definir peso,altura,imc Como Real;
	Definir nombre,resultado como Cadena;
	Definir edad Como Entero;
	
	//Lecturas
	Escribir "Empresa genérica de salud SA de CV";
	Escribir "Ingrese el nombre del paciente";
	Leer nombre;
	Escribir "Ingrese la edad del paciente (en años enteros)";
	Leer edad;
	Escribir "Ingrese el peso del paciente (Kilogramos)";
	Leer peso;
	Escribir "Ingrese la altura del paciente (Metros)";
	Leer altura;
	
	//Cálculos
	imc=peso/altura^2
	
	Si imc<18 Entonces
		resultado="Bajo peso";
	Sino
		Si imc>=18 y imc<25 Entonces
			resultado="Peso normal";
		SiNo
			Si imc>=25 y imc<27 Entonces
				resultado="Sobrepeso I";
			SiNo
				Si imc>=27 y imc<30 Entonces
					resultado="Sobrepeso II";
				SiNo
					Si imc>=30 y imc<35 Entonces
						resultado="Obesidad tipo I";
					SiNo
						Si imc>=35 y imc<40 Entonces
							resultado="Obesidad tipo II";
						SiNo
							Si imc>=40 y imc<=50 Entonces
								resultado="Obesidad tipo III";
							SiNo
								resultado="Probablemente muerto"
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	
	//Impresiones
	Imprimir "Se han finalizado los cálculos";
	Imprimir "Nombre del paciente: ",nombre;
	Imprimir "Edad del paciente: ",edad;
	Imprimir "Indice de masa corporal: ",imc;
	Imprimir "El estatus del paciente es de: ",resultado;
	
FinAlgoritmo
