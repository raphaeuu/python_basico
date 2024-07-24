"""

Calculadora com While
(+, -, * , /)

"""
import os

while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Insira o operador (+/*-): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    def finalizar_calculadora():
        os.system('cls')
        print('Finalizando o cálculo, muito obrigado!')
        print('Calculadora liberada! Insira os números abaixo para usar novamente.')

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos. ❌')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido. ❌')
        continue

    if len(operador) > 1:
        print('Digite apenas 1 (um) operador.')
        continue


    print('Realizando a sua conta. Confira o resultado abaixo:\n ')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ',num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = ',num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ',num_1_float + num_2_float)
    else:
        print('Se você chegou aqui, alguma coisa errada aconteceu... 😕 ')

    sair = input('Deseja sair? Tecle [S] e Enter para confirmar: ').lower().startswith('S')

    if sair is True:
        break

    finalizar_calculadora()


