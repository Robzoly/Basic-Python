Diccionario={"Alemania":"Berlín", "Japón":"Tokio","Francia":"Paris","Colombia":"Bogotá"}
print(Diccionario["Colombia"])
print(Diccionario)

Diccionario["Argentina"]="Madrid"
print(Diccionario)
Diccionario["Argentina"]="Buenos Aires"
print(Diccionario)
del Diccionario["Francia"]
print (Diccionario)

Diccionario2={"Jordan":23,"Messi":10,"Cristiano":7}
print(Diccionario2)

Tupla=["España","Mexico","Brasil","Usa"]
Diccionario3={Tupla[0]:"Madrid",Tupla[1]:"CDMX",Tupla[2]:"Río de Janeiro",Tupla[3]:"Washington"}
print(Diccionario3["Mexico"])

Diccionario4={"Jordan":23,"Nombre":"Michael","Equipo":"Chicago","Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(Diccionario4["Anillos"])
print(Diccionario4)

print(Diccionario4.keys())
print(Diccionario4.values())
print(len(Diccionario4))