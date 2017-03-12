# -*- coding: utf-8 -*-
import matriz

def main():
    sel = " "

    while sel != "s":
        lista = ['Calculadora de matrices', 'a. Determinante ', 'b. Traspuesta', 'c. Inversa',
                 'd. Multiplicar matriz por un número', 'e. Matriz elevada a una Potencia', 'f. Matriz Simetrica',
                 'g.Matriz Identida ', 'h. A * B', 'i. A - B ', 'j. A + B', 'S. Salir']
        for i in lista:
            print i
        sel = raw_input("Seleccione una opción: ")

        if sel == "a":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            if matrizA.filas == matrizA.columnas:
                matrizA.Llenar_matriz()
                matrizA.Print_m()
                print matrizA.determinante(matrizA.datam())
            else:
                print "Matriz no es cuadrada"
        elif sel == "b":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            matrizA.Llenar_m()
            matrizA.Print_m()
            matrizC = matriz.Matriz(matrizA.columnas, matrizA.filas)
            matrizC.Crear_m()
            matrizC.transpuesta(matrizA.datos())
            matrizC.Print_m()
        elif sel == "c":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            matrizA.Llenar_m()
            matrizA.Print_m()
            print matrizA.inversa(matrizA.datos())
        elif sel == "d":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            matrizA.Llenar_m()
            matrizA.Print_m()
            num = int(raw_input('Número a multiplicar: '))
            matrizA.multiplicanum(num)
            matrizA.Print_m()
        elif sel == "e":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            matrizA.Llenar_m()
            matrizA.Print_m()
            pot=int(raw_input("Potencia"))
            print matrizA.potencia(pot)
        elif sel == "f":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            matrizA.Llenar_matriz()
            if matrizA.filas == matrizA.columnas:
                matrizA.Print_m()
                matrizA.simetrica()
            else:
                print "Matriz no es Cuadrada"
        elif sel == "g":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()

            if matrizA.filas == matrizA.columnas:
                matrizA.identidad()
                matrizA.Print_m()
            else:
                print "Matriz no es Cuadrada"
        elif sel == "h":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            matrizA.Llenar_m()
            matrizA.Print_m()
            matrizB = matriz.Matriz()
            matrizB.Crear_m()
            matrizB.Llenar_m()
            matrizB.Print_m()
            valida=matrizB.valida_m(matrizA.columnas,matrizB.filas)
            if valida:
                print "Error las Columnas de la Matriz A debe ser igual a las filas de la Matriz B "
            else:
                matrizC = matriz.Matriz(matrizA.filas, matrizB.columnas)
                matrizC.Crear_m()
                matrizC.multi_m(matrizA.datos(),matrizB.datos(),matrizB.filas)
                matrizC.Print_m()
        elif sel == "i":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            matrizA.Llenar_m()
            matrizA.Print_m()

            matrizB = matriz.Matriz()
            matrizB.Crear_m()
            matrizB.Llenar_m()
            matrizB.Print_m()
            vali=matrizB.valida_sumres(matrizA.filas, matrizA.columnas, matrizB.filas, matrizB.columnas)
            if vali:
                print "las matrices deben tener el mismo tamaño"
            else:
                matrizC = matriz.Matriz(matrizA.filas, matrizB.columnas)
                matrizC.Crear_m()
                matrizC.sum_m(matrizA.datos(), matrizB.datos())
                matrizC.Print_m()
        elif sel == "j":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            matrizA.Llenar_m()
            matrizA.Print_m()
            matrizB = matriz.Matriz()
            matrizB.Crear_m()
            matrizB.Llenar_m()
            matrizB.Print_m()
            vali=matrizB.valida_sumres(matrizA.filas, matrizA.columnas, matrizB.filas, matrizB.columnas)
            if vali:
                print "las matrices deben tener el mismo tamaño"
            else:
                matrizC = matriz.Matriz(matrizA.filas, matrizB.columnas)
                matrizC.Crear_m()
                matrizC.rest_m(matrizA.datos(), matrizB.datos())
                matrizC.Print_m()
        elif sel == "s":
            exit()
        else:
            print("Digite una opción valida \n")


if __name__ == '__main__':
    main()