texto_p = input("Digite a palavra: ")

def palindromo (texto):
    if texto_p == texto [::-1]:
        return True
    else:
        return False
print(palindromo(texto_p))