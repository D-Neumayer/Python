def media(list):
    digitos = 0
    soma = 0
    for numero in list:
        numero = int(numero)
        digitos += 1
        soma = soma + numero
    media = soma/digitos
    return media


def mediana(list):
    i = 0
    comprimento = len(list)
    list = [eval(i) for i in list]
    list.sort()
    if comprimento % 2 != 0:
        mediana = comprimento//2
        print("Mediana: ", list[mediana])
    else:
        valor_1 = comprimento // 2
        valor_2 = valor_1 - 1
        mediana = (list[valor_1] + list[valor_2])/2
        print(f"Mediana: {mediana}")


def moda(list):
    contador = {}
    for numero in list:
        if numero in contador:
            contador[numero] += 1
        else:
            contador[numero] = 1
    contador = sorted(contador.items(), key=lambda x: x[1])
    contador = dict(contador)
    for numero, quantidade in contador.items():
        pass
    if quantidade == 1:
        print("Não há moda")
    else:
        print(f"Moda: {numero} aparece {quantidade} vezes.")


def desvio_padrao(list):
    valor = media(list)
    total = 0
    quantidade = 0
    for numero in list:
        quantidade += 1
        numero = int(numero)
        total = total + ((numero - valor) * (numero - valor))
    total = (total/quantidade)**0.5
    print(f"Desvio Padrão:", "%.1f" % total)


def variancia(list):
    valor = media(list)
    total = 0
    quantidade = 0
    for numero in list:
        quantidade += 1
        numero = int(numero)
        total = total + ((numero - valor) * (numero - valor))
    total = total/quantidade
    print(f"Variância:", "%.1f" % total)


def main():
    # funcao = input("Qual Fução voce que usar(Media / Mediana / Moda / Desvio Padrão)? ").lower()
    list = input(
        "Digite os numeros para a mediana (separados por espaços): ").strip()
    list = list.split(' ')
    # if funcao == "mediana":
    mediana(list)
    # elif funcao == "media" or funcao == "média":
    valor = media(list)
    print("Media: ", "%.1f" % valor)
    # elif funcao == "moda":
    moda(list)
    # elif funcao == "desvio padrão" or funcao == "desvio padrao":
    desvio_padrao(list)
    # elif funcao == "variancia" or funcao == "variância":
    variancia(list)
    # else:
    print("Função invalida")


main()
