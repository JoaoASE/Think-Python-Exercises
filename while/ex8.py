while True:
    idade = input("Qual a sua idade? (Digite 'sair' para encerrar) ")
    if idade.lower() == 'sair':
        break
    idade = int(idade)
    if idade < 3:
        print("Seu ingresso é gratuito!")
    elif idade >= 3 and idade <= 12:
        print("O preço do seu ingresso é $10.")
    else:
        print("O preço do seu ingresso é $15.")
