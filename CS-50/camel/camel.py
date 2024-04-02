def main():
    camel = input("CamelCase: ")
    snake = transform(camel)
    print("snake_case: ", snake)


def transform(camel):
    snake = ""
    for i in camel:
        if i.isupper():
            snake += "_" + i.lower()
        else:
            snake += i
    return snake


main()
