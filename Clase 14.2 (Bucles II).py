Contador=0
miEmail=input("Introduce tu correo electrónico: ")

for i in miEmail:
    
    if(i=="@" or i=="."):

        Contador=Contador+1

if Contador==2:
    print("Email es correcto")
else:
    print("Email es incorrecto")