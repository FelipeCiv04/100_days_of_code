import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo(a) ao gerador de senhas em python")
nr_letters = int(input("Quantas letras você gostaria de ter na sua senha?\n")) 
nr_symbols = int(input(f"Quantos simbolos você gostaria de ter na sua senha?\n"))
nr_numbers = int(input(f"Quantos números você gostaria de ter na sua senha? \n"))

letrasSenha = []
simbolosSenha = []
numerosSenha = []

for nl in range(1, nr_letters + 1, 1):
    letrasSenha.append(random.choice(letters))
     
for ns in range(1, nr_symbols + 1, 1 ):
    simbolosSenha.append(random.choice(symbols))

for nn in range(1, nr_numbers + 1, 1):
    numerosSenha.append(random.choice(numbers))

caracteres_da_senha = simbolosSenha + numerosSenha + letrasSenha

random.shuffle(caracteres_da_senha)

senha_final = ''.join(caracteres_da_senha)

print(f'Sua senha nova pode ser: {senha_final}')

fim = int(input('...'))