def main():
    time = input("What time is it? ")
    hours = convert(time)
    if (7.0 <= hours <= 8.0):
        print("Breakfast Time")
    elif (12.0 <= hours <= 13.0):
        print("Lunch Time")
    elif (18.0 <= hours <= 19.0):
        print("Dinner Time")


def convert(time):
    try:
        hours, minutes = time.split(":")
    except ValueError:
        print("Enter a Valid hour format like (HH:MM)")
        main()

    minutes = float(minutes)/60
    hours = float(hours) + float(minutes)
    return hours


if __name__ == "__main__":
    main()
