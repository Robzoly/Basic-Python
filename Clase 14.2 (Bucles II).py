Owo=0
miEmail=input("Introduce tu correo electrónico: ")

for i in miEmail:
    
    if(i=="@" or i=="."):

        Owo=Owo+1

if Owo==2:
    print("Email es correcto")
else:
    print("Email es incorrecto")