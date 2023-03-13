import time


print("Para ser aprovado sua nota devera ser maior que 7")
time.sleep(2)
nota1 = int(input("Qual a sua nota da AV1?"))
nota2 = int(input("Qual a sua nota da AV2?"))
nota3 = int(input("Qual a sua nota da AV3?"))

tot = nota1 + nota2 + nota3
med = tot/3
if med >= 7:
    print("A media do aluno é:", med)
    time.sleep(2)
    print("Aluno aprovado!")
else:
    print("A media do alune é:", med)
    time.sleep(2)
    print("Aluno devera fazer a AV4 proximo semestre.")

exit()
