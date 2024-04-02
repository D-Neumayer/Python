def main():
    i = 0
    grocery(i)

def grocery(i):
    market = {"apple": i, "banana": i, "ice cream": i, "tomato": i,"lettuce":i,"carrot":i, "mango": i, "strawberry": i,"milk": i,"tortilla": i, "sweet potato": i}
    try:
        while True:
            item = input("Product: ").lower()
            if item in market:
                market[item] = market[item] + 1
            else:
                pass
    except EOFError:
        print("\n")
        for item, count in market.items():
            if count != 0:
                print(count, item.upper())
            else:
                pass
main()
