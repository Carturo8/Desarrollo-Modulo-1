import unicodedata
import re

book_catalog = [
    {
        "title": "Cien años de soledad",
        "author": ["Gabriel García Márquez"],
        "genre": "Magical Realism",
        "year_of_publication": 1967,
        "quantity_available": 5,
        "replacement_price": 5000
    },
    {
        "title": "1984",
        "author": ["George Orwell"],
        "genre": "Dystopian",
        "year_of_publication": 1949,
        "quantity_available": 3,
        "replacement_price": 4200
    },
    {
        "title": "To Kill a Mockingbird",
        "author": ["Harper Lee"],
        "genre": "Classic",
        "year_of_publication": 1960,
        "quantity_available": 4,
        "replacement_price": 4600
    },
    {
        "title": "The Great Gatsby",
        "author": ["F. Scott Fitzgerald"],
        "genre": "Novel",
        "year_of_publication": 1925,
        "quantity_available": 2,
        "replacement_price": 3900
    },
    {
        "title": "Don Quijote de la Mancha",
        "author": ["Miguel de Cervantes", "Pepito Perez"],
        "genre": "Novel",
        "year_of_publication": 1805,
        "quantity_available": 3,
        "replacement_price": 7500
    },
    {
        "title": "Papi",
        "author": ["Miguel de Cervantes", "Pepito Perez"],
        "genre": "Novelaa",
        "year_of_publication": 1905,
        "quantity_available": 5,
        "replacement_price": 6500
    },
    {
        "title": "Niño",
        "author": ["Niño loco", "Pepito Perez"],
        "genre": "Novelaa",
        "year_of_publication": 1905,
        "quantity_available": 5,
        "replacement_price": 6500
    }
]

def normalize(text: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    ).lower()

def validate_book_title(book_title:str = "") -> str:
    condition = True
    while condition:
        book_title = " ".join(input("\nEnter the name: ").split())
        book_title = book_title.capitalize()
        if len(book_title) > 25:
            print("\033[91m❌ The title must not exceed 25 characters.\033[0m")
        elif not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", book_title):
            print("\033[93m⚠️ Only letters and spaces are allowed (including accents like á, é, ñ).\033[0m")
        else:
            condition = False
    return book_title

def validate_book_author(book_author:str = "") -> str:
    condition = True
    while condition:
        book_author = " ".join(input("\nEnter the author: ").split())
        book_author = book_author.title()
        if len(book_author) > 25:
            print("\033[91m❌ The author must not exceed 25 characters.\033[0m")
        elif not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", book_author):
            print("\033[93m⚠️ Only letters and spaces are allowed (including accents like á, é, ñ).\033[0m")
        else:
            condition = False
    return book_author

def validate_book_genre(book_genre:str = "") -> str:
    condition = True
    while condition:
        book_genre = " ".join(input("\nEnter the genre: ").split())
        book_genre = book_genre.capitalize()
        if len(book_genre) > 25:
            print("\033[91m❌ The genre must not exceed 25 characters.\033[0m")
        elif not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", book_genre):
            print("\033[93m⚠️ Only letters and spaces are allowed (including accents like á, é, ñ).\033[0m")
        else:
            condition = False
    return book_genre

def validate_book_publication_year(book_publication_year:int = 0) -> int:
    condition = True
    while condition:
        try:
            book_publication_year = int(input("\nEnter the year of publication: "))
            if 1800 <= book_publication_year <= 2024:
                condition = False
            else:
                print("\033[91m❌ Year of publication must be greater or equal than 1800 and lower than 2025.\033[0m")
        except ValueError:
            print("\033[93m⚠️ Invalid input. Please enter a number between 1800 and 2024 (e.g., 2020).\033[0m")
    return book_publication_year

def validate_book_quantity_available(book_quantity_available:int = 0) -> int:
    condition = True
    while condition:
        try:
            book_quantity_available = int(input("\nEnter the quantity available: "))
            if 0 < book_quantity_available <= 100_000_000:
                condition = False
            elif book_quantity_available > 100_000_000:
                print("\033[91m❌ Quantity available exceeds the maximum allowed (100,000,000).\033[0m")
            else:
                print("\033[91m❌ Quantity available must be greater than zero.\033[0m")
        except ValueError:
            print("\033[93m⚠️ Invalid input. Please enter a whole number (e.g., 15).\033[0m")
    return book_quantity_available

def validate_book_replacement_price(book_replacement_price:float = 0.0) -> float:
    condition = True
    while condition:
        try:
            book_replacement_price = round(float(input("\n💰 Enter the replacement price: ")), 2)
            if 0 < book_replacement_price <= 1_000_000_000:
                condition = False
            elif book_replacement_price > 1_000_000_000:
                print("\033[91m❌ Replacement price exceeds the maximum allowed ($1,000,000,000).\033[0m")
            else:
                print("\033[91m❌ Invalid replacement price. The value must be greater than zero.\033[0m")
        except ValueError:
            print("\033[93m⚠️ Invalid input. Please enter a valid number (e.g., 19.99).\033[0m")
    return book_replacement_price

