# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     if senha_digitada == senha_salva:
#         break

#     repeticoes = repeticoes + 1
    

# print('\n')
# print(f'Número de tentativas: {repeticoes}')
# print('O laço acima pode ter repetições infinitas.')


texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

