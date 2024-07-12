usuario_1 = input('Insira o nome do jogador 1: ')
usuario_2 = input('Insira o nome do jogador 2: ')
valor_1 = int(input(f'{usuario_1}, digite o primeiro valor: '))
valor_2 = int(input(f'{usuario_2}, digite o segundo valor: '))
print('\n')


if valor_1 > valor_2:
    print(f'{usuario_1}, seu valor é maior. ({valor_1})')
    print('\n')
    print(f'Valor escolhido por {usuario_2}: {valor_2}')
elif valor_2 > valor_1:
    print(f'{usuario_2}, seu valor é maior. ({valor_2})')
    print('\n')
    print(f'Valor escolhido por {usuario_1}: ({valor_1})')
else:
    print('Digite um valor válido e tente novamente, obrigado!')

