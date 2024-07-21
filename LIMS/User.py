import Admin

def borrowBook():
    print("Enter the following details to borrow a book: ")
    name = input("Enter the name of the Book to: ")
    author = input("Enter the name of the author of this book: ")
    for book in Admin.books:
        if(book.name == name and book.author == author):
            book.status = "borrowed"
            print("Book borrowed successfully")
        else:
            print("Not found")

def returnBook():
    print("Enter the following details to return a book: ")
    name = input("Enter the name of the Book: ")
    author = input("Enter the name of the author of this book: ")
    for book in Admin.books:
        if(book.name == name and book.author == author):
            book.status = "available"
            print("Book returned successfully")
        else:
            print("Not found")