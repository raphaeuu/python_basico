"""
For + Range
Range -> range(start, stop, step)
iter -> me entregue seu iterador
next -> me entregue o próximo valor

"""


""""
texto = iter('Luiz')#.__iter__()
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())

"""

# texto = 'Luiz' # iterável
# iterador = iter(texto) # iterator

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break


for i in range(3):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')
