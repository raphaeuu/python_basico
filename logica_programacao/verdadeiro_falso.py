valor1 = input('Digite o primeiro valor lógico (True/False): ').strip().capitalize()
valor2 = input('Digite o segundo valor lógico (True/False): ').strip().capitalize()

valor1 = True if valor1 == 'True' else False
valor2 = True if valor2 == 'True' else False

if valor1 and valor2:
    print('Ambos são valores VERDADEIROS.')

elif not valor1 and not valor2:
    print('Ambos os valores são FALSOS.')
