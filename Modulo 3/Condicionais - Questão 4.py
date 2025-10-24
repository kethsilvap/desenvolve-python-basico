classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").lower()
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

if classe == "guerreiro":
    atributos_ok = forca >= 15 and magia <= 10
elif classe == "mago":
    atributos_ok = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    atributos_ok = forca <= 15 and magia <= 15 and forca > 0 and magia > 0
else:
    atributos_ok = False

print("Pontos de atributo consistentes com a classe escolhida:", atributos_ok)