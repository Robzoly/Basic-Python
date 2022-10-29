print("Programa de calificaciones de alumnos")

nota_alumno=input("Inserte la calificacion del alumno:")

def Evaluacion(nota):
	Calificacion="Aprobado"
	if nota<6:
		Calificacion="Reprobado"
	return Calificacion

print(Evaluacion(int(nota_alumno)))

Print("PROGRAMA DE BECAS UNITEC")

promedio=input("Inserte el promedio del alumno")

def Beca(final):
	Promedio="Mantiene su Beca"
	if final<8:
		Promedio="Pierde su beca"
	return Promedio

print(Beca(int(Promedio)))
