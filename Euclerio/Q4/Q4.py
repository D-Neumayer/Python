import csv
from datetime import date
arquivo = input("Arquivo a abrir: ")
substituir = input("Que palavra quer substituir: ")
nova_palavra = input("Nova palavra: ")
with open(arquivo, "r") as file:
    text = file.read()
text = text.replace(substituir, nova_palavra)
data = date.today()
print(data)
with open(f"{substituir}_{nova_palavra}__{data}.txt", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([text])
