print("Programa de becas 2022")

distancia_escuela=int(input("Introduce la distancia a la escuela en KM: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el n° de hermanos en el centro educativo: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce el salario mensual de tu familia: "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("El trámite de beca se ha completado")

else:
	print("No hay derecho a beca")