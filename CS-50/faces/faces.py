
def convert():
    emo = input("Send me some Emoticons to Change: \n")
    emo = emo.replace(":(", "🙁")
    emo = emo.replace(":)", "😐")
    print(emo)


def main():
    convert()


main()
