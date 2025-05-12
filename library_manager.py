import datetime

# Global book catalog
book_catalog = []

# Register a new book
def register_new_book(book_list=book_catalog):
    try:
        title = input("Enter book title: ").strip()
        author = input("Enter author: ").strip()
        genre = input("Enter genre: ").strip()
        year = int(input("Enter year of publication: "))
        current_year = datetime.datetime.now().year
        if year < 1800 or year > current_year:
            print(f"Invalid year. Enter a value between 1800 and {current_year}.")
            return

        quantity = int(input("Enter quantity: "))
        if quantity < 0:
            print("Quantity must be a positive number.")
            return

        price = float(input("Enter replacement price: "))
        if price < 0:
            print("Price must be a positive number.")
            return

        book = {
            "title": title,
            "author": author,
            "genre": genre,
            "year": year,
            "quantity": quantity,
            "price": price
        }
        book_list.append(book)
        print("Book registered successfully.")
    except ValueError:
        print("Invalid input. Please enter the correct data types.")

# Preload example books
def preload_books(book_list):
    example_books = [
        {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "genre": "Fiction", "year": 1967, "quantity": 4, "price": 30.0},
        {"title": "1984", "author": "George Orwell", "genre": "Dystopia", "year": 1949, "quantity": 5, "price": 25.5},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "year": 1960, "quantity": 3, "price": 22.0},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy", "year": 1937, "quantity": 6, "price": 27.0},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction", "year": 1951, "quantity": 2, "price": 24.0}
    ]
    book_list.extend(example_books)

# Search for books by title or author (case-insensitive)
def search_book(book_list):
    query = input("Enter book title or author to search: ").strip().lower()
    found = False
    for book in book_list:
        if query in book["title"].lower() or query in book["author"].lower():
            print("Book found:")
            for key, value in book.items():
                print(f"{key.capitalize()}: {value}")
            found = True
    if not found:
        print("Book not found. Would you like to register it?")

# Update a book's quantity and/or price
def update_book(book_list):
    title = input("Enter the title of the book to update: ").strip().lower()
    for book in book_list:
        if book["title"].lower() == title:
            try:
                new_quantity = int(input("Enter new quantity: "))
                if new_quantity < 0:
                    print("Quantity must be positive.")
                    return
                new_price = float(input("Enter new replacement price: "))
                if new_price < 0:
                    print("Price must be positive.")
                    return
                book["quantity"] = new_quantity
                book["price"] = new_price
                print("Book updated successfully.")
            except ValueError:
                print("Invalid input.")
            return
    print("Book not found.")

# Delete a book with confirmation
def delete_book(book_list):
    title = input("Enter the title of the book to delete: ").strip().lower()
    for book in book_list:
        if book["title"].lower() == title:
            confirm = input(f"Are you sure you want to delete '{book['title']}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                book_list.remove(book)
                print("Book deleted successfully.")
            else:
                print("Deletion canceled.")
            return
    print("Book not found.")

# Generate inventory reports
def generate_reports(book_list):
    if not book_list:
        print("No books in inventory.")
        return

    total_value = sum(book["price"] * book["quantity"] for book in book_list)
    print(f"\nTotal replacement value of inventory: ${total_value:.2f}")

    genre_books = {}
    for book in book_list:
        genre = book["genre"]
        if genre not in genre_books:
            genre_books[genre] = []
        genre_books[genre].append(book)

    print("\nOldest and newest book per genre:")
    for genre, books in genre_books.items():
        oldest = min(books, key=lambda b: b["year"])
        newest = max(books, key=lambda b: b["year"])
        print(f"\nGenre: {genre}")
        print(f"  Oldest: {oldest['title']} ({oldest['year']})")
        print(f"  Newest: {newest['title']} ({newest['year']})")

# Display the main menu
def main_menu():
    preload_books(book_catalog)
    while True:
        print("\nLibrary Book Management System")
        print("1. Register a new book")
        print("2. Search for a book")
        print("3. Update book information")
        print("4. Delete a book")
        print("5. Generate inventory reports")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            register_new_book()
        elif choice == "2":
            search_book(book_catalog)
        elif choice == "3":
            update_book(book_catalog)
        elif choice == "4":
            delete_book(book_catalog)
        elif choice == "5":
            generate_reports(book_catalog)
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")

# Entry point
if __name__ == "__main__":
    main_menu()