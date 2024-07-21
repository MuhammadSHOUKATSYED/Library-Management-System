import Admin
import User


op = 'Y'
while op == 'Y' or op == 'y':
        print("Please select your option: ")
        print("1. Admin: ")
        print("2. User: ")

        option = input("Enter 1 or 2: ")
        if(int(option) == 1):
                print("Please select your option")
                print("1. Add a Book: ")
                print("2. Remove a Book: ")
                print("3. See Details of a Book: ")
                print("4. Update a Book: ")
                op = input("Enter your option here: ")
                if(int(op) ==1):
                    Admin.addBook()
                elif(int(op) ==2):
                    Admin.removeBook()
                elif(int(op) ==3):
                    Admin.showInfo()
                elif(int(op) ==4):
                    Admin.updateBook()

        elif(int(option) == 2):
            print("Please select your option")
            print("1. Borrow a Book: ")
            print("2. Return a Book: ")
            op = input("Enter your option here: ")
            if(int(op) == 1):
                    User.borrowBook()
            elif(int(op) == 2):
                    User.returnBook()
        else:
            print("Error: Wrong option")
        print("Do you want to go back to the main menu or not? (Y/N)")
        op = input("Enter here: ")
        if(op == 'N' or op == 'n'):
            exit()