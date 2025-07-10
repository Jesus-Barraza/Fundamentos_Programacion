Algoritmo cilindro
	
	//definiciones
	Definir area,volumen,altura,radio Como Real;
	
	//Lecturas
	Escribir "Ingresa la altura del cilindro (cualquier unidad sin esp. con decimales)";
	Leer altura;
	Escribir "Ingresa el radio de la base del cilindro (cualquier unidad sin esp. con decimales)";
	Leer radio;
	
	//Cálculos
	area=(2*pi*(radio^2))+(2*pi*radio*altura);
	volumen=pi*(radio^2)*altura;

	//Impresiones
	Imprimir "La superficie de área del cilindro es de: ",area," unidades cuadradas";
	Imprimir "El volumen del cilindro es de: ",volumen," unidades cubicas";

FinAlgoritmo
