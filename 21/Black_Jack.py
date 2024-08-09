import random

naipes = ['♦', '♠', '♥', '♣']
numeros = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']
cartas = []

# Gerar o baralho de cartas
for naipe in naipes:
    for numero in numeros:
        cartas.append(f'{numero} {naipe}')

# Dicionário para os valores das cartas
valores = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'J': 10,
    'Q': 10,
    'K': 10
}

pontos = 0

while True:
    #print('Jogo Black Jack - mais proximo do 21 Ganha')
    print()
    print("\nMenu:")
    print('====================================')
    print("1 - Pegar carta")
    print("2 - Parar")
    print("3 - Ver pontos")
    print('====================================')
    print()
    print()
    print(f'Pontos: {pontos}')
    print()


    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        carta = random.choice(cartas)  # Pega uma carta aleatória
        numero = carta.split()[0]       # Extrai o número da carta
        valor = valores[numero]         # Obtém o valor correspondente
        pontos += valor                 # Adiciona os pontos
        print(f'Você pegou: {carta} - Valor: {valor}')

    elif opcao == '2':
        print("Você parou.")
        print(f'Seu total de pontos: {pontos}')
        break

    elif opcao == '3':
        print(f'Seu total de pontos: {pontos}')

    else:
        print("Opção inválida. Tente novamente.")

 # Pergunta se o jogador quer jogar novamente
 #   jogar_novamente = input("Você quer jogar novamente? (s/n): ").strip().lower()
 #   if jogar_novamente != 's':
 #       print("Obrigado por jogar! Até a próxima!")
 #       break
