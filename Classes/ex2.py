class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("This is Restaurant name is " + self.restaurant_name + ". The speciality of the house is " + self.cuisine_type )
    
    def open_restaurant(self):
        print(self.restaurant_name + " is open !")


restaurant = Restaurant("Gusteau","French cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()
