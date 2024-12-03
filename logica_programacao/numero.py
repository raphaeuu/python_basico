numero = int(input('Insira um número: '))


if numero %2 == 0 and numero > 0:
    print(f'({numero}) é par.')
    print(f'({numero}) é positivo.')

# elif numero < 0:
#     print(f'{numero} é negativo.')

# elif numero > 0:
#     print(f'{numero} é positivo.')

else:
    print(f'({numero}) é ímpar.')
    print(f'({numero}) é negativo.')

# else:
#     print(f'({numero}) é ímpar.')