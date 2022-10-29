PlayList=["Juan", 5, True, 7.99]
print(PlayList[:])
print(PlayList[2])
print(PlayList[-3])
print(PlayList[0:3])
print(PlayList[:3])
print(PlayList[1:3])

PlayList.append("Marquitos")
print(PlayList[:])

PlayList.insert(3,"Pedro")
print(PlayList[:])

PlayList.extend(["María", "Yael", "Sebastián"])
print(PlayList[:])

print(PlayList.index(True))

print("Paco" in PlayList)

print(True in PlayList)

PlayList.remove("Yael")
print(PlayList[:])

PlayList.remove(7.99)
print(PlayList[:])

PlayList2=["Naomi", 10, False, "Franco", 7.77]

PlayList3=PlayList+PlayList2
print(PlayList3[:])

PlayList4=[1, True, 25, "OwO"]*4
print(PlayList4[:])

PlayList5=["505-Artic_Monkeys", "I_Wanna_Be_Yours-Artic_Monkeys", "Hijo_de_la_Luna-Mecano"]
print(PlayList5[:])
print(PlayList5[:2])

PlayList6=["Artic_Monkeys","Queen","Mecano","Zoe","BTS"]

PlayListFinal=PlayList5+PlayList6

print(PlayListFinal)

print(PlayList4[:])

print(PlayList4.index(1))

print("Indila" in PlayList6)

PlayList6.pop()

print(PlayList6[:])
print("Se eliminó BTS")