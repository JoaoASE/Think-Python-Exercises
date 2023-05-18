#Modifique a função make_shirt() de modo que as camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
#uma camiseta grande e outra média com a mensagem default, e uma camiseta de qualquer tamanho com uma mensagem diferente.

def make_shirt(size_shirt = '22',description = ' I love Python'):
    print("This size shirt is "+size_shirt+" and"+ description)
make_shirt()