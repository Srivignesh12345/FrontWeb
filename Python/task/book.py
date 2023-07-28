class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class BookManager:
    def __init__(self):
        self.books = []

    def create_book(self, title, author, genre):
        book = Book(title, author, genre)
        self.books.append(book)
        print("Book created successfully.")

    def read_book(self, title):
        for book in self.books:
            if book.title == title:
                print("Title:", book.title)
                print("Author:", book.author)
                print("Genre:", book.genre)
                return
        print("Book not found.")

    def update_book(self, title, new_title=None, new_author=None, new_genre=None):
        for book in self.books:
            if book.title == title:
                if new_title:
                    book.title = new_title
                if new_author:
                    book.author = new_author
                if new_genre:
                    book.genre = new_genre
                print("Book updated successfully.")
                return
        print("Book not found.")

    def delete_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Book deleted successfully.")
                return
        print("Book not found.")

    def list_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("List of books:")
            for book in self.books:
                print("Title:", book.title)
                print("Author:", book.author)
                print("Genre:", book.genre)

def main():
    book_manager = BookManager()

    while True:
        print("\n=== Book CRUD ===")
        print("1. Create book")
        print("2. Read book")
        print("3. Update book")
        print("4. Delete book")
        print("5. List books")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            genre = input("Enter the genre: ")
            book_manager.create_book(title, author, genre)
        elif choice == '2':
            title = input("Enter the title of the book to read: ")
            book_manager.read_book(title)
        elif choice == '3':
            title = input("Enter the title of the book to update: ")
            new_title = input("Enter the new title (leave blank to keep existing): ")
            new_author = input("Enter the new author (leave blank to keep existing): ")
            new_genre = input("Enter the new genre (leave blank to keep existing): ")
            book_manager.update_book(title, new_title, new_author, new_genre)
        elif choice == '4':
            title = input("Enter the title of the book to delete: ")
            book_manager.delete_book(title)
        elif choice == '5':
            book_manager.list_books()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()