#Calcular el área de las fíguras geométricas con los valores que ingrese el usuario en la terminal

print("Bienvenido a la cálculadora de áreas de fíguras geométricas")

print("Área del cuadrado")
Num1=int(input("Introduzca el valor de uno de sus lados: "))
Area_cuadrado=Num1*Num1
print("El área del cuadrado es igual a: ", Area_cuadrado)

print("Área del rectángulo")
Base=int(input("Introduzca el valor de su base: "))
Altura=int(input("Introduzca el valor de su altura: "))
Area_rectángulo=Base*Altura
print("El área del rectangulo es igual a: ", Area_rectángulo)

print("Área del tríangulo")
Base=int(input("Introduzca el valor de su base: "))
Altura=int(input("Introduzca el valor de su altura: "))
Area_triangulo=Base*Altura/2
print("El área del triángulo es igual a: ", Area_triangulo)

print("Área del círculo")
Radio=int(input("Introduzca el valor del radio: "))
Pi=3.141592
Area_Circulo=Radio*Radio*Pi
print("El área del círculo es igual a: ", Area_Circulo)

print("Área de polígnos de más de 4 lados")
Lados=int(input("Introduzca la cantidad de lados de la figura: "))
Base=int(input("Introduzca el valor de la base: "))
Apotema=int(input("Introduzca el valor de su apotema: "))
Perimetro=Lados*Base
Area=Perimetro*Apotema/2
print("El área del polígono es igual a: ", Area)
print("Ha finalizado el programa")