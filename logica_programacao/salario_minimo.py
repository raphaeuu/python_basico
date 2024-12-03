salario_minimo = float(input('Qual o salário mínimo atual (Ex: 1.000)? '))
salario_user = float(input('Insira seu salário (Ex: 1.000): '))

quantidade = salario_user / salario_minimo

print(f'O usuário recebe aproximadamente {quantidade:.1f} salários mínimos.')