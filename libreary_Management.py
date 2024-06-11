class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if title not in self.books:
            self.books[title] = author
            print(f"Book '{title}' by {author} added to the library.")
        else:
            print("Book already exists in the library.")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Book '{title}' removed from the library.")
        else:
            print("Book not found in the library.")

    def display_books(self):
        if self.books:
            print("Books available in the library:")
            for title, author in self.books.items():
                print(f"'{title}' by {author}")
        else:
            print("No books available in the library.")

    def search_book(self, title):
        if title in self.books:
            print(f"'{title}' by {self.books[title]} is available in the library.")
        else:
            print("Book not found in the library.")


def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Available Books")
        print("4. Search Book")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            library.add_book(title, author)
        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)
        elif choice == '3':
            library.display_books()
        elif choice == '4':
            title = input("Enter the title of the book to search: ")
            library.search_book(title)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