def get_book_details(book_title:str = "") -> dict:
    # Validate the rest of the book details
    book_author = validate_book_author()
    book_genre = validate_book_genre()
    book_publication_year = validate_book_publication_year()
    book_quantity_available = validate_book_quantity_available()
    book_replacement_price = validate_book_replacement_price()

    # Return a dictionary with all the book data
    return {
        "title": book_title,
        "author": book_author,
        "genre": book_genre,
        "year_of_publication": book_publication_year,
        "quantity_available": book_quantity_available,
        "replacement_price": book_replacement_price
    }

# ----- REGISTER NEW BOOK -----

def register_new_book() -> None:
    condition = True
    while condition:
        # Validate the book title
        book_title = validate_book_title()

        # Check if the book already exists in the catalog
        if any(book_title.lower() == book["title"].lower() for book in book_catalog):
            print("📚 The book is already registered in the catalog.")
        else:
            # Create a new book dictionary
            new_book = get_book_details(book_title)

            # Add the new book to the catalog
            book_catalog.append(new_book)
            print("\n✅ The book has been successfully registered!\n")

        # Ask the user if they want to register another book
        continue_registering = input(
    "\033[93m➕ Do you want to register another book? (Press 'y' to add more / any other key to return to menu): \033[0m"
).strip().lower()
        if continue_registering != "y":
            condition = False

# ----- SEARCH BOOK -----

def search_book() -> None:
    condition = True
    while condition:
        # Ask user to choose search criteria
        print("\n🔍 Choose a search option:")
        print("1️⃣ Search by title")
        print("2️⃣ Search by author")
        option = input("Enter your choice (1 or 2): ").strip()

        if option == "1":
            # Validate and get the book title
            book_title = normalize(validate_book_title())
            matching_books = [
                book for book in book_catalog
                if book_title == normalize(book["title"])
            ]

            if matching_books:
                print("\n📖 Book(s) found:")
                for book in matching_books:
                    print("\n" + "-" * 40)
                    print(f"📘 Title: {book['title']}")
                    print(f"✍️ Author(s): {', '.join(book['author'])}")
                    print(f"🏷️ Genre: {book['genre']}")
                    print(f"📅 Year of Publication: {book['year_of_publication']}")
                    print(f"📦 Quantity Available: {book['quantity_available']}")
                    print(f"💰 Replacement Price: ${book['replacement_price']}")
                    print("-" * 40)
            else:
                register = input(
                    "\n❓ Book not found. Do you want to register it? (Press 'y' to register / any other key to cancel): ").strip().lower()
                if register == "y":
                    register_new_book()
                    condition = False

            again = input("\n🔁 Do you want to search again? (Press 'y' to continue / any other key to exit): ").strip().lower()
            if again != "y":
                condition = False

        elif option == "2":
            # Validate and get the author
            book_author = normalize(validate_book_author())
            matching_authors = [
                book for book in book_catalog
                if any(book_author == normalize(author) for author in book["author"])
            ]

            if matching_authors:
                print("\n📖 Book(s) found:")
                for book in matching_authors:
                    print("\n" + "-" * 40)
                    print(f"📘 Title: {book['title']}")
                    print(f"✍️ Author(s): {', '.join(book['author'])}")
                    print(f"🏷️ Genre: {book['genre']}")
                    print(f"📅 Year of Publication: {book['year_of_publication']}")
                    print(f"📦 Quantity Available: {book['quantity_available']}")
                    print(f"💰 Replacement Price: ${book['replacement_price']}")
                    print("-" * 40)
            else:
                print("\n📭 No books found by that author.")

            again = input("\n🔁 Do you want to search again? (Press 'y' to continue / any other key to exit): ").strip().lower()
            if again != "y":
                condition = False
        else:
            print("\n❌ Invalid option. Please choose 1 or 2.")

def update_book_info() -> None:
    if not book_catalog:
        print("\n📭 The book catalog is empty. No books to update.")
        return

    condition = True
    while condition:
        book_title = normalize(validate_book_title())
        matching_books = [
            book for book in book_catalog
            if normalize(book["title"]) == book_title
        ]

        if matching_books:
            book = matching_books[0]
            print(f"\n📘 Book found: {book['title']} by {', '.join(book['author'])}")
            print("\n⚙️ What would you like to update?")
            print("1️⃣ Quantity Available")
            print("2️⃣ Replacement Price")
            print("3️⃣ Both")
            print("0️⃣ Cancel")
            option = input("Enter your choice: ").strip()

            if option == "1":
                validate_book_quantity_available()

            elif option == "2":
                validate_book_replacement_price()

            elif option == "3":
                validate_book_quantity_available()
                validate_book_replacement_price()

            elif option == "0":
                print("🔙 Update cancelled.")
                break

            else:
                print("❌ Invalid option. Please choose 1, 2, 3, or 0.")
                continue

        else:
            print("\n❌ No book found with that title.")


            # Ask if the user wants to update again
            again = input("\n🔁 Do you want to update another field for this book? (y/n): ").strip().lower()
            if again != "y":
                condition = False

#register_new_book()
#search_book()
update_book_info()
