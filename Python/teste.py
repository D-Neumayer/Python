tes = 1
print("Escreva o numero")
i = int(input())

while(tes != 0):   
    tes = i % 2
    i = i//10
    print(tes)

    