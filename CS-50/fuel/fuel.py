def main():
    frac = input("Fraction: ")
    gauge(frac)


def gauge(frac):
    try:
        x, y = int(frac.split('/'))
        x = int(x)
        y = int(y)
        if x == 0:
            print("E")
        else:
            x = x * 100
            resul = str(x/y)
            perc, zero = resul.split(".")
            if zero == "0":
                print(perc + "%")
            else:
                print(resul + "%")

    except (ValueError, ZeroDivisionError):
        print("E")


main()
