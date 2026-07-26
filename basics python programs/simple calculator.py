a=int(input("enter a number: "))
b=int(input("enter a number: "))
sum=input("enter a operators (+,-,*,/" )
if sum == '+':
    print("Result =", a + b)
elif sum == '-':
    print("Result =", a - b)
elif sum == '*':
    print("Result =", a * b)
elif sum == '/':
    print("Result =", a / b)
else:
    print("invalid operator")
