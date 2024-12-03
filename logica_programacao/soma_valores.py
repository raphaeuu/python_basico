a = int(input('Insira o valor A: '))
b = int(input('Insira o valor B: '))


if a == b: 
        c = a + b
        print(
            f'O resultado de {a} + {b} = {c}.'
            )
        
elif a != b:
        c = a * b
        print(
            f'O resultado de {a} x {b} = {c}.'
            )

else:
    print('Insira um valor válido e tente novamente.')