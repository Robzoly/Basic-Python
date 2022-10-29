print("Evaluación de alumnos")

nota_alumno=int(input("Inserte la nota del alumno: "))

if nota_alumno<5:
	print("Reprobado")

elif nota_alumno<6:
	print("Aprobado")

elif nota_alumno<7:
	print("Desempeño deficiente")

elif nota_alumno<8:
	print("Desempeño regular")

elif nota_alumno<9:
	print("Desempeño alto")

else:
	print("Sobresaliente")