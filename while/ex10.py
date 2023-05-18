sandwiches_orders = ['atum', 'sausage','angus','chicken']
# Criando a lista vazia para os sanduíches prontos
finished_sandwiches = []

while sandwiches_orders:
    pedido = sandwiches_orders.pop(0)
    print(f"Seu sanduíche {pedido} está sendo preparado")

    finished_sandwiches.append(pedido)

    print("Os seguintes sanduíches foram preparados:")
for sanduiche in finished_sandwiches:
    print(f"- {sanduiche}")
