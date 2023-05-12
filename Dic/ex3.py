#exemplo de laço for com todos as chave-valor em dicionário

favortite_langueages = {'joao':'python','joel':'javascript','moises':'java'}

for name,lang in favortite_langueages.items():    #repare que deve-se implantar duas variaveis para a chave(name) e valor(lang)
    print (name.title() + " loves " + lang.title())


#exemplo de percorrer somente com a chave -- método keys()

for name in favortite_langueages.keys():
    print(name.title())

#exemplo de percorrer somente com o valor -- método values()    

for lang in favortite_langueages.values():
    print(lang.title())