#Escreva um laço que peça ao usuário para
#fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
#fornecido

ingredientes = input("Escolha os ingredientes da pizza: ")

while ingredientes != "quit":
    print("Adicionado !")
    ingredientes = input("Continue escolhendo  ")
    print("Saiu !")
    
    
