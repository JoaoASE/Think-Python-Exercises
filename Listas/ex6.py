#exercício de laço para encontrar o cubo do range de todos os numeros
squares = []   #lista sem valor
for value in range(1,11): 
 square = value**3
 squares.append(square)
 print(squares)

#list comprehension
compre = [i**3 for i in range(1,11) ]
print(compre)

