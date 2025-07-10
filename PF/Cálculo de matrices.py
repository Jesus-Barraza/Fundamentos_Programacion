'''multiplicacion de matrices'''
#importante descargar numpy
import numpy as np
import os
start=True

while start==True:
    os.system("cls")
    print("\n\t\t CALCULADORA DE MATRICES \n\t 1. suma \n\t 2. resta \n\t 3. multiplicación \n\t 4. división \n\t 5. salir")
    
    try:
        eleccion=int(input("\n\t eliga una opcion: "))
    except TypeError:
        print("Debes de convertir el numero a entero")
    except ValueError:
        print("Debes de introducir un numero no se puede convertir un numero a cadena")

    #suma
    if eleccion==1:
        os.system("cls")
        
        def leer_matriz(filas, colum):
            matrix = []
            for i in range(filas):
                row = []
                for j in range(colum):
                    while True:
                        try:
                            value = int(input(f"Ingrese un valor para la matriz[{i}][{j}]: "))
                            break
                        except ValueError:
                            print("Debes introducir un número entero válido.")
                    row.append(value)
                matrix.append(row)
            return matrix

        def sumar_matrices(matrix1, matrix2):
            result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
            for i in range(len(matrix1)):
                for j in range(len(matrix1[0])):
                    result[i][j] = matrix1[i][j] + matrix2[i][j]
            return result

        def imprimir_matriz(matriz):
            for fila in matriz:
                print(" ".join(map(str, fila)))

        # Solicitar dimensiones
        while True:
            try:
                filas = int(input("Ingrese el número de filas: "))
                columnas = int(input("Ingrese el número de columnas: "))
                break
            except ValueError:
                print("Por favor, ingrese números enteros para filas y columnas.")

        # Leer las dos matrices
        print("Matriz 1")
        matriz1 = leer_matriz(filas, columnas)

        print("Matriz 2")
        matriz2 = leer_matriz(filas, columnas)

        # Sumar matrices
        resultado = sumar_matrices(matriz1, matriz2)

        # Mostrar resultado
        print("Resultado de la suma:")
        imprimir_matriz(resultado)

        input("Presione ENTER para continuar...")

    #resta
    elif eleccion==2:
        os.system("cls")

        def leer_matriz(filas, colum):
            matrix = []
            for i in range(filas):
                row = []
                for j in range(colum):
                    while True:
                        try:
                            value = int(input(f"Ingrese un valor para la matriz[{i}][{j}]: "))
                            break
                        except ValueError:
                            print("Debes introducir un número entero válido.")
                    row.append(value)
                matrix.append(row)
            return matrix

        def restar_matrices(matrix1, matrix2):
            result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
            for i in range(len(matrix1)):
                for j in range(len(matrix1[0])):
                    result[i][j] = matrix1[i][j] - matrix2[i][j]
            return result

        def imprimir_matriz(matriz):
            for fila in matriz:
                print(" ".join(map(str, fila)))

        # Solicitar dimensiones
        while True:
            try:
                filas = int(input("Ingrese el número de filas: "))
                columnas = int(input("Ingrese el número de columnas: "))
                break
            except ValueError:
                print("Por favor, ingrese números enteros para filas y columnas.")

        # Leer las dos matrices
        print("Matriz 1")
        matriz1 = leer_matriz(filas, columnas)

        print("Matriz 2")
        matriz2 = leer_matriz(filas, columnas)

        # Restar matrices
        resultado = restar_matrices(matriz1, matriz2)

        # Mostrar resultado
        print("Resultado de la resta:")
        imprimir_matriz(resultado)

        input("Presione ENTER para continuar...")

    #multiplicacion
    elif eleccion==3:
            os.system("cls")
        
            def leer_matriz(filas, colum):
                matrix = []
                for i in range(filas):
                    row = []
                    for j in range(colum):
                        while True:
                            try:
                                value = int(input(f"Ingrese un valor para la matriz[{i}][{j}]: "))
                                break
                            except ValueError:
                                print("Debes introducir un número entero válido.")
                        row.append(value)
                    matrix.append(row)
                return matrix

            def sumar_matrices(matrix1, matrix2):
                result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
                for i in range(len(matrix1)):
                    for j in range(len(matrix1[0])):
                        result[i][j] = matrix1[i][j] * matrix2[i][j]
                return result

            def imprimir_matriz(matriz):
                for fila in matriz:
                    print(" ".join(map(str, fila)))

            # Solicitar dimensiones
            while True:
                try:
                    filas = int(input("Ingrese el número de filas: "))
                    columnas = int(input("Ingrese el número de columnas: "))
                    break
                except ValueError:
                    print("Por favor, ingrese números enteros para filas y columnas.")

            # Leer las dos matrices
            print("Matriz 1")
            matriz1 = leer_matriz(filas, columnas)

            print("Matriz 2")
            matriz2 = leer_matriz(filas, columnas)

            # Sumar matrices
            resultado = sumar_matrices(matriz1, matriz2)

            # Mostrar resultado
            print("Resultado de la suma:")
            imprimir_matriz(resultado)

            input("Presione ENTER para continuar...")

    #division
    elif eleccion==4:
        os.system("cls")
        def ingresar_matriz(filas, columnas, nombre=""):
            print(f"\nIngresa los elementos de la matriz {nombre}:")
            matriz = []
            for i in range(filas):
                fila = []
                for j in range(columnas):
                    while True:
                        try:
                            valor = float(input(f"Ingrese el valor en la posición ({i+1},{j+1}): "))
                            fila.append(valor)
                            break
                        except ValueError:
                            print("Error: debes introducir un número válido.")
                matriz.append(fila)
            return matriz

        def dividir_matrices(matriz1, matriz2):
            filas = len(matriz1)
            columnas = len(matriz1[0])
            resultado = []

            for i in range(filas):
                fila_resultado = []
                for j in range(columnas):
                    if matriz2[i][j] == 0:
                        print(f"Error: división por cero en la posición ({i+1},{j+1}).")
                        return None
                    fila_resultado.append(matriz1[i][j] / matriz2[i][j])
                resultado.append(fila_resultado)

            return resultado

        def mostrar_matriz(matriz):
            print("\nMatriz resultante:")
            for fila in matriz:
                print("  ".join(f"{valor:.2f}" for valor in fila))

        def main():
            print("Division de matrices\n")

            try:
                filas = int(input("Número de filas: "))
                columnas = int(input("Número de columnas: "))
            except ValueError:
                print("Error: debes introducir un número entero.")
                return

            matriz1 = ingresar_matriz(filas, columnas, "1")
            matriz2 = ingresar_matriz(filas, columnas, "2")

            resultado = dividir_matrices(matriz1, matriz2)

            if resultado:
                mostrar_matriz(resultado)

            input("\nPresiona ENTER para continuar...")

        if __name__ == "__main__":
            main()

    
    #salir
    elif eleccion==5:
        print("\n\t Termino de ejecutar el programa")
        start=False

    #otro resultado
    else:
        print("\n\t Opcion no valida. Vuelva a intentarlo. Oprima ENTER para continuar.")
        input("pulsa enter para continuar")
