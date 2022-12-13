from login import Librarian, User
from tools import LibrarianTools, UserTools

def main():
    while True:
        print("Welcome to the library! Please login to continue.")
        command = input("Who are you?: (user/librarian/exit): ")
        match command.lower():
            case ("librarian"):
                while True:
                    login_librarian = input("Enter your id number: ")
                    password_librarian = input("Enter your password: ")
                    librarian = Librarian(login_librarian, password_librarian)
                    librarian = librarian.login_librarian()
                    if librarian:
                        print("Login successful")
                        break
                    else:
                        print("Login unsuccessful. Try again")
                print(f"Welcome {login_librarian}! What would you like to do?")
                while True:
                    action = input("Create user (CU), book return (BR), add new book (AB), delete the book (DB), browse the catalog (BC), exit (E): ")
                    match action.upper():
                        case "CU":
                            while True:
                                username = input("Enter username: ")
                                password = input("Enter password: ")
                                user = User(username, password)
                                if user.create_user():
                                    print("User created successfully")
                                    break
                                else:
                                    print("User creation unsuccessful. Try again")
                        case "BR":
                            if LibrarianTools.book_return():
                                print("Book returned successfully")
                            else:
                                print("Book return unsuccessful. Try again")                       
                        case "AB": 
                            LibrarianTools.add_book()
                            print("Book added successfully")
                        case "DB":
                            while True:
                                if LibrarianTools.delete_book():
                                    print("Book deleted successfully")
                                    break
                                else:
                                    print("Book deletion unsuccessful. Try again")
                        case "BC":
                            while True:
                                if LibrarianTools.browse_catalog():
                                    break
                                else:
                                    print("Browse unsuccessful. Try again")
                        case "E":
                            break
                        case _:
                            print("Invalid input.")

            case ("user"):
                while True:
                    login_user = input("Enter your username: ")
                    password_user = input("Enter your password: ")
                    user = User(login_user, password_user)
                    user = user.login_user()
                    if user:
                        print("Login successful")
                        break
                    else:
                        print("Login unsuccessful. Try again")
                print(f"Welcome {login_user}! What would you like to do?")
                user = UserTools(login_user)
                while True:
                    action = input("Borrow book (BB), reservation of book (RB), prolong a book (PB), find a book (FB), exit (E): ")
                    match action.upper():
                        case "BB":
                            while True:
                                if user.borrow_book():
                                    print("Book borrowed successfully")
                                    break
                                else:
                                    print("Book borrowing unsuccessful. Try again")
                        case "RB":
                            if user.reservation_book():
                                print("Book reserved successfully")
                            else:
                                print("Book reservation unsuccessful. Try again")
                        case "PB":
                            if user.prolong_book():
                                print("Book prolonged successfully")
                            else:
                                print("Book prolongation unsuccessful. Try again")
                        case "FB":
                            if user.find_book():
                                print("Book found successfully")
                            else:
                                print("Book finding unsuccessful. Try again")
                        case "E":
                            break
                        case _:
                            print("Invalid input.")
            case "exit":
                print("See you soon!")
                break

if __name__ == "__main__":
    main()