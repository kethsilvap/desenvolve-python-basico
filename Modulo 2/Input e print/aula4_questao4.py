# Lê o valor total em reais
valor = int(input())

# Calcula o número de notas de 100
nota100 = valor // 100
valor %= 100

# Calcula o número de notas de 50
nota50 = valor // 50
valor %= 50

# Calcula o número de notas de 20
nota20 = valor // 20
valor %= 20

# Calcula o número de notas de 10
nota10 = valor // 10
valor %= 10

# Calcula o número de notas de 5
nota5 = valor // 5
valor %= 5

# Calcula o número de notas de 2
nota2 = valor // 2
valor %= 2

# Calcula o número de notas de 1
nota1 = valor // 1
valor %= 1

# Exibe o resultado formatado
print(f"{nota100} nota(s) de R$100,00")
print(f"{nota50} nota(s) de R$50,00")
print(f"{nota20} nota(s) de R$20,00")
print(f"{nota10} nota(s) de R$10,00")
print(f"{nota5} nota(s) de R$5,00")
print(f"{nota2} nota(s) de R$2,00")
print(f"{nota1} nota(s) de R$1,00")