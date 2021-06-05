# GRUPO 2: 
# Crea una funcion que dado una palabra diga si es palindroma o no.

def palindroma(palabra):
    print(f"Palabra Normal: {palabra}, Palabra Invertida: {palabra[::-1]}")
    if palabra == palabra[::-1]:
        print("Es palindroma")
    else:
        print("No es palindroma")

print("Ingrese una palabra :")
palabra=input()
palindroma(palabra)

palabra="CursodePython"
print(palabra[0:3])
print(palabra[2:5])

# OTRO: 
# - Crea una función que tome una lista y devuelva el primer y el último valor de la lista. 
#   Si la longitud de la lista es menor que 2, haga que devuelva False.

def recorrerlista(lista):
    if len(lista)<2:
        return False
    else:
        print(lista[0])
        print(lista[len(lista)-1])

print(recorrerlista([7]))
print(recorrerlista([7,2,4,6,8]))

# - Crea una función que tome una lista y devuelva un diccionario con su mínimo, máximo, promedio y suma.
def devuelvedic(lista):
    dic={"Minimo":min(lista),"Maximo":max(lista),"Promedio":sum(lista)/len(lista),"Suma":sum(lista)}
    return dic

lista=[1,21,3,44,-15,6]
print("Diccionario:", devuelvedic(lista))
