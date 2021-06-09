# Asignatura: Ciclo For Básico II
# Objetivos: Obten funciones de escritura cómodas solo usando bloques de construcción básicos de Python (es decir, usando sus propias habilidades en lugar de confiar en los elementos integrados)
#            Ponte cómodo usando bucles, funciones, listas y otros tipos de datos
#
#     Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
#         Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]
def mifuncion(lista):
    for i in range(0, len(lista), 1):
        if lista[i] > 0:
            lista[i] = "big"
    return lista
print(mifuncion([7,-2,4,-6,8]))

#     Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
#         Ejemplo: count_positives([- 1, 1, 1,1 ]) cambia la lista original a [-1, 1, 1, 3] y la devuelve
#         Ejemplo: count_positives([1, 6, -4, -2, -7, -2]) cambia la lista a [1, 6, -4, -2, -7, 2] y la devuelve
def mifuncion(lista):
    suma = 0
    for i in range(0, len(lista), 1):
        if lista[i] > 0:
            suma += 1
    lista[len(lista)-1] = suma        
    return lista
print(mifuncion([7,-2,4,-6,8]))

#     Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
#         Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#         Ejemplo: sum_total ([6,3, -2]) debería devolver 7
def mifuncion(lista):
    suma = 0
    for i in range(0, len(lista), 1):
        suma += lista[i]
    return suma
print(mifuncion([7,-2,4,-6,8]))

#     Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#         Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
def mifuncion(lista):
    suma = 0
    for i in range(0, len(lista), 1):
        suma += lista[i]
    return (suma / len(lista))
print(mifuncion([7,-2,4,-6,8]))

#     Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
#         Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
#         Ejemplo: longitud ([]) debería devolver 0
def mifuncion(lista):  
    suma = 0
    for i in range(0, len(lista), 1):
        suma += 1
    return suma
print(mifuncion([7,-2,4,-6,8]))

#     Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
#         Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#         Ejemplo: mínimo ([]) debería devolver False
def mifuncion(lista):  
    if len(lista) == 0:
        return False
    minimo = lista[0]
    for i in range(0, len(lista), 1):
        if lista[i] < minimo:
            minimo = lista[i] 
    return minimo
print(mifuncion([]))    
print(mifuncion([7,-2,4,-6,8]))

#     Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
#         Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
#         Ejemplo: máximo ([]) debería devolver False
def mifuncion(lista):  
    if len(lista) == 0:
        return False
    maximo = lista[0]
    for i in range(0, len(lista), 1):
        if lista[i] > maximo:
            maximo = lista[i] 
    return maximo
print(mifuncion([]))    
print(mifuncion([7,-2,4,-6,8]))

# Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}
def mifuncion(lista):  
    if len(lista) == 0:
        return False
    suma = 0
    long = 0
    mini = lista[0]
    maxi = lista[0]
    for i in range(0, len(lista), 1):
        suma += lista[i]
        long += 1
        if lista[i] > maxi:
            maxi = lista[i] 
        if lista[i] < mini:
            mini = lista[i]
    dic = {'Suma': suma, 'Promedio': suma / long, 'Minimo': mini, 'Maximo': maxi, 'Longitud': long}
    return dic
print(mifuncion([7,-2,4,-6,8]))

# Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
def reversar(lista):
    max_i = len(lista) - 1
    itera = int(len(lista)/2)                             # numero de iteraciones
    for i in range(0, itera):                             # i es el puntero inicial
        lista[i], lista[max_i] = lista[max_i], lista[i]        
        max_i -= 1                                        # Decrementa el puntero final
    return lista
miarr = [2, 5, 8, 9, 12, 19, 25, 27, 32, 60]
print(miarr)
print(reversar(miarr))