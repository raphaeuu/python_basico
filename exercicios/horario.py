"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""

#Exercício 2


nome = input('Me diga o seu nome: ')
horario = int(input('Me informe seu horário: '))

try:
    if horario >= 0 and horario <= 11:
        print(f'Bom dia, {nome}!')
    elif horario >= 12 and horario <= 17:
        print(f'Boa tarde, {nome}!')
    elif horario >= 18 and horario <= 23:
        print(f'Boa noite, {nome}!')
    else:
        print(f'{nome}, hora inválida. Digite um valor entre 0 à 23.')
except:
    print('Informe apenas 2 (dois) dígitos.')