print("Bienvenido al sistema de calificaciones UNITEC")

Nota=int(input("Introduzca su primer nota: "))
Nota_2=int(input("Introduzca su segunda nota: "))
Nota_3=int(input("Introzuca su tercer nota: "))

Promedio_Final=(Nota+Nota_2+Nota_3)/3

if(Promedio_Final<60):
    print("Usted ha reprobado el semestre")

else:
    print("Usted ha aprobado el semestre")