import random
numero_secreto = random.randint(1, 10)
palpite = int(input("Adivinhe o número entre 1 e 10: "))

while palpite != numero_secreto:
    print("Errado! Tente novamente.")
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    
print(f"Parabéns! O número secreto é ({numero_secreto}).")

