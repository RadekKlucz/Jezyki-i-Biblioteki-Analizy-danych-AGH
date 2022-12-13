import hashlib 
import json

class Librarian:
    def __init__(self, id_number, password):
        self.id_number = id_number
        self.password = hashlib.md5(password.encode()).hexdigest()

    
    def __create_librarian(self):
        """This method creates a new librarian. Method is private and it is only available for root"""
        with open("./database/credentials_librarian.json", "r+") as json_file:
            data = json.load(json_file)
            data.append({
                "id_number": self.id_number,
                "password": self.password
            })
            json_file.seek(0)
            json.dump(data, json_file, indent=4)


    def login_librarian(self):
        """This method checks if the id number and password are correct for librarian"""
        with open("./database/credentials_librarian.json", "r") as json_file:
            data = json.load(json_file)
            for librarian in data:
                if self.id_number == librarian["id_number"] and self.password == librarian["password"]:
                    return True
                

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.md5(password.encode()).hexdigest()


    def create_user(self):
        """This method creates a new user. Method is only available for librarian"""
        confirm_password = input("Confirm your password: ")
        confirm_password = hashlib.md5(confirm_password.encode()).hexdigest()
        if self.password == confirm_password:
            with open("./database/credentials_user.json", "r+") as json_file:
                data = json.load(json_file)
                data.append({
                    "username": self.username,
                    "password": self.password
                })
                json_file.seek(0)
                json.dump(data, json_file, indent=4)
            return True
        else:
            return False


    def login_user(self):
        """This method checks if the username and password are correct for user"""
        with open("./database/credentials_user.json", "r") as json_file:
            data = json.load(json_file)
            for user in data:
                if self.username == user["username"] and self.password == user["password"]:
                    return True