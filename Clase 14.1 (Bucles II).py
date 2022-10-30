mail=False

miEmail=input("Introduce tu dirección de Email: ")
for i in miEmail:
    
    if(i=="@"):
        mail=True
#"==" comparan y "=" asigna un valor.
if mail==True:
    print("El mail es correcto")
else:
    print("El mail es incorrecto")

password=False

miPassword=input("Introduzca su contraseña: ")
for ai in miPassword:

    if(ai=="Zetaelfail"):
        password=True
if password==True:
    print("Contraseña incorrecta")
else:
    print("Contraseña correcta")