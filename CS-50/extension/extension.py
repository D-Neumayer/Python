def extensions():
    file = input("File name: ").lower()

    if file.endswith(".txt"):
        print("file/txt")
    elif file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".pdf"):
        print("file/pdf")
    elif file.endswith(".zip"):
        print("file/zip")
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        print("image/jpeg")
    else:
        print("Not a File")


def main():
    extensions()


main()
