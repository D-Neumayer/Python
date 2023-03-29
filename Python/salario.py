import time

sal = int(input("Qual o seu Salario?"))
if sal <= 0:
    print("Salario não pode ser negativo ou zero")
    exit()
time.sleep(1)
au = int(input("Quanto foi a porcentagem do Aumento?"))
if au <= 0:
    print("Aumento não pode ser Negativo ou zero")
    exit()
au = au * 0.01
val = sal * au
sal = sal + val
time.sleep(2)
print("Este é o seu novo salario:", sal)
exit()
