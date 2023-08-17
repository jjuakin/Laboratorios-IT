#!/usr/bin/env python
# -*- coding: utf-8 -*-

matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

print = (matriz)

fila = int(input("fila: "))
columna = int(input("Columna: "))

if fila < len(matriz[fila]):
	if columna < len(matriz[fila][columna]):
		print (matriz[fila][columna])
	else: 
		print ("Error en las columnas")
else:
		print ("Error en las filas")

