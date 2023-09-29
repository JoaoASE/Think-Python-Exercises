class User():

    def __init__(self,first_name, last_name,area):
        self.first_name = first_name
        self.last_name = last_name
        self.area = area

    def describe_user(self):
        print("This is "+ self.first_name, self.last_name + ". This person is going to be the manager of " + self.area)

    def greet_user(self):
        print("Saudations, Mr(s) " + self.last_name + "! Welcome to our team.")


manager1 = User("Maria","Hill","Logistic Area")
manager2 = User("Tony","Stark","Technology Area")
manager3 = User("Phil", "Coulson","Comercial Area")


manager1.describe_user()
manager1.greet_user()
manager2.describe_user()
manager2.greet_user()
manager3.describe_user()
manager3.greet_user()