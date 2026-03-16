name = input("What is your name? ")

match name:
    case "Harry" | "Herm" | "Ron":
        print("Griff")
    case "Draco":
        print("Sly")
    case _:
        print("Who?")

