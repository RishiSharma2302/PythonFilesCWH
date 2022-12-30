# Faulty calculator

def calculator():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    op = (input("Enter the operation (+, -, *, /, %): "))

    if op == "+":
        if ((n1 == 56 and n2 == 9) or (n1 == 9 and n2 == 56)):
            print("NAHI BATAUNGA!!!")
        else:
            print(n1 + n2)
    if op == "-":
        print(n1 - n2)
    if op == "*":
        if ((n1 == 45 and n2 == 3) or (n1 == 3 and n2 == 45)):
            print("NAHI BATAUNGA!!!")
        else:
            print(n1 * n2)
    if op == "/":
        if (n1 == 56 and n2 == 6):
            print("NAHI BATAUNGA!!!")
        else:
            print(int((n1 / n2)))
    if op == "%":
        print(n1 % n2)

    again()

def again():
    ch = input("Run again? (y/n): ")
    if ch=='y':
        calculator()
    elif ch=='n':
        print("Program made through Rishi, Thak you")
    else:
        again()

calculator()