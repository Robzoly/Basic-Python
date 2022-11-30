for i in range(5,90,3):
    print (f"Valor de la variable {i}")

valido=False
email=input("Introduce tu correo electrónico: ")

for a in range(len(email)):
    
    if email[a]=="@":
        valido=True

if valido:
    print("El email es correcto")
else:
    print("El email es incorrecto")