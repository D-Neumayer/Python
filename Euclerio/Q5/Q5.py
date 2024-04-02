def main():
    checa_nome()
    checa_idade()
    checa_salario()
    checa_sexo()
    checa_estado_civil()


def checa_nome():
    while True:
        nome = input("Qual seu nome? ")
        if len(nome) >= 3:
            break
        else:
            print("Nome muito curto")


def checa_idade():
    while True:
        idade = int(input("Qual sua Idade? "))
        if 0 <= idade <= 150:
            break
        else:
            print("Idade não esta entre 0 e 150")


def checa_salario():
    while True:
        salario = int(input("Qual seu Salario? "))
        if salario >= 0:
            break
        else:
            print("Salario menor que zero")


def checa_sexo():
    while True:
        sexo = input("Qual o seu Sexo(M/F)? ").lower()
        if sexo == "m" or sexo == "f":
            break
        else:
            print("Sexo invalido!")


def checa_estado_civil():
    while True:
        estado_civil = input(
            "Qual o seu Estado Civil(Solteiro/a = S, Casado/a = C, Viuvo/a = V, Divorciado/a = D)? ").lower()
        if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
            break
        else:
            print("Estado Civil Invalido")


main()
