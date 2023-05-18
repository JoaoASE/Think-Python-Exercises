#Escreva uma função chamada describe_city() que aceite o nome de uma cidade e seu país. A função deve exibir uma frase simples,
#como Reykjavik está localizada na Islândia. Forneça um valor default ao parâmetro que representa o país.
#Chame sua função para três cidades diferentes em que pelo menos uma delas não esteja no país default.

def describe_city(city,country):
    print("A cidade "+city.title()+ " localiza-se no país "+country.upper())
describe_city('rio de janeiro','brasil')
describe_city('paris','frança')

