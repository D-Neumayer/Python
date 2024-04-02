def main():
    machine()


def machine():
    amount_due = 50
    while True:
        print("Amount Due: ", amount_due)
        coins = int(input("Insert Coin: "))
        amount_due = amount_due - coins
        if amount_due <= 0:
            amount_due = amount_due * -1
            print("Change Owed: ", amount_due)
            break


main()
