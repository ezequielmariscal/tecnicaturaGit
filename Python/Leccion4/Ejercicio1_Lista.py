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

# ***** Leccion 7 =====> Preguntamos cuantos elementos tiene una Array
print(len(nombres)) #pasamos como parametro la lista

# ***** Leccion 8 =====> Agregamos un elemento al Array
nombres.append('Luffy')
print(nombres)

# ***** Leccion 9 =====> Agregar dos nuevos elemento en un indice especifico
nombres.insert(1, 'Zoro') #agrego un entero y un tipo string
print(nombres)
nombres.insert(3, 'Nami')
print(nombres)

# ***** Leccion 10 =====> Eliminamos un elemento
nombres.remove('Zoro')
print(nombres)

# ***** Leccion 11 =====>  Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# ***** Leccion 12 =====>  Eliminar un indice especifico
del nombres[2] # del significa delete (eliminar)
print(nombres)

# ***** Leccion 13 =====>  Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# ***** Leccion 14 =====> Eliminar la lista
del nombres
print(nombres) # Aqui nos muestra la lista eliminada



