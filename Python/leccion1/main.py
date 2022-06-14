'''
# distintasVariablesEjemplos
miVariable = 3
print(miVariable)
miVariable = "hola mundo"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))  # id sirve para saber la direccion de memoria ram
# Las liteales se escriben x624 (ya q son valores hexadecimales)

# Tipos int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))


# Manejo de cadenas (String)
miGrupoFavorito = "My chemical Romance"
caracteristicas = "The best rock band ever"
print("Mi grupo favorito es : "+miGrupoFavorito+" "+caracteristicas)
# otra manera
print("Mi grupo favorito es : ", miGrupoFavorito, caracteristicas)

# que pasa si sumo 2 cadenas o string?

numero1 = "7"
numero2 = "8"
print(numero1 + numero2)  # da 78 se unen porque es una cadena
# como convierto esta concatenacion a numeros para poder sumarlos ?
print(int(numero1) + int(numero2))

# Tipos Boleanos (bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# funcion imput
# resultado = input("Digite un numero: ")  # regresa un dato tipo string
# print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)

# Ejercicio 1: Califica tu día
# ¿Cómo estuvo tu día (1 al 10)?
# Mi día estuvo de: 10
print("como estuvo tu dia?")
calificacionDelDia = "10"
print("Mi día estuvo de: "+calificacionDelDia)

# Ejercicio 2:
# Se solicita incluir la siguiente información acerca de un libro:
# titulo
# autor
# Debes imprimir la información en el siguiente formato:

# Proporciona el título:

# Proporciona el autor:

# <titulo> fue escrito por <autor>

titulo = input(" Proporciona el titulo= ")
autor = input(" Proporciona el nombre del autor= ")
print(titulo + "fue escrito por: " + autor)

'''
"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("Resultado de la suma: ", suma)
# se denomina interpolacion la de {} de debe poner letra f al principio
print(f'El resultado de las suma es: {suma} ')

resta = operandoA - operandoB
print(f'El resultado de la res es: {resta}')

multiplicacion = operandoA * operandoB
print(f'El reustaldo de la multiplicacion es: {multiplicacion}')

division = operandoA / operandoB
print(f'el resultado de la division es: {division}')
division = operandoA // operandoB
print(f'El resutaldo de la division (int) es: {division}')
modulo = operandoA % operandoB
print(f'El resultado de la division o residuo(modulo) es: {modulo}')
exponente = operandoA ++ operandoB
print(f'El resultado del exponente es: {exponente}')
"""

# # Ejercicio rectángulo
#
# alto = int(input("Proporciona el alto del rectángulo: "))
# ancho = int(input("Proporciona el ancho del rectángulo: "))
# area = alto * ancho
# perimetro = (alto + ancho)*2
# print(f"El perimetro de el rectángulo es {perimetro} y el area es {area}")
#
# # Operadores de reasignación
#
# miVariable3 = 10
# print(miVariable3)
#
# miVariable3 = miVariable3 + 1
# print(miVariable3)
#
# miVariable3 += 1
# print(miVariable3)
#
# # miVariable3 = miVariable -2
# miVariable3 -= 2
# print(miVariable3)
#
# # miVariable3 = miVariable3 * 3
# miVariable3 *= 3
# print(miVariable3)
#
# # miVariable3 = miVariable / 2
# miVariable3 /= 2
# print(miVariable3)
# # Algunos operadores aritméticos también nos permiten
# # realizar operaciones sobre cadenas de texto:
# # + concatenación  ej: 'ho' + 'la' = 'hola'
# # * repetición  ej: 'Hello world' * 4 = 'Hello world, Hello world,
# #  Hello world, Hello world'
#
# # Operadores de comparación
#
# d = 4
# b = 2
# print(f'd = {d}  y  b = {b}')
# # ==  Son iguales?
# resultado = d == b
# print(f'd y b son iguales?:        {resultado}')
#
# # !=  Son distintos?
# resultado = d != b
# print(f'd y b son distintos?:      {resultado}')
#
# # >   Es mayor que?
# resultado = d > b
# print(f'd es mayor que b?:         {resultado}')
#
# # <   Es menor que?
# resultado = d < b
# print(f'd es menor que b?:         {resultado}')
#
# # >=  Es mayor o igual que?
# resultado = d >= b
# print(f'd es mayor o igual que b?: {resultado}')
#
# # <=  Es menor o igual que?
# resultado = d <= b
# print(f'd es menor o igual que b?: {resultado}')
#
# # Ejercicio1 par o impar
#
# num = int(input("ingrese un numero: "))
# if (num % 2) == 0:
#     print("el numero es par")
# else:
#     print("el numero es impar")
#
# comprobador = (num % 2) == 0
#
# if comprobador:
#     print("el numero es par")
# else:
#     print("el numero es impar")
#
#
# # Ejercicio2: Determinar si es mayor de edad
# edadAdulto = 18
# edad = int(input("Introduzca la edad: "))
# if edad >= edadAdulto:
#     print(f'Tu edad es {edad} años, sos mayor de edad')
# else:
#     print(f'Tu edad es {edad} años, sos menor de edad')
#
#
# # Operadores lógicos
#
# a = True
# b = True
# # operador and
# resultado = a and b
# print(resultado)  # en este caso será True
#
# # operador or
# a = False
# b = True
# resultado = a or b
# print(resultado)  # en este caso será True
#
# # operador not
# resultado = not a
# print(resultado)  # en este caso será True
#
#
# # Ejercicio: Valor dentro de un rango
# num = int(input("Por favor ingrese un numero entero: "))
# if (num <= 5) and (num >= 0):
#     print("El valor se encuentra dentro del rango (0,5)")
# else:
#     print("El valor se encuentra fuera del rango (0,5)")
#
#
# # Ejercicio: operador or
# vacaciones = False
# diaDescanso = False
# if vacaciones or diaDescanso:
#     print("El padre puede ir a ver a su hijo")
# else:
#     print("El padre no puede ver a su hijo")
#
#
# # Ejercicio: Rango entre las edades 20 y 30 años
# edad = int(input("Por favor ingrese su edad"))
# veinte = (edad >= 20) and (edad < 30)
# print(veinte)
# treinta = (edad >= 30) and (edad < 40)
# print(treinta)
#
# if veinte:
#     print("Estas dentro del rango de los 20 años")
# elif treinta:
#     print("Estas dentro del rango de los 30 años")
# else:
#     print("No estas dentro del rango de los 20 o de los 30 años")
#
#
# # Ejercicio: el mayor de dos números
# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))
# if num1 < num2:
#     print("El segundo numero es mayor")
# elif num2 < num1:
#     print("El primer número es mayor")
# else:
#     print("Los números son iguales")


# Ejercicio: tienda de libros
print("Ingrese los siguientes datos de libro")
nombreLibro = input("Digite el nombre del libro: ")
idLibro = input("Digite el ID del libro: ")
precioLibro = input("Digite el precio del libro: ")
envioGratuito = bool(input("Indicar con True / False si tiene envio gratuito: "))
print("Nombre:"+nombreLibro)
print("ID:"+idLibro)
print("Precio:"+precioLibro)
if envioGratuito:
    print("El envio es gratuito")
else:
    print("El envio no es gratuito")
