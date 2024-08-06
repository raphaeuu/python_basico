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

texto = 'Luiz' # iterável
iterador = iter(texto) # iterator

while True:
    try:
        print(next(iterador))
    except StopIteration:
        print()