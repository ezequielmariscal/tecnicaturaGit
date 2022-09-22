# COLECCIONES EN PYTHON
# ########### TUPLAS##########

# las listas son modificables.... las tuplas aunque son similares a las lista siguen el orden de las listas
# las tuplas se pueden modificar pero no se pueden eliminar es decir son INMUTABLES esa es la principal dif.

# ***** Leccion 1 =====> Definimos una tupla

cocina = ('cuchara', 'cuchillo', 'tenedor')  # usamos parentesis en las tuplas.
print(cocina)
print(len(cocina))  # tambien podemos usar len para desaparecer la tupla

# ***** Leccion 2 =====> Acceder a un elemento, para esto usamos corchetes no parentesis

print(cocina[0])

# ***** Leccion 3 =====> Tambien lo puedo mostrar de manera inversa

print(cocina[-1])

# ***** Leccion 4 =====> Acceder a un rango (quiero mostrar un grupo de elementos)

print(cocina[0:1])  # aca simplemente no muestra el cero
# como saber cuando es una tupla y cuando es un array?==?=?
# Ejemplo
verduras = ('papa',)  # Una tupla siempre tendra las coma despues(aunq sea una sola coma) de las comillas (IMPORTANTE)

# DE LO CONTRARIO SOLO SERIA UN TIPO STR CADENA..

# ***** Leccion 5 =====> Recorremos los elementos de una tupla
for cocinar in cocina:
    print(cocinar)  # al ejecutar nos muestra un salto de linea que lo hace print usa backlash /n pra usar salto de line
    print(cocinar, end=' ')  # hace que los saltos de linea finalicen

# se puede cambiar un tupla como una lista? NOOOOO!!!! salta error en el print
# cocina[0] = 'plato'
# print(cocina)

# como se puede modificar una tupla?? ESTO ES UNA MALA PRACTICA AL MENOS QUE SEA NECESARIO
# hacemos conversion de tupla a lista y modificamos y pasamos a tupla de vuelta
cocinaLista = list(cocina)  # de tupla a lista
cocinaLista[0] = 'plato'  # modificamos
cocina = tuple(cocinaLista)  # de lista a tupla
print('\n', cocina)

# ***** Leccion 6 =====> como elimino una tupla?

# del cocina
# print(cocina)

# Repaso de Tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 47], 4, 'Hola')  # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla)  # Accion booleana, su respuesta es de tipo booleana
# En tuplas se puede convertir de tupla a lista y de lista a tupla
