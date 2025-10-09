# Inicializa o total da compra como 0
total = 0

# Lê os dados do produto 1
nome1 = input("Digite o nome do produto 1: ")
preco1 = float(input("Digite o preço unitário do produto 1: "))
quant1 = int(input("Digite a quantidade do produto 1: "))
# Calcula o subtotal do produto 1 e soma ao total
total += preco1 * quant1

# Lê os dados do produto 2
nome2 = input("Digite o nome do produto 2: ")
preco2 = float(input("Digite o preço unitário do produto 2: "))
quant2 = int(input("Digite a quantidade do produto 2: "))
# Calcula o subtotal do produto 2 e soma ao total
total += preco2 * quant2

# Lê os dados do produto 3
nome3 = input("Digite o nome do produto 3: ")
preco3 = float(input("Digite o preço unitário do produto 3: "))
quant3 = int(input("Digite a quantidade do produto 3: "))
# Calcula o subtotal do produto 3 e soma ao total
total += preco3 * quant3

# Exibe o preço total formatado com separador de milhar e duas casas decimais
print(f"Total: R${total:,.2f}")