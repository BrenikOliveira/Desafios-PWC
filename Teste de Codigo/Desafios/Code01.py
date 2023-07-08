texto = input("Digite uma frase: ")
frase = []
frase = texto.split(" ")
frase_inv = []
i = len(frase)
for palavra in frase:
    i -= 1
    frase_inv.append(frase[i])
frase_pronta = " ".join(frase_inv)
print(frase_pronta)