def greet(name:str = ""):
    """
    Function to greet a person with their name.

    Parameters:
    name (str): The name of the person to greet. Default is an empty string.

    Returns:
    str: A greeting message.
    """
    name = input("¿Cuál es tu nombre? ").strip()
    print(f"¡Hola, {name}!")

def sum_numbers(num1:float = 0, num2:float = 0):
    """
    Function to sum two numbers.

    Parameters:
    num1 (float): The first number. Default is 0.
    num2 (float): The second number. Default is 0.
    """
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    sum_ = num1 + num2
    print(f"La suma de {num1} y {num2} es: {sum_}")

def circle_area(radius:float = 0):
    """
    Function to calculate the area of a circle.

    Parameters:
    radius (float): The radius of the circle. Default is 0.
    """
    radius = float(input("Ingresa el radio del círculo: "))
    pi = 3.14159
    area = round(pi * (radius ** 2), 2)
    print(f"El área del círculo con radio {radius} es: {area}")

def even_number(number:int = 0):
    """
    Function to check if a number is even.

    Parameters:
    number (int): The number to check. Default is 0.
    """
    number = int(input("Ingresa un número: "))
    if number % 2 == 0:
        print(f"{number} es par.")
    else:
        print(f"{number} es impar.")

def greater_than_three_numbers(num1:int = 0, num2:int = 0, num3:int = 0):
    """
    Function to find the greatest of three numbers.

    Parameters:
    num1 (int): The first number. Default is 0.
    num2 (int): The second number. Default is 0.
    num3 (int): The third number. Default is 0.
    """
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))

    if num1 > num2 and num1 > num3:
        print(f"El mayor de los números {num1, num2, num3} es {num1}.")
    elif num2 > num1 and num2 > num3:
        print(f"El mayor de los números {num1, num2, num3} es {num2}.")
    else:
        print(f"El mayor de los números {num1, num2, num3} es {num3}.")

def counting_vowels(text:str = ""):
    """
    Function to count the number of vowels in a string.
    """
    text = input("Ingresa un texto: ")
    vowels:str = "aeiouAEIOU"
    count:int = sum(1 for char in text if char in vowels)
    print(f"El número de vocales en el texto es: {count}")

def calculate_factorial(numer:int = 0):
    """
    Function to calculate the factorial of a number.

    Parameters:
    number (int): The number to calculate the factorial. Default is 0.
    """
    number = int(input("Ingresa un número: "))
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"El factorial de {number} es: {factorial}")

def palindrome(word:str = ""):
    """
    Function to check if a word is a palindrome.

    Parameters:
    word (str): The word to check. Default is an empty string.
    """
    count = -1
    palindrome:str = ""
    word = input("Ingresa una palabra: ").lower()
    for char in word:
        if char == word[count]:
            palindrome = palindrome + char
            count -= 1
        else:
            print(f"{word.title()} no es un palíndromo.")
            break
    print(f"{word.title()} es un palíndromo.") if palindrome.title() == word.title() else None

#greet()
#sum_numbers()
#circle_area()
#even_number()
#greater_than_three_numbers()
#counting_vowels()
#calculate_factorial()
#palindrome()