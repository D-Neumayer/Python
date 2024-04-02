def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid: ", plate)
    else:
        print("Invalid")


def is_valid(s):
    if first_two(s):
        print("First two characters must be Letters")
        return False
    if betw_26(s):
        print("Must have between 2 and 6 characters")
        return False
    if numbers(s):
        print("Numbers only at the end!")
        return False
    if not_alphanum(s):
        print("Only numbers and Letters are permited")
    return True


def first_two(s):
    count = 1
    for i in s:
        if count <= 2:
            if not i.isalpha():
                return True
            count += 1
    return False


def betw_26(s):
    char = 0
    for i in s:
        char += 1
    if 2 <= char <= 6:
        return False
    else:
        return True


def numbers(s):
    numb = False
    for i in s:
        if i.isnumeric():
            numb = True
        elif numb and i.isalpha:
            return True
    return False


def not_alphanum(s):
    for i in s:
        if not i.isalnum():

            return True
    return False


main()
