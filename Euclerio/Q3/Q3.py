frase = input("Digite sua Frase: ").lower()
frase = frase.split(' ')
contador = {}
for palavras in frase:
    if palavras in contador:
        contador[palavras] += 1
    else:
        contador[palavras] = 1
for palavra, valor in contador.items():
    print(f"'{palavra}' aparece {valor} vezes.")
