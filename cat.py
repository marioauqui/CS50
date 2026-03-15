
#i = 10
#while i != 0:

	#print("Meow, meow, woof")

	#i = i - 1


#i = 0
#while i < 3:
#	print("Hi!")
#	i += 1


#while True:
#	n = int(input("What's n? "))
#	if n > 0:
#		break

#for _ in range(n):
#	print("meow")

def main():
    number = getnumber()
    meow(number)


def getnumber():
    while True:
        n = int(input("Pick a number n (make sure it's positive): " ))
        if n > 0:
              return n

def meow(n):
     for _ in range(n):
          print("Meow")

main()


