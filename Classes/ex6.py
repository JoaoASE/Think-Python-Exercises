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

# Criar uma instância da classe Restaurant
restaurant = Restaurant("Gusteau", "French cuisine")

# Apresentar o número de clientes atendidos (valor padrão, 0)
print("Number of customers served:", restaurant.number_served)

# Mudar o número de clientes atendidos
restaurant.set_number_served(50)

# Apresentar o novo número de clientes atendidos
print("Number of customers served:", restaurant.number_served)

# Incrementar o número de clientes atendidos
restaurant.increment_number_served(20)

# Apresentar o novo número de clientes atendidos após incrementar
print("Number of customers served:", restaurant.number_served)
