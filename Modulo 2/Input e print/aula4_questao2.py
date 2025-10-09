# Lê a temperatura em graus Fahrenheit
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# Converte a temperatura para Celsius usando a fórmula
celsius = (fahrenheit - 32) * (5/9)

# Converte o valor para inteiro
celsius_int = int(celsius)

# Exibe o resultado formatado
print(f"{fahrenheit} graus Fahrenheit são {celsius_int} graus Celsius.")