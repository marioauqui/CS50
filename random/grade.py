#student grade calculator

score = int(input("What is your score? " ))

if 90 <= score <= 100:
    print("You got an A!")

elif 80 <= score < 90:
    print("You got an B")

elif 70 <= score < 80:
    print("You got an C")

elif 60 <= score < 70:
    print("You got an D")

else:
    print("You Failed")
