import json 
from datetime import date, timedelta, datetime

class LibrarianTools:
    def book_return():
        """This method returns a book in library"""
        id_book = input("Enter id book: ")
        with open("./database/library.json", "r+") as json_file:
            data = json.load(json_file)
            for book in data:
                if book["bookID"] == id_book:
                    book["in library"] = True
                    book["check-out date"] = ""
                    book["due date"] = ""
                    book["checked-out by"] = ""
                    with open("./database/library.json", "w") as json_file:
                        json.dump(data, json_file, indent=4)
                    return True

    def add_book():
        """This method adds a new book in library"""
        id_book = input("Enter id book: ")
        title = input("Enter title: ")
        with open("./database/library.json", "r+") as json_file:
            data = json.load(json_file)
            data.append({
                "bookID":id_book, 
                "title":title, 
                "reservation":False, 
                "reservation date":"", 
                "in library":True, 
                "check-out date":"", 
                "due date":""
            })
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            

    def delete_book():
        """This method deletes a book from library"""
        id_book = input("Enter id book: ")
        with open("./database/library.json", "r+") as json_file:
            data = json.load(json_file)
        for book in data:
            if book["bookID"] == id_book:
                data.pop(int(id_book) - 1)
                with open("./database/library.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)
                return True

    def browse_catalog():
        """This method browses the catalog of books in library"""
        title = input("Enter title: ")
        with open("./database/library.json", "r") as json_file:
            data = json.load(json_file)
            for book in data:
                if book["title"] == title:
                    print(book)
                    return True


class UserTools:
    def __init__(self,user_name):
        self.user_name = user_name
    

    def borrow_book(self):
        """This method borrows a book from library"""
        title = input("Enter title of book: ")
        with open("./database/library.json", "r+") as json_file:
            data = json.load(json_file)
            for book in data:
                if book["title"].lower() == title.lower() and book["in library"] == True and book["reservation"] == False:
                    book["in library"] = False
                    book["checked-out by"] = self.user_name
                    today_date = date.today()
                    book["check-out date"] = today_date.strftime("%Y/%m/%d")
                    due_date = today_date + timedelta(days=14)
                    book["due date"] = due_date.strftime("%Y/%m/%d")
                    with open("./database/library.json", "w") as json_file:
                        json.dump(data, json_file, indent=4)
                    return True


    def reservation_book(self):
        """This method reserves a book in library"""
        title = input("Enter title of book: ")
        with open("./database/library.json", "r+") as json_file:
            data = json.load(json_file)
            for book in data:
                if book["title"].lower() == title.lower() and book["in library"] == False and book["reservation"] == False:
                    book["reservation"] = True
                    today_date = date.today()
                    book["reservation date"] = today_date.strftime("%Y/%m/%d")
                    with open("./database/library.json", "w") as json_file:
                        json.dump(data, json_file, indent=4)
                    return True


    def prolong_book(self):
        """This method prolongs a book in library"""
        title = input("Enter title of book: ")
        with open("./database/library.json", "r+") as json_file:
            data = json.load(json_file)
            for book in data:
                if book["title"].lower() == title.lower() and book["checked-out by"].lower() == self.user_name.lower():
                    date = datetime.strptime(book["check-out date"], "%Y/%m/%d")
                    due_date = date + timedelta(days=14)
                    book["due date"] = due_date.strftime("%Y/%m/%d")
                    with open("./database/library.json", "w") as json_file:
                        json.dump(data, json_file, indent=4)
                    return True


    def find_book(self):
        """This method finds a book in library"""
        title = input("Enter title of book: ")
        author = input("Enter author of book (If you know author of book): ")
        description = input("Enter description of book (If you know something about description of book): ")
        with open("./database/library.json", "r") as json_file:
            data = json.load(json_file)
            for book in data:
                if book["title"].lower() == title.lower() or book["author"].lower() == author.lower() or description.lower() in book["description"].lower():
                    print("Title ",  book["title"], 
                          "Author: ", book["author"], 
                          "Description: ", book["description"], 
                          "Reservation: ", book["reservation"], 
                          "Reservation date: ", book["reservation date"],
                          "In library: ", book["in library"], 
                          "Due date: ", book["due date"], sep=" ")
                    return True