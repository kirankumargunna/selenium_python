# -----------------------------------------------------single inheritance----------------------

# Parent class
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        return f"{self.username} has logged in."

    def logout(self):
        return f"{self.username} has logged out."

    def display_info(self):
        return f"Username: {self.username}, Email: {self.email}"

# Child class
class Admin(User):
    def __init__(self, username, email, admin_level):
        super().__init__(username, email)  # Call to the parent class constructor
        self.admin_level = admin_level

    def manage_users(self):
        return f"{self.username} can manage users at level {self.admin_level}."

# Create instances of User and Admin
user1 = User("john_doe", "john@example.com")
admin1 = Admin("admin_user", "admin@example.com", "super")

# Call methods on User instance
print(user1.login())  
print(user1.display_info())  
print(user1.logout())  

# Call methods on Admin instance
print(admin1.login())  
print(admin1.display_info())  
print(admin1.manage_users())  
print(admin1.logout())  


# -------------------------------------------------------Multiple Inheritance-------------

# Another Parent class
class Moderator:
    def __init__(self, moderation_level):
        self.moderation_level = moderation_level

    def moderate_content(self):
        return f"Moderating content at level {self.moderation_level}."

# Child class inheriting from User and Moderator
class Editor(User, Moderator):
    def __init__(self, username, email, moderation_level):
        User.__init__(self, username, email)  # Initialize User part
        Moderator.__init__(self, moderation_level)  # Initialize Moderator part

    def edit_content(self):
        return f"{self.username} is editing content."

# Create an instance of Editor
editor1 = Editor("editor_user", "editor@example.com", "high")

# Call methods from User and Moderator
print(editor1.login())
print(editor1.display_info())
print(editor1.moderate_content())
print(editor1.edit_content())
print(editor1.logout())


#------------------------------------Hierarchical Inheritance---------

# Child class: Editor
class Editor2(User):
    def __init__(self, username, email, moderation_level):
        super().__init__(username, email)  # Call to the parent class constructor
        self.moderation_level = moderation_level

    def edit_content(self):
        return f"{self.username} is editing content."

# Create instances of Admin and Editor
admin2 = Admin("admin_user", "admin@example.com", "super")
editor2 = Editor2("editor_user", "editor@example.com", "high")

# Call methods from Admin instance
print(admin2.login())
print(admin2.display_info())
print(admin2.manage_users())
print(admin2.logout())

# Call methods from Editor instance
print(editor2.login())
print(editor2.display_info())
print(editor2.edit_content())
print(editor2.logout()) 