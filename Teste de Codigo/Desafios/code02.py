texto = input("Digite um texto : ")
lista_letras = []
lista_palavra = []
for caracter in texto:
    lista_letras.append(caracter)
    if not caracter in lista_palavra:
        lista_palavra.append(caracter)

palavra = "".join(lista_palavra)
print(palavra)

