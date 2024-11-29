import random
numero_secreto = random.randint(1, 10)

while True:

    try:
        palpite = int(input("Adivinhe o número entre 1 e 10: "))
        print('\n')

        if palpite < 1 or palpite > 10:
            print('Por favor, digite um número entre 1 e 10.')
            print('\n')
            continue
        
        elif palpite == numero_secreto:
             print(f'Parabéns! Seu palpite está correto. O número correto é: ({numero_secreto})')
             break
        
        elif palpite > numero_secreto:
            print(f'{palpite} é maior do que o número secreto.')
           
        else:
            print(f'{palpite} é menor do que o número secreto.')

    except ValueError: 
        print('Erro. Tente novamente inserindo um número inteiro!')
        print('\n')