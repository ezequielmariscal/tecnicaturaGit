#  MARISCAL EZEQUIEL (NO_CODE)
#  Ejercicio 4 : Sumar numeros apres dentro de un rango
# Hacer un programa pa sumar numeros pares dentro de un rango, por ej:
# suma de numeros pares del 2 al 30
# suma = 240
a = int(input('Digite de donde va a comenzar la suma : '))
b = int(input('Digite hasta donde quiere llegar a sumar '))
suma = 0
for i in range(a, b+1):
    if i % 2 == 0:  # Esto si el numero es par
        suma += i
print(f"\n La suma de numeros pares dentro del rango es: {suma}")