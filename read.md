# 📚 Library Book Management System

This Python program provides a command-line interface for managing a book catalog in a library. It allows librarians to register new books, search and update existing entries, delete old or lost books, and generate inventory reports.

## ✅ Features

- **Register Books**: Add new books with title, author, genre, year, quantity, and replacement price.
- **Search Books**: Search by title or author (case-insensitive). Prompts to register if not found.
- **Update Books**: Modify quantity and/or replacement price. Validates for positive values.
- **Delete Books**: Remove books with confirmation.
- **Reports**:
  - Total replacement value of the inventory.
  - Oldest and newest book by genre.

## 🧪 Data Validation

- `Year`: Must be between 1800 and current year.
- `Quantity`: Must be a non-negative integer.
- `Price`: Must be a non-negative float.

## 📦 Preloaded Example Books

The program includes 5 preloaded books at startup:

- *One Hundred Years of Solitude*
- *1984*
- *To Kill a Mockingbird*
- *The Hobbit*
- *The Catcher in the Rye*

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Download the file `library_manager.py`.
3. Run it in your terminal or command prompt:

```bash
python library_manager.py
Library Book Management System
1. Register a new book
2. Search for a book
3. Update book information
4. Delete a book
5. Generate inventory reports
6. Exit
Choose an option (1-6): 2
Enter book title or author to search: Orwell
Book found:
Title: 1984
Author: George Orwell
Genre: Dystopia
Year: 1949
Quantity: 5
Price: 25.5
```