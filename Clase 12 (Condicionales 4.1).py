print("Asignaturas optativas Ing. en Sistemas Computacionales")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribir la asignatura a elegir: ")

Asignatura=opcion.lower()

if Asignatura in ("informática grafica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida: " + Asignatura)

else:
	print("La asignatura escogida es obligatoria")