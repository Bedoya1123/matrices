# -*- coding: utf-8 -*-
import random

class Matriz(object):
    def __init__(self, filas=None, columnas=None):

        if filas:
            self.filas =filas
        else:
            try:
                self.filas = int(raw_input(" Ingrese número de filas"))
            except ValueError:
                print "ATENCIÓN: Debe ingresar un número entero."
                exit()

        if columnas:
            self.columnas = columnas
        else:
            try:
                self.columnas = int(raw_input(" Ingrese número de columnas"))
            except ValueError:
                print "ATENCIÓN: Debe ingresar un número entero."
                exit()



    def Crear_m(self):
      self.matriz=[]
      for f in range(self.filas):
          self.matriz.append([0]*self.columnas)

    def Llenar_m(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = random.randint(-10, 10)

    def Llenar_matriz(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = int(raw_input("Ingrese %d,%d: " % (f, c)))

    def Print_m(self):
        print self.matriz

    def datos(self):
        return self.matriz

    def valida_m(self,colA,filB):
        if colA != filB:
            return True
        else:
            return False

    def multi_m(self,matrizA,matrizB,filaB):
        for f in range(self.filas):
            for c in range(self.columnas):
                for k in range(filaB):
                    self.matriz[f][c]+=matrizA[f][k]*matrizB[k][c]

    def multiplicanum(self,num):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = self.matriz[f][c] * num

    def valida_sumres(self,filA, colA, filB,colB):
        if (colA != colB) or (filA != filB):
            return True
        else:
            return False

    def sum_m(self,matrizA,matrizB):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = matrizA[f][c] + matrizB[f][c]

    def rest_m(self,matrizA,matrizB):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = matrizA[f][c] - matrizB[f][c]

    def transpuesta(self,mA):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = mA[c][f]

    def simetrica(self):
        band = True
        for f in range(self.filas):
            for c in range(self.columnas):
                if (self.matriz[f][c] != self.matriz[c][f]):
                    band = False
                    break
        if (band):
            print"Matriz Simetrica"
        else:
            print"Matriz no es Simetrica"

    def identidad(self):
        for f in range(self.filas):
            self.matriz[f][f] = 1

    def multiply(self,matriz1, matriz2,fila):
        res = []
        for f in range(fila):
            res.append([0] * fila)

        for i, row in enumerate(res):
            for j in range(0, len(row)):
                for k in range(0, len(row)):
                    res[i][j] += matriz1[i][k] * matriz2[k][j]
        return res

    def potencia(self, pow):
        powerhash = {}
        if pow in powerhash.keys():
           return powerhash[pow]
        if pow == 1:
            return self.matriz
        if pow == 2:
            powerhash[pow] = self.multiply(self.matriz, self.matriz,self.filas)
            return powerhash[pow]
        if pow % 2 == 0:
            powerhash[pow] = self.multiply(self.potencia(pow / 2), self.potencia(pow / 2),self.filas)
        else:
            powerhash[pow / 2 + 1] = self.multiply(self.potencia(pow / 2), self.matriz,self.filas)
            powerhash[pow] = self.multiply(self.potencia(pow / 2), powerhash[pow / 2 + 1],self.filas)
        return powerhash[pow]

    def trans(self,m):
        t = []
        for r in range(len(m)):
            tRow = []
            for c in range(len(m[r])):
                if c == r:
                    tRow.append(m[r][c])
                else:
                    tRow.append(m[c][r])
            t.append(tRow)
        return t

    def menor(self,m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def determinante(self,m):
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        deter = 0
        for c in range(len(m)):
            deter += ((-1) ** c) * m[0][c] * self.determinante(self.menor(m, 0, c))
        return deter

    def inversa(self,m):
        deter = float(self.determinante(m))
        if (deter != 0):
            if len(m) == 2:
                return [[m[1][1] / deter,-1 * m[0][1] / deter],
                        [-1 * m[1][0] / deter,m[0][0] / deter]]

            cofactors = []
            for r in range(len(m)):
                cofactorRow = []
                for c in range(len(m)):
                    minor = self.menor(m, r, c)
                    cofactorRow.append(((-1) ** (r + c)) * self.determinante(minor))
                cofactors.append(cofactorRow)
            cofactors = self.trans(cofactors)
            for r in range(len(cofactors)):
                for c in range(len(cofactors)):
                    cofactors[r][c] = round(float(cofactors[r][c] / deter),2)
            return cofactors
        else:
            print "nose puede calcular"