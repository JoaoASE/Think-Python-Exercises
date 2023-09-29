class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("This is Restaurant name is " + self.restaurant_name + ". The speciality of the house is " + self.cuisine_type )
    



restaurant = Restaurant("Gusteau","French cuisine")
restaurant1 = Restaurant("Napole","Italian cuisine")
restaurant2 = Restaurant("Sal","Brazillian cuisine")

restaurant.describe_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()


