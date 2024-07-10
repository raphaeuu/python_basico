nome_usuario = input('Informe seu nome: ')
peso_usuario = float(input('Insira seu peso:'))
altura_usuario = float(input('Insira sua altura: '))
calculo_usuario = round(peso_usuario / altura_usuario ** 2)

print(f'{nome_usuario}, seu IMC é: ', calculo_usuario)


