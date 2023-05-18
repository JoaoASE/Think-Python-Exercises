responses = {}
polling_active = True

while polling_active:
    name = input("Your name ? ")
    response = input("What mountain do you want to climb ? ")

    responses[name] = response
    repeat = input("Would you like to someone else answer the question for you ? ")
    if repeat == 'no':
        polling_active = False

        for name, response in responses.items(): 
            print(name + " would like to climb " + response + ".")
