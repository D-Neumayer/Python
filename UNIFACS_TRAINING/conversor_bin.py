import time
def decimalToBinary(n):
 
    if(n > 1):
        # divide with integral result
        # (discard remainder)
        decimalToBinary(n//2)
 
     
    print("Esse é seu valor convertido:", n%2, end=' ')

def binaryToDecimal(binary):
 
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print("Esse é seu valor convertido:",decimal)

# Loop infinito para repetição caso numero inserido for invalido
while(1):
    print("Escolha qual tipo de conversão: Binario para Decimal: 1, Decimal para Binario: 2 ou sair: 3")
    tip = int(input())
    num = 0
    # Função para conversão de Binario
    if(tip == 1):
        print("Digite seu codigo em Binario: ")
        num = int(input())
        binaryToDecimal(num)
        exit()
    # Função para Conversão de Decimal
    elif(tip == 2):
        print("Digite seu codigo em Decimal: ")       
        num = int(input())
        decimalToBinary(num)
        exit()
    # Função de Saida
    elif(tip == 3):
        exit()
    else:
        print("Valor não reconhecido.")
        time.sleep(1)

   