#COLECCIONES EN PYTHON
############ DICCIONARIOS ##########

# Diccionarios en Python
# Los diccionarios son una estructura de datos de Python muy importante.
# Mientras que las listas te permiten crear colecciones de valores, los diccionarios permiten crear colecciones de pares clave/valor.
# Aquí hay un ejemplo de diccionario con un par clave/valor:

# 'Maradona' :10  Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key,value)

# ***** Leccion 1 =====> Realizamos un diccionario con key,value

diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientadas a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos',
}
print(diccionario)

# ***** Leccion 2 =====> Verificar la cantidad de elementos del diccionario

print(len(diccionario))

# ***** Leccion 3 =====> Acceder a un diccionario con la llave (key)

print(diccionario['IDE'])

# ***** Leccion 4 =====> Forma de agregar  elementos

print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# ***** Leccion 5 =====> Modificamos elementos

diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# ***** Leccion 6 =====> Como recorrer los elementos

for termino in diccionario: # recorremos mostrando solo las llaves
    print(termino)

# for termino, valor in diccionario:   --- esto da error porque no se puede recorrer el value, solo las key
#     print(termino, valor)

# Necesitamos una fx para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# ***** Leccion 7 =====> Otras manera a acceder a un diccionario

for termino in diccionario.keys(): #Estamos usando una funcion
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una funcion para acceder al valor
    print(valor)

# ***** Leccion 8 =====> Comprobar la existencia de algun elemento

print('IDE' in diccionario) #  devuelve un booleano

# ***** Leccion 9 =====> Agregar un elemento

diccionario['PK'] = 'Primary Key'
print(diccionario)

# ***** Leccion 10 =====> Eliminar un elemento

diccionario.pop('SABD')
print(diccionario)

# ***** Leccion 11 =====> Vaciar un diccionario

# diccionario.clear()
# print(diccionario)

# ***** Leccion 12 =====> Eliminar diccionario

# del diccionario el diccionario se borro