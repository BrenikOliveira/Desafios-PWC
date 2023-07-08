texto_p = input("Digite a palavra: ")
palindromo = []
for caracter in texto_p:
    palindromo.append(caracter)
    receptora = "".join(palindromo)
    if not len(receptora) == 1 and receptora == receptora[::-1]:
        print(receptora)


