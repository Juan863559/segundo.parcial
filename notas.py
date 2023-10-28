# Definir la función double
def double(x:int)->int:
    return x * 2

# Asignar la función double a la variable my_double
my_double = double
print(type(my_double))

# Llamar a la función a través de la variable
result = my_double(5)

# Imprimir el resultado
print(result)
#------------------------------------
def double(x:int)->int:
    return x * 2

# Llamar a la función a través de la variable
doble = double(3)

def cuad(f):
    return f ** 2

cuadrado = cuad(doble)
print(cuadrado)
#-----------------------------------------------------------------

def cuad(n:int)->int:
    return n ** 2


def elevar_numeros(lista, cuad):
    lista_cuadrados = []
    for num in lista:
        lista_cuadrados.append(cuad(num))
    return lista_cuadrados


lista = [1, 2, 3, 4, 5]
print(elevar_numeros(lista, cuad))

#---------------------------------------------

def cuad(n:int)->int:
    return n ** 2


def elevar_numeros(lista):
    lista_cuadrados = []
    for num in lista:
        lista_cuadrados.append(cuad(num))
    return lista_cuadrados


lista = [1, 2, 3, 4, 5]
print(elevar_numeros(lista))

#-----------------------------------

def elevar_numeros(lista):
    lista_cuadrados = []
    for num in lista:
        lista_cuadrados.append((lambda x: x **2)(num))
    return lista_cuadrados


lista = [1, 2, 3, 4, 5]
print(elevar_numeros(lista))

#---------------------------------------

def potencia(x,y): #pow(x,y)
    for _ in range(y):
        x = x * y
    return x


def elevar_numeros(lista, y):
    lista_potencias = []
    for num in lista:
        lista_potencias.append(pow(num,y))
    return lista_potencias


lista = [1, 2, 3, 4, 5]
print(elevar_numeros(lista, 2))

#----------------------------------------
def factorial(n):
    print(f"factorial() llamado con n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n -1)
    print(f"-> factorial({n}) retorna {return_value}")
    return return_value


factorial(5)
#factorial() llamado con n = 5
#factorial() llamado con n = 4
#factorial() llamado con n = 3
#factorial() llamado con n = 2
#factorial() llamado con n = 1
#-> factorial(1) retorna 1
#-> factorial(2) retorna 2
#-> factorial(3) retorna 6
#-> factorial(4) retorna 24
#-> factorial(5) retorna 120

#--------------------------------------

# Ejemplo iterativo
from timeit import timeit

timeit("print(string)", setup="string='Hola Mundo'", number=100)

#-----------------------------------------

# Performance algoritmo factorial iterativo
from timeit import timeit

setup_string = """
print("Iterativo:")
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
"""

from timeit import timeit
timeit("factorial(4)", setup=setup_string, number=10000000)

#-------------------------------------------

# Performance algoritmo factorial iterativo
from timeit import timeit

setup_string = """
print("Recursive:")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
"""

from timeit import timeit
timeit("factorial(4)", setup=setup_string, number=10_000_000)

#---------------------------------------------

#Usando reduce
setup_string = """
from functools import reduce
print("reduce():")
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
"""

from timeit import timeit
timeit("factorial(4)", setup=setup_string, number=10000000)

#-------------------------------------------------------------

def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
            print(key, '->', val)


f(name_1 = "Hugo", name_2 = "Paco", name_3 = "Luis")

#{'name_1': 'Hugo', 'name_2': 'Paco', 'name_3': 'Luis'}
#<class 'dict'>
#name_1 -> Hugo
#name_2 -> Paco
#name_3 -> Luis

#----------------------------------------------------

names = {"name_1": "Hugo", "name_2": "Paco", "name_3" : "Luis"}
f(**names)

#{'name_1': 'Hugo', 'name_2': 'Paco', 'name_3': 'Luis'}
#<class 'dict'>
#name_1 -> Hugo
#name_2 -> Paco
#name_3 -> Luis

#-------------------------------------------------

def f(a, b, c):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')


d = {'a': 'Hugo', 'b': "Paco", 'c': 'Luis'}
f(**d)

#a = Hugo
#b = Paco
#c = Luis