print("Seja bem-vindo ao Cine-SIQ".upper())
print("\nEstes são os filmes disponíveis:")
filmes = ['Batman','Zorro','Barbie']

print(filmes)
print("\nSelecione o filme que deseja:")
filme_desejado = input()

if filme_desejado == filmes[0]:
    print("Ingresso confirmado")
elif filme_desejado == filmes[1]:       
    print("Ingresso confirmado")
else:
    print("Sessão lotada")
