import time

nota = 0
i = 0

print("Quantas notas são?")
quant = int(input())

while (quant > i):
    
    print("Qual o valor da nota", i, "?")
    som = int(input())
    nota += som
    i += 1
    time.sleep(1)

nota = nota/quant
arr = round(nota, 1)

if nota >= 7:
    print("Aluno aprovado!")
    print("Essa é sua media:", arr)
else:
    print("Aluno reprovado!")
    print("Essa é sua media:", arr)
exit()
