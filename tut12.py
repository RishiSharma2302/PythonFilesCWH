# var1=6
# var2=56
# var3=int(input("Enter value: "))
#
# if var3>var2:
#     print("Var3 > var2")
# elif var3==var2:
#     print("equal")
# else:
#     print(("var2>var3"))

# list1=[1, 3, 5, 7, 9]
# print(15 not in list1)
# if 35 not in list1:
#     print("NOT IN THE LIST")

age = int(input("Enter your age: "))
if age>5 and age<100:
    if age>18:
        print("YOU CAN DRIVE!")
    elif age==18:
        print("CAN NOT DECIDE")
    else:
        print("YOU CAN NOT DRIVE")
else:
    print("ENTER A VALID AGE")