"""
-------------------------------------------------------
Ejercicios de funciones, listas, tuplas y diccionarios.
-------------------------------------------------------
"""

"""1. Suma de elementos de una lista.
Dada una lista de números, calcula la suma de todos sus elementos·"""

def sum_of_list(list_:list[float] = []):
    """
    Function to calculate the sum of elements in a list.
    """
    list_ = input("Ingresa la lista de números separados por comas: ").split(",")
    list_ = [float(number) for number in list_]
    print(f"La suma de los números de la lista {list_} es: {sum(list_)}.")


"""2. Eliminar duplicados de una lista.
Crear una función que reciba una lista y devuelva una nueva lista sin elementos repetidos, manteniendo el orden original."""

def remove_duplicates(list_:list[str] = []):
    """
    Function to remove duplicates from a list and return a new list maintaining the original order.
    """
    new_list = []
    list_ = input("Ingresa los elementos de la lista separados por comas: ").split(",")
    for element in list_:
        if element not in new_list:
            new_list.append(element)
    print(f"La lista sin duplicados es: {new_list}.")

"""3. Invertir una lista (sin métodos built-in).
Invierte el orden de una lista sin usar reverse(), reversed() o slicing ([::-1]). Usa un bucle."""

def invert_list(list_:list[str] = []):
    """
    Function to invert a list without using built-in methods.
    """
    invert_list = []
    list_ = input("Ingresa los elementos de la lista separados por comas: ").split(",")
    for element in range(1, len(list_) + 1, 1):
        invert_list.append(list_[-element])
    print(f"La lista invertida es: {invert_list}.")

"""4. Contador de palabras.
Dada una lista de palabras, cuenta cuántas veces aparece cada una y devuelve un diccionario con los resultados."""

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
    print(f"El conteo de palabras es: {word_count}.")

"""5. Combinar dos listas ordenadas
Dadas dos listas ordenadas de menor a mayor, combínalas en una sola lista manteniendo el orden."""

def combine_sorted_lists(list1:list[int] = [], list2:list[int] = []):
    """
    Function to combine two sorted lists into one while maintaining the order.
    """
    list1 = input("Ingresa la primera lista de números separados por comas: ").split(",")
    list1 = [int(number) for number in list1]
    list2 = input("Ingresa la segunda lista de números separados por comas: ").split(",")
    list2 = [int(number) for number in list2]
    combined_list = list1 + list2
    print(f"La lista combinada es: {sorted(combined_list)}.")

"""6. Mayor y menor de una tupla.
Dada una tupla de números, devuelve una nueva tupla con el valor máximo y el mínimo."""

def max_and_min_tuple(tuple_:tuple[float] = ()):
    """
    Function to return a new tuple with the maximum and minimum values of a tuple.
    """
    tuple_ = tuple(input("Ingresa la tupla de números separados por comas: ").split(","))
    tuple_ = [float(number) for number in tuple_]
    new_tuple = (max(tuple_), min(tuple_))
    print(f"El valor máximo y mínimo de la tupla es {new_tuple} respectivamente.")

"""7. Desempaquetado de tuplas
Dada la tupla (3, 5, 7, 9), asigna cada valor a las variables a, b, c, d e imprímelas."""

def unpack_tuple(tuple_:tuple[int] = ()):
    """
    Function to unpack a tuple and assign each value to variables a, b, c, d.
    """
    tuple_ = (3, 5, 7, 9)
    a = tuple_[0]
    b = tuple_[1]
    c = tuple_[2]
    d = tuple_[3]
    print(f"a = {a}, b = {b}, c = {c}, d = {d}")

"""8. Convertir tupla a lista y viceversa
convierte una tupla en lista, añade el número 4, y luego conviértela de nuevo en tupla."""

def convert_tuple_to_list(tuple_:tuple[int] = ()):
    """
    Function to convert a tuple to a list, add the number 4, and then convert it back to a tuple.
    """
    tuple_ = input("Ingresa los elementos de la tupla separados por comas: ").split(",")
    tuple_ = [int(number) for number in tuple_]
    tuple_ = list(tuple_)
    tuple_.append(4)
    tuple_ = tuple(tuple_)
    print(f"La tupla con el nuevo elemento es: {tuple_}.")

