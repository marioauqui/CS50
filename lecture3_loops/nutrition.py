


fruit = input("Item: ").lower()


fruits = {
    "apple": 95,
    "banana": 105,
    "orange": 62,
    "strawberry": 4,
    "grape": 3,
    "watermelon": 86,
    "pineapple": 82,
    "mango": 99,
    "pear": 57,
    "peach": 58
}

if fruit in fruits:
    print(f"{fruit.capitalize()} has {fruits[fruit]} calories" )
else:
    print("We don't have that fruit")