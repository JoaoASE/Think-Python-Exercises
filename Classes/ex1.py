class Dog():

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+" is sitting now")
    def roll_over(self):
        print(self.name.title()+" rolled over !")


my_dog = Dog("Lolla",6)
my_dog.sit()
my_dog.roll_over()