"""9. Diccionario desde lista de tuplas
Convierte una lista de tuplas (clave, valor) en un diccionario."""

def convert_list_of_tuple_to_dict(tuple_:tuple[int] = ()):
    """
    Function to convert a list of tuples (key, value) to a dictionary.
    """
    list_of_tuples = []
    dictionary = {}
    tuples = input("Ingresa los elementos separados por comas: ").split(",")
    for element in range(1, len(tuples) + 1, 2):
        list_of_tuples.append((tuples[element - 1], tuples[element]))
    for key, value in list_of_tuples:
        dictionary[key] = int(value)
    print(f"El diccionario creado a partir de la lista de tuplas es: {dictionary}.")

"""10. Ordenar lista de tuplas por elemento.
Ordena una lista de tuplas de forma ascendente según el segundo elemento de cada tupla."""

def sort_list_of_tuples_by_second_element(list_of_tuples:list[tuple[int]] = []):
    """
    Function to sort a list of tuples by the second element of each tuple in ascending order.
    """
    list_of_tuples = []
    tuples = input("Ingresa los elementos separados por comas: ").split(",")
    tuples = [int(number) for number in tuples]
    for element in range(1, len(tuples) + 1, 2):
        list_of_tuples.append((tuples[element - 1], tuples[element]))
    list_of_tuples.sort(key = lambda x: x[1])
    print(f"La lista de tuplas ordenada por segundo elemento es: {list_of_tuples}.")

def menu_1():
    """
    Function to display the first menu.
    """
    print("""\nMenú de funciones: 
    1. Suma de elementos de una lista.
    2. Eliminar duplicados de una lista.
    3. Invertir una lista.
    4. Contador de palabras.
    5. Combinar dos listas ordenadas.
    6. Mayor y menor de una tupla.
    7. Desempaquetado de tuplas.
    8. Convertir tupla a lista y viceversa.
    9. Diccionario desde lista de tuplas.
   10. Ordenar lista de tuplas por elemento.
   --> Ingrese otro valor para salir.
    """)

def menu_2():
    """
    Function to display the second menu and return a boolean value indicating whether to continue.
    """
    print("""\nMenú de opciones:
    1. Volver al menú principal.
   --> Ingrese otro valor para salir.""")
    option = input("\nIngresa la opción deseada: ")
    condition = True
    if option == "1":
        menu_1()
    else:
        condition = False
        print("Gracias por usar el programa.")
    return condition

def main():
    """
    Function to run the program.
    """
    condition = True
    menu_1()
    while condition:
        option = input("Ingrese el número de la función que desea utilizar: ")
        if option == "1":
            print("\n-- Suma de elementos de una lista --")
            sum_of_list()
            condition = menu_2()
        elif option == "2":
            print("\n-- Eliminar duplicados de una lista --")
            remove_duplicates()
            condition = menu_2()
        elif option == "3":
            print("\n-- Invertir una lista --")
            invert_list()
            condition = menu_2()
        elif option == "4":
            print("\n-- Contador de palabras --")
            word_counter()
            condition = menu_2()
        elif option == "5":
            print("\n-- Combinar dos listas ordenadas --")
            combine_sorted_lists()
            condition = menu_2()
        elif option == "6":
            print("\n-- Mayor y menor de una tupla --")
            max_and_min_tuple()
            condition = menu_2()
        elif option == "7":
            print("\n-- Desempaquetado de tuplas --")
            unpack_tuple()
            condition = menu_2()
        elif option == "8":
            print("\n-- Convertir tupla a lista y viceversa --")
            convert_tuple_to_list()
            condition = menu_2()
        elif option == "9":
            print("\n-- Diccionario desde lista de tuplas --")
            convert_list_of_tuple_to_dict()
            condition = menu_2()
        elif option == "10":
            print("\n-- Ordenar lista de tuplas por elemento --")
            sort_list_of_tuples_by_second_element()
            condition = menu_2()
        else:
            condition = False
            print("Gracias por usar el programa.")

if __name__ == "__main__":
    main()