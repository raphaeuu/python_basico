### Número 1

# try:
#     numero_usuario = input("Insira um número: ")
    
#     if numero_usuario.isdigit():
#         numero_int = int(numero_usuario)
#         par_impar = numero_int %2 == 0
#         par_impar_texto = 'Ímpar'

#         if par_impar:
#             par_impar_texto = 'Par' 

#         print(f"O número ({numero_int}) é {par_impar_texto}.")
    
#     else:
#         print(f"Esse número é ímpar. ({numero_usuario})")

# except ValueError:
#     print("Não é número inteiro. Tente novamente!")





### Número 2

# nome_usuario = input("Digite seu nome: ")
# hora_usuario = int(input(f"{nome_usuario}, agora insira um horário : "))

# try:

#     if hora_usuario >= 0 and hora_usuario <= 11:
#         print(f'Bom dia, {nome_usuario}!')
    
#     elif hora_usuario >= 12 and hora_usuario <= 17:
#         print(f'Boa tarde, {nome_usuario}!')

#     elif hora_usuario >= 18:
#         print(f'Boa noite, {nome_usuario}!')
        
#     else:
#         print('Insira um horário correto, entre 00h e 23h. ')

# except ValueError:
#     print("O formato não é correto. Insira no formato númerico!")






### Número 3

# nome_usuario = input('Insira seu nome: ')
# contagem_letra = len(nome_usuario)


# try:
#     if contagem_letra <= 4:
#         print(
#             f'({nome_usuario}) | Seu nome é curto e tem {contagem_letra} letras.'
#             )
#     elif contagem_letra == 5 and contagem_letra == 6:
#         print(
#             f'({nome_usuario}) | Seu nome é normal e tem {contagem_letra} letras.'
#             )
#     elif contagem_letra > 6:
#         print(
#             f'({nome_usuario}) | Seu nome é grande e tem {contagem_letra} letras.'
#             )
#     else:
#         print("😱")

# except ValueError:
#     print('Tente novamente inserindo apenas letras.')

