aluno = input('Nome do aluno: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
calculo = (nota1 + nota2 + nota3 + nota4) / 4
media_min = 7

try:
    if calculo < media_min:
        print(f'O aluno {aluno} está em recuperação.')
        print(f'Média: {calculo:.2f}')

    elif calculo == media_min:
        print(f'O aluno {aluno} está na média e não irá para recuperação.') 
        print(f'Média: {calculo:.2f}')
        print('\n')
              
    elif calculo > media_min:
        print(f'O aluno {aluno} está acima da média, parabéns! ')
        print(f'Média: {calculo:.2f}')
        print('\n')
    
    else:
         print(f'Nota não identificada. Por favor, insira as notas para obter a média.')

except ValueError:
        print('Formato incorreto. (Ex: 7.00)')