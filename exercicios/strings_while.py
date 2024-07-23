"""

Iterando strings com While

"""
#       12345678010111213
nome = input('Insira um nome: ') # Iteráveis
#       13121110987654321
indice = 0
novo_nome = ('')

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    print(nome[indice])
    indice += 1

novo_nome += f'*'
print(novo_nome)