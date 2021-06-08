# Asignatura: Funciones Básicas II
# Objetivos: Aprende a crear funciones básicas en Python
#            Ponte cómodo usando listas
#            Ponte cómodo haciendo que la función devuelva una expresión / valor
#
#  Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, 
#  desde el número (como el elemento 0) hasta 0 (como el último elemento). Ej: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]

def mifuncion(num):
    newlista = []
    for i in range(num, 0, -1):
        newlista.append(i)
    return newlista
print(mifuncion(5))
print(mifuncion(10))


#  Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
#         Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2
def mifuncion(lista):
    print(lista[0])
    return (lista[len(lista)-1])
print(mifuncion([7,2]))

#  First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
#         Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)
def mifuncion(lista):
    return (lista[0] + len(lista))
print(mifuncion([7,2,4,6,8]))

#  Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la 
#  lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista 
#  tiene menos de 2 elementos, haga que la función devuelva False
#         Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
#         Ejemplo: values_greater_than_second ([3]) debería devolver False
def mifuncion(lista):
    if len(lista)<2:
        return False
    else:
        newlista = []
        for i in range(0, (len(lista)-1), 2):
            if  lista[i]> lista[i+1]:
                newlista.append(lista[i])

        return newlista
print(mifuncion([7]))
print(mifuncion([7,2,4,6,8,1]))

#  Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y 
#  devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
#         Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
#         Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]
def mifuncion(itera, numero):
    newlista = []
    for i in range(0, itera, 1):
        newlista.append(numero)

    return newlista
print(mifuncion(4,7))
print(mifuncion(6,2))

