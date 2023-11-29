szam1 = 5
print(type(szam1))
print(id(szam1))
szam2 = szam1
print(szam2)
print(type(szam2))
print(id(szam2))
szam1 = szam1+5
print(szam1)
print(type(szam1))
print(id(szam1))
print(szam2)
print(type(szam2))
print(id(szam2))

# Eredeti lista
lista1 = [1, 2, 3]

# Az eredeti lista id-je
print("lista1 id:", id(lista1))
lista3 = lista1
print("lista3 id:", id(lista3))
# Új referenciával másolás
lista2 = lista1.copy()

# Az új lista id-je
print("lista2 id:", id(lista2))

# Módosítás az új referenciára
lista3.append(4)

# Az eredeti lista id-je változatlan marad
print("lista1 id (módosítás után):", id(lista1))
print("lista3 id (módosítás után):", id(lista3))
print(lista1)