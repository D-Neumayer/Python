def main():
    inp = input("Input: ")
    out = devownator(inp)
    print("Output: ", out)


def devownator(frase):
    result = ""
    for i in frase:
        if i.lower() not in ("a", "e", 'i', 'o', 'u'):
            result += i
    return result


main()
