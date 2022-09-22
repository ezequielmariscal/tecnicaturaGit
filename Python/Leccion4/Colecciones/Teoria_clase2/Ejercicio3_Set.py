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
del planetas # al eliminar nos muestra un error
