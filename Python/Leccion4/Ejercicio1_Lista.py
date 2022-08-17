# hacer una lista de nombres de 4 personas, la lista arranca del indice 0

nombres = ["Ezequiel", "Alito", "Angel", "Isabella"]
print(nombres)

# ***** Leccion 1 =====> probar las posiciones de nombres en una lista
#
# print(nombres[0])
# print(nombres[1])
# print(nombres[3])
# print(nombres[-1])# podemos recorrer en numeros negativos para mostrar el penultimo elemento
# print(nombres[-2])

# ***** Leccion 2 =====> como recuperar el rango de una lista
print(nombres[0:2]) #recorre el indice 0 y 1 , pero no el indice 2

# ***** Leccion 3 =====> Ir del inicio de la lista al indice (pero sin incluirlo: sin incluir ,
# el nro de indice que pongamos va a ir uno antes
print(nombres[ :3]) #Indices a mostrar 0, 1, 2

# ***** Leccion 4 =====> recorrer desde el indice indicado hasta el final.
print(nombres[1: ]) # que ejecute desde el indice 1 "Alito" hasta el final.

# ***** Leccion 5 =====> Modificar un valor
nombres[2] = 'Langelitos'
nombres[0] = 'Zequi'
print(nombres)

# ***** Leccion 6 =====> Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')