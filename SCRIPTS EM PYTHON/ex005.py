import random  #A biblioteca random é importada para gerar números aleatórios
print("Bem-vindo ao jogo de adivinhação")
print("Estou pensando em um número entre 1 e 100.")  #Essas linhas exibem uma mensagem de boas-vindas ao jogador e informam que o número a ser adivinhado está no intervalo de 1 a 100
secret = random.randint(1, 100)  #A função random.randint(1, 100) gera um número aleatório entre 1 e 100, e esse número é armazenado na variável secret
tentativas = 0  #Ela serve para contar quantas vezes o jogador tentou adivinhar o número.
while True:  #O laço continuará até que o jogador adivinhe o número corretamente (quando o programa executa break), ou seja, até que a condição de saída seja satisfeita.
    chute = int(input("Qual o seu palpite: "))  #O programa solicita ao usuário que insira um número (seu palpite
    tentativas += 1 #O contador de tentativas é incrementado em 1 a cada vez que o jogador faz um palpite, para registrar quantas tentativas foram feitas.
    if chute == secret:  # programa verifica se o palpite do jogador (chute) é igual ao número secreto gerado pelo computador (secret). Se for, o jogador venceu
        print(f"Parabéns! Você acertou o número {secret} em {tentativas} tentativas.")  #Se o palpite estiver correto, o programa exibe uma mensagem de parabéns, informando o número secreto e o número de tentativas feitas. O comando break encerra o laço while, já que o jogo foi concluído com sucesso
        break
    elif chute < secret:  #Se o palpite for menor que o número secreto, o programa entra nesta condição e avisa o jogador que o palpite está muito baixo.
        print("Seu palpite é muito baixo. Tente novamente!")
    else:  #Se o palpite não for nem igual nem menor que o número secreto, a única opção restante é que ele seja maior. 
        print("Seu palpite é muito alto. Tente novamente!")  #A mensagem informa ao jogador que o palpite é muito alto e sugere tentar novamente.
