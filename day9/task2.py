num1=int(input("Enter num1 is:"))
num2=int(input("Enter num2 is:"))
num3=int(input("Enter num3 is:"))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is gratest")
    else:
        print(f"{num1} is smallest")
elif num2 > num1:
    if num2 > num3:
        print(f"{num2} is gratest")
    else:
        print(f"{num2} is smallest")
elif num3 > num1:
    if num3 > num2:
        print(f"{num3} is gratest")
    else:
        print(f"{num3} is smallest")