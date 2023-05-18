#exercicio de laço while com método break -- usado para sair imediatamente do laço
prompt = "\n(Enter 'quit' when you are finished.)"

while True: 
    city = input(prompt)  
    if city == 'quit': 
        break  
    else: 
        print("I'd love to go to " + city.title() + "!") 