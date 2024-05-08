nome = str(input("Olá! Essa é a caçada ao tesouro em Python, qual é o seu nome? \n"))
print("")

morte = '''   ___-----------___
           __--~~                 ~~--__
       _-~~                             ~~-_
    _-~                                     ~-_
   /                                           \\
  |                                             |
 |                                               |
 |                                               |
|                                                 |
|                                                 |
|                                                 |
 |                                               |
 |  |    _-------_               _-------_    |  |
 |  |  /~         ~\\           /~         ~\\  |  |
  ||  |             |         |             |  ||
  || |               |       |               | ||
  || |              |         |              | ||
  |   \\_           /           \\           _/   |
 |      ~~--_____-~    /~V~\\    ~-_____--~~      |
 |                    |     |                    |
|                    |       |                    |
|                    |  /^\\  |                    |
 |                    ~~   ~~                    |
  \\_         _                       _         _/
    ~--____-~ ~\\                   /~ ~-____--~
         \\     /\\                 /\\     /
          \\    | ( ,           , ) |    /
           |   | (~(__(  |  )__)~) |   |
            |   \\/ (  (~~|~~)  ) \\/   |
             |   |  [ [  |  ] ]  /   |
              |                     |
               \\                   /
                ~-_             _-~
                   ~--___-___--~
'''
buraco = "Esse caminho tinha um buraco com uma armadilha, você morreu 😭"
urso = "Você foi farejado por um Urso Cinzento e ele te devorou!"

print(f"Prazer em conhecê-lo, {nome}. Você se encontra em 2 caminhos atualmente, um para a esquerda \n e outro para a direita. Para onde você acha que deveria ir? (direita ou esquerda)")
caminho1 = str(input())

if caminho1 == "esquerda":
    casa = str(input("Muito bem, este foi o caminho correto! Agora você se depara com uma casa abandonada. Você quer entrar para checar sim ou não? "))
    
    if casa == "sim":
        porta = input("Você encontrou uma passagem dentro da casa com 3 portas, uma vermelha, outra azul e por último uma verde. Qual você escolhe? ")

        if porta == "azul":
            print("PARABÉNS, VOCÊ ACHOU O TESOURO!")
        else:
            print("Você escolheu a porta errada ou não escolheu nada, você morreu.")
            print(morte)
    else:
        print(urso)
        print(morte)
else:
    print(buraco, morte)