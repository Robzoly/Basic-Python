print("Verificación de edad")

edad_usuario=int(input("Introduzca su edad: "))

if edad_usuario<18:
	print("Es necesario ser mayor de edad para acceder a esta sección")
elif edad_usuario>100:
	print("Esta edad no es válidad. Intente de nuevo")
else:
	print("Acceso concedido")
print("El programa ha finalizado")