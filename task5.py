class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
class UserManager:
    def __init__(self):
        self.list_of_users = []
    def register(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        new_user = User(first_name, last_name, username, password)
        self.list_of_users.append(new_user)
        print("User registered successfully!")
    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for user in self.list_of_users:
            if user.username == username:
                if user.password == password:
                    print("Login successful!")
                else:
                    print("Password incorrect.")
        print("User with this username not found.")

    def change_password(self):
        username = input("Enter your username: ")
        old_password = input("Enter your old password: ")
        new_password = input("Enter your new password: ")
        
        for user in self.list_of_users:
            if user.username == username:
                if user.password == old_password:
                    user.password = new_password
                    print("Password changed successfully!")
                else:
                    print("Old password incorrect.")
        print("User with this username not found.")

    def get_users(self):
        for user in self.list_of_users:
            print("First Name:", user.first_name)
            print("Last Name:", user.last_name)
            print("Username:", user.username)
            print("Password:", user.password)
my_user = UserManager()
my_user.register()
my_user.register()
my_user.get_users()
my_user.login()
my_user.change_password()
my_user.get_users()