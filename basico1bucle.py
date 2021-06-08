# Asignatura: bucles For: Básico I
# Objetivos: Aprende a usar las instrucciones básicas para bucles en Python
#            Practica algunos algoritmos básicos en Python

# Crea un archivo de Python llamado for_loop_basic1.py que realice las siguientes tareas.
# Básico : imprime todos los enteros del 0 al 150.
for i in range(0, 150+1, 1):
    print(i)

# Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for i in range(1, 1000+1, 1):
    if i % 5 == 0:
        print(i)

# Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10,
# imprima "Coding Dojo".
for i in range(1, 100+1, 1):
    if i % 5 == 0:
        print(i, "Coding")
    if i % 10 == 0:
        print(i, "Coding Dojo")

# ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
suma = 0
for i in range(1, 5010+1, 2):
    suma += i
print("Suma :", suma)

# Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
for i in range(2018, 0, -4):
    print(i)

# Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, 
# imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle 
# debe imprimir 3, 6, 9 (en líneas sucesivas)
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum+1, 1):
    if i % mult == 0: 
        print(i)

# BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000?