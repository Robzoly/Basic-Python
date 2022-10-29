print("Bienvenido")

nota=int(input("Introduzca la nota obtenida: "))

if(nota>0 and nota<=59):
	print("Usted ha reprobado")
elif(nota<60 and nota<=69):
	print("Usted ha aprobado")
elif(nota<70 and nota<=79):
	print("Usted tiene notas comunes")
elif(nota<80 and nota<=89):
	print("Usted tiene notas buenas")
elif(nota<90 and nota<=99):
	print("Usted es un alumno sobresaliente")
else:
	print("Usted es un estudiante de honor")

print("Gracias por usar el programa de calificaciones")