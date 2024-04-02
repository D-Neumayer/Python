import csv
from datetime import datetime
s = int(input("Quanto você ganha por hora? "))
hrs = int(input("Quantas horas você trabalha no mês? "))
tot = s*hrs
print("Salario Bruto:", tot)
inss = tot * 0.1
print("Valor do INSS:", inss)
sind = tot * 0.02
print("Valor para o Sindicato:", sind)
imp = tot * 0.15
liq = tot - imp - inss - sind
print("Salario Liquido:", liq)
valores = {"Salario Bruto": tot, "Valor do INSS": inss,
           "Valor para o Sindicato": sind, "Salario Liquido": liq}
hora = datetime.now()

with open('data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(["Descrição", "Valor"])
    for key, value in valores.items():
        writer.writerow([key, value])
    writer.writerow([hora])
    writer.writerow(" ")
