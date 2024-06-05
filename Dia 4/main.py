from random import randint
print("bem-vindo(a) ao jogo de pedra, papel ou tesoura!\n" )
escolha = input("Digite aqui a sua escolha: ")

opcao = escolha.lower()

emoji = ""
emoji_machine = ''


random_int = randint(0, 2)
machine_choice = ""
if random_int == 0:
    machine_choice = str('pedra')
elif random_int == 1:
    machine_choice = str('papel')
else:
    machine_choice = str('tesoura')


if opcao == 'tesoura':
    emoji =='✂'

if opcao == "pedra":
    if machine_choice == 'pedra':
        print(f'Voce escolheu {opcao} {emoji} e a maquina escolheu {machine_choice}, vocês empataram!')
    elif machine_choice == 'tesoura':
        print(f'Voce escolheu {opcao} {emoji} e a maquina escolheu {machine_choice}, você perdeu...')
    else:
        print(f'Voce escolheu {opcao} {emoji} e a maquina escolheu {machine_choice}, você ganhou!')
elif opcao == 'papel':
    if machine_choice == 'pedra':
        print(f'Voce escolheu {opcao} e a maquina escolheu {machine_choice}, você ganhou!')
    elif machine_choice == 'tesoura':
        print(f'Voce escolheu {opcao} e a maquina escolheu {machine_choice}, você perdeu...')
    else:
        print(f'Voce escolheu {opcao} e a maquina escolheu {machine_choice}, vocês empataram!')
elif opcao == 'tesoura':
    if machine_choice == 'pedra':
        print(f'Voce escolheu {opcao} e a maquina escolheu {machine_choice}, você perdeu...')
    elif machine_choice == 'tesoura':
        print(f'Voce escolheu {opcao} e a maquina escolheu {machine_choice}, vocês empataram!')
    else:
        print(f'Voce escolheu {opcao} e a maquina escolheu {machine_choice}, você ganhou!')
else:
    print('Houve um erro de digitação ou valor nulo! Reinicie o programa')