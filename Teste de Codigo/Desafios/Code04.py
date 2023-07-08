palavras_maiusc = "hello. how are you? i'm fine, thank you."
Separador_frase = []
Conjunt_Frase = []
Separador_frase = palavras_maiusc.split(".")
VinculoFraseCompleta = ""
for frase in Separador_frase:
    Conjunt_Frase.append(frase.strip().capitalize())
for frase in Conjunt_Frase:
    VinculoFraseCompleta = ". ".join(Conjunt_Frase)
Separador_frase = VinculoFraseCompleta.split("?")
Conjunt_Frase = []
for frase in Separador_frase:
    Conjunt_Frase.append(frase.strip().capitalize())
for frase in Conjunt_Frase:
    VinculoFraseCompleta = "? ".join(Conjunt_Frase)
print(VinculoFraseCompleta)