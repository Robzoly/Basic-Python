Salario_Presidente=int(input("Introduce el salario del presidente de la compañía: "))
print("Salarios presidente: " +str(Salario_Presidente))

Salario_Director=int(input("Introduce el salario del Director: "))
print("Salarios director: " +str(Salario_Director))

Salario_Jefe_de_area=int(input("Introduce el salario del Jefe de area: "))
print("Salarios Jefe de area: " +str(Salario_Jefe_de_area))

Salario_Administrador=int(input("Introduce el salario de los administradores: "))
print("Salarios Administrador: " +str(Salario_Administrador))

if Salario_Administrador<Salario_Jefe_de_area<Salario_Director<Salario_Presidente:
	print("Todo funciona correctamente")
else:
	print("Error de salarios, intente de nuevo")