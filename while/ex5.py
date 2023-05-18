#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.

user = input("Insira o nome de usuario: ")
psswd = input("Insira a senha")

while user == psswd:
    print("ERRO !")
    psswd = input("Crie uma senha diferente do usuário")
    print("Cadastro criado !")
