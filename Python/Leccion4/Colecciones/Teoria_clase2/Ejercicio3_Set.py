#COLECCIONES EN PYTHON
################# SET #####################


# Los conjuntos(sets) son otra estructura de datos importante de Python.
# Podemos decir que funcionan como tuplas, pero no están ordenadas y son mutables.
# O podemos decir que funcionan como diccionarios, pero no tienen claves.
# También tienen una versión inmutable, llamada frozenset.
# Puedes crear un conjunto usando esta sintaxis:

# ***** Leccion 1 =====> Sintaxis
planetas = {'Marte', 'Jupiter', 'Venus'}
# print(planetas)
print(len(planetas)) # usamos la funcion len = length significa largo

# ***** Leccion 2 =====> Revisar si un elemento existe dentro de set
print('Marte' in planetas)
print('Jupiter' not in planetas)

# ***** Leccion 3 =====>  Agregar un elemento
planetas.add('Tierra') # add es una funcion
print(planetas)
# no se puede volver a agregar elementos duplicados o repetidos en un set.

# ***** Leccion 4 =====> Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Jupiter') # Esta funcion ante un mal ingreso o inexistencia del elem da error
print(planetas)
planetas.discard('tierra') # Esta funcion no nos presenta ningun error
print(planetas)

# ***** Leccion 5 =====> Limpiar set
planetas.clear()
print(planetas)

# ***** Leccion 6 =====> Eliminar set
del planetas  # al eliminar nos muestra un error

# Respaso de set o conjunto
# ***** Leccion 7 =====>para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1)  # Preguntamos si el numero 3 NO esta en el conjutno1

# ***** Leccion 8 =====> Como hace la igualdad de dos conjuntos
print(conjunto1 == conjunto2)  # Nos devuelve como respuesta un booleano

# ***** Leccion 9 =====> Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2  # la linea uno los dos conjuntod
print(conjunto3)

conjunto3 = conjunto1 & conjunto2  # Que elementos tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2  # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2  # Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))  # Aqui preguntamos si un conjuntos es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto2))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1))  # Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2))  # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# ***** Leccion 10 =====> Como saber si ambos conjuntos son disconecos esto si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))  # No hyas cosas en comun

# ***** Leccion 11 =====> Convertir un conjunto totalmente inmutable
conjunto1 = frozenset  # Esto hace que el conjunto sea totalmente inmutable
#  No se puede agregar, modificar ni eliminar elementos del conjunto
