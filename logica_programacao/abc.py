a = int(input('Insira o valor A: '))
b = int(input('Insira o valor B: '))
c = int(input('Insira o valor C: '))
soma = a + b

if soma > c:
    print(
        f'({soma}) é maior que ({c}).'
        )
else:
    print(
        f'({soma}) é menor ou igual a ({c}).'
        )