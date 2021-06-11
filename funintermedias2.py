# Asignatura: Funciones Intermedias II
# Objetivos : Practica escribir funciones y recorrer los diccionarios
#             Comprender mejor cómo recorrer una lista de diccionarios o un diccionario de listas
# Nota: Evita usar palabras clave de clase como int, str, list y dict como nombres de variables / parámetros.

#  1. Actualiza los valores en diccionarios y listas
#     x = [ [5,2,3], [10,8,9] ] 
#     students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'}
#     ]
#     sports_directory = {
#         'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#         'soccer' : ['Messi', 'Ronaldo', 'Rooney']
#     }
#     z = [ {'x': 10, 'y': 20} ]
#  Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
def mifuncion(lista):  
    for i in range(0, len(lista), 1):
        for j in range(0, len(lista[i])):
            if lista[i][j] == 10:
                lista[i][j] = 15
    return lista
x = [ [5,2,3], [10,8,9] ] 
print("Resultado:", mifuncion(x))

# lista = [1, 2.5, 'DevCode', [5,6] ,4]
# print (lista[0]) # 1
# print (lista[1]) # 2.5
# print (lista[2]) # DevCode
# print (lista[3]) # [5,6]
# print (lista[3][0]) # 5
# print (lista[3][1]) # 6
# print (lista[1:3]) # [2.5, 'DevCode']
# print (lista[1:6]) # [2.5, 'DevCode', [5, 6], 4]
# print (lista[1:6:2]) # [2.5, [5, 6]]

# Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
def mifuncion(lista):  
    for persona in lista:
        if persona['last_name'] == 'Jordan':
            persona['last_name'] = 'Bryant'

    return lista

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print("Resultado:", mifuncion(students))


#  En el directorio sports_directory, cambia 'Messi' a 'Andres'
def mifuncion(lista):  
    for deporte in lista:
        print(lista[deporte])
        for jugador in lista[deporte]:
            print (jugador)
            if jugador == 'Messi':
                print("Es Messi")
                jugador = 'Andres'
        
    return lista

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print ("Resultado:", mifuncion(sports_directory))

#  Cambia el valor 20 en z a 30
def mifuncion(lista):  
    for elem in lista:
        print(elem)
        for valor in elem:
            print(elem[valor])
            if elem[valor] == 20:
               elem[valor] = 30     
      
    return lista

z = [ {'x': 10, 'y': 20} ]
print("Resultado:", mifuncion(z))


#  2. Itera a través de una lista de diccionarios
#     Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:
#     students = [
#              {'first_name':  'Michael', 'last_name' : 'Jordan'},
#              {'first_name' : 'John', 'last_name' : 'Rosales'},
#              {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#              {'first_name' : 'KB', 'last_name' : 'Tonel'}
#         ]
#     iterateDictionary(students) 
#     # La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
#     # Bonus: Hacer que aparezcan exactamente así!
#     first_name - Michael, last_name - Jordan
#     first_name - John, last_name - Rosales
#     first_name - Mark, last_name - Guillen
#     first_name - KB, last_name - Tonel

def iterateDictionary(some_list): 
    for estudiante in some_list:
        #  print(estudiante)
        print (estudiante.keys())
        print (estudiante.values())
        print(f"first_name -", estudiante['first_name'] + "," , "last_name -", estudiante['last_name'] )
    
students = [
             {'first_name':  'Michael', 'last_name' : 'Jordan'},
             {'first_name' : 'John', 'last_name' : 'Rosales'},
             {'first_name' : 'Mark', 'last_name' : 'Guillen'},
             {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ]
iterateDictionary(students)


# 3. Obtén valores de una lista de diccionarios
#    Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima 
#   el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:
#     Michael
#     John
#     Mark
#     KB
def iterateDictionary(some_list): 
    for estudiante in some_list:
        # print (estudiante['first_name'])
        print (estudiante['last_name'])        
    
students = [
             {'first_name':  'Michael', 'last_name' : 'Jordan'},
             {'first_name' : 'John', 'last_name' : 'Rosales'},
             {'first_name' : 'Mark', 'last_name' : 'Guillen'},
             {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ]
iterateDictionary(students)

#     e iterateDictionary2('last_name', students) debería generar:
#     Jordan
#     Rosales
#     Guillen
#     Tonel

# 4. Itera a través de un diccionario con valores de listas
#  Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, imprima el nombre de cada clave
#  junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

def printInfo(dojo):
    for i in dojo:
        lista = dojo[i]
        print (f"{len(lista)} {i.upper()}")
        for x in dojo[i]:
            print(x)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
#     # output:
#     7 LOCATIONS
#     San Jose
#     Seattle
#     Dallas
#     Chicago
#     Tulsa
#     DC
#     Burbank
#     8 INSTRUCTORS
#     Michael
#     Amy
#     Eduardo
#     Josh
#     Graham
#     Patrick
#     Minh
#     Devon