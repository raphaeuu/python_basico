nome_usuario = input('Informe seu nome: ')
altura_usuario = float(input('Insira sua altura: '))
peso_usuario = float(input('Insira seu peso: '))
calculo_usuario = round(peso_usuario / altura_usuario ** 2, 2)

print(f'{nome_usuario}, seu Índice de Massa Corpórea (IMC) é: ', calculo_usuario)

if calculo_usuario < 18.5:
    print(f'{nome_usuario}, você está em um nível de magreza elevado, com grau zero (0) de obesidade.')
elif calculo_usuario > 18 and calculo_usuario == 25:
    print(f'{nome_usuario}, você está em um nível normal, com grau 0 (zero) de obesidade.')
elif calculo_usuario == 25 and calculo_usuario < 29.9:
    print(f'{nome_usuario}, você está em um nível de sobrepreso, com grau  I (um) de obesidade.')
elif calculo_usuario == 30 and calculo_usuario < 39.9:
    print(f'{nome_usuario}, você está em um nível de obesidade, com grau dois II (dois) de obesidade.')
elif calculo_usuario > 40:
    print(f'{nome_usuario}, você está em um nível de obesidade grave, com grau III (três) de obesidade.')
else:
    print('Tente novamente inserindo seu peso e altura corretamente, usando número e se caso precisar, separar com ponto (.) .')