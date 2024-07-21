from Book import Book

book = Book("name","publisher","author","publishDate", "available")

books = [book]

def addBook():
        print("Provide the information of the book to be added: ")
        name = input("Enter the name of the book: ")
        publisher = input("Enter the name of the book: ")
        author = input("Enter the name of the author: ")
        publishDate = input("Enter the publishing Date of the book: ")
        book = Book(name,publisher,author,publishDate, "available")
        books.append(book)

def removeBook():
    name = input("Enter the name of the Book to be removed: ")
    author = input("Enter the name of the author of this book: ")
    for book in books:
        if(book.name == name and book.author == author):
            books.remove(book)
            print("Book removed successfully")

def updateBook():
    name = input("Enter the name of the Book to be updated: ")
    author = input("Enter the name of the author of this book: ")
    for book in books:
        if(book.name == name and book.author == author):
            book.name = input("Enter updated name: ")
            book.publisher = input("Enter updated publisher: ")
            book.author = input("Enter updated author: ")
            book.publishDate = input("Enter updated published Date: ")
            book.status = input("Enter Status: ")
            print("Action successfully")


def showInfo():
    name = input("Enter the name of the Book to: ")
    author = input("Enter the name of the author of this book: ")
    for book in books:
        if(book.name == name and book.author == author):
            print("Name: " +book.name)
            print("Author: " +book.author)
            print("Publisher: " +book.publisher)
            print("Published Date: " +book.publishDate)
            print("Status: " +book.status)
