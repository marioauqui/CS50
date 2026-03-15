expression = input("Expression: ").split()

x = float(expression[0])

op = expression[1]

y = float(expression[2])


if op == "+":
    print(x + y)

elif op == "-":
    print(x - y)

elif op == "*":
    print(x * y)

elif op == "/":
    print(x / y)
