idade = int(input("Digite sua idade: "))
jogou_3_vezes = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ").capitalize()
vitorias = int(input("Quantos jogos já venceu? "))

jogou_3_vezes = jogou_3_vezes == "True"

pode_entrar = (idade >= 16 and idade <= 18) and jogou_3_vezes and vitorias >= 1

print("Apto para ingressar no clube de jogos de tabuleiro:", pode_entrar)