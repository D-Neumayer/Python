def meaning():
    quest = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? \n")
    if (quest == "42"):
        print("YES")
    elif (quest == "forty-two"):
        print("YES")
    elif (quest == "forty two"):
        print("YES")
    else:
        print("NO")


def main():
    meaning()


main()
