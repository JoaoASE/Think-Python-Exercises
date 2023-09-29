class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("This restaurant's name is " + self.restaurant_name + ". The specialty of the house is " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is open !")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant("Gusteau", "French cuisine")
print("Number of customers served:", restaurant.number_served)
restaurant.set_number_served(50)
print("Number of customers served:", restaurant.number_served)
restaurant.increment_number_served(20)
print("Number of customers served:", restaurant.number_served)
