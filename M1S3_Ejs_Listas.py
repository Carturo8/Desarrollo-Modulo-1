# 1. Suma de elementos de una lista.
"Dada una lista de números, calcula la suma de todos sus elementos·"""

def sum_of_list(list_:list[float] = []):
    """
    Function to calculate the sum of elements in a list.
    """
    list_ = input("Ingresa la lista de números separados por comas: ").split(",")
    list_ = [float(number) for number in list_]
    print(f"La suma de los números de la lista {list_} es: {sum(list_)}")

# 2. Eliminar duplicados de una lista.
"""Crear una función que reciba una lista y devuelva una nueva lista sin elementos repetidos, manteniendo el orden original."""

def remove_duplicates(list_:list[str] = []):
    """
    Function to remove duplicates from a list and return a new list maintaining the original order.
    """
    new_list = []
    list_ = input("Ingresa los elementos de la lista separados por comas: ").split(",")
    for element in list_:
        if element not in new_list:
            new_list.append(element)
    print(f"La lista sin duplicados es: {new_list}")

# 3. Invertir una lista (sin métodos built-in).
"""Invierte el orden de una lista sin usar reverse(), reversed() o slicing ([::-1]). Usa un bucle."""

def invert_list(list_:list[str] = []):
    """
    Function to invert a list without using built-in methods.
    """
    invert_list = []
    list_ = input("Ingresa los elementos de la lista separados por comas: ").split(",")
    for element in range(1, len(list_) + 1, 1):
        invert_list.append(list_[-element])
    print(f"La lista invertida es: {invert_list}")

# 4. Contador de palabras.
"""Dada una lista de palabras, cuenta cuántas veces aparece cada una y devuelve un diccionario con los resultados."""

def word_counter(list_:list[str] = []):
    """
    Function to count the occurrences of each word in a list and return a dictionary with the results.
    """
    list_ = input("Ingresa las palabras separadas por comas: ").split(",")
    list_ = [number.strip() for number in list_]
    word_count = {}
    for word in list_:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(f"El conteo de palabras es: {word_count}")

# 5. Combinar dos listas ordenadas
"""Dadas dos listas ordenadas de menor a mayor, combínalas en una sola lista manteniendo el orden."""

def combine_sorted_lists(list1:list[int] = [], list2:list[int] = []):
    """
    Function to combine two sorted lists into one while maintaining the order.
    """
    list1 = input("Ingresa la primera lista de números separada por comas: ").split(",")
    list1 = [int(number) for number in list1]
    list2 = input("Ingresa la segunda lista de números separada por comas: ").split(",")
    list2 = [int(number) for number in list2]
    combined_list = list1 + list2
    print(f"La lista combinada es: {sorted(combined_list)}")

# 6. Mayor y menor de una tupla.
"""Dada una tupla de números, devuelve una nueva tupla con el valor máximo y el mínimo."""

#sum_of_list()
#remove_duplicates()
#invert_list()
#word_counter()
#combine_sorted_lists()