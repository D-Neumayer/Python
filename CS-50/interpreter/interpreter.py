def interpreter():
    ex = input("Expression: ")
    x, y, z = ex.split(" ")
    x = int(x)
    z = int(z)
    match y:
        case "+":
            res = x + z
            print(res)
        case "-":
            res = x - z
            print(res)
        case "*":
            res = x * z
            print(res)
        case "/":
            res = x / z
            print(res)


def main():
    interpreter()


main()
